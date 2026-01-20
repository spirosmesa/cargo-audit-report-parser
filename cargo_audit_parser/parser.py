import logging
from typing import Any

def parse_cargo_vulnerabilities_list(vulns_list: list) -> list[dict]:
    """
    Parses the cargo vulnerabilities list generates list of printable values.
    
    :param vulns_list: A list of vulnerabilities found by cargo-audit, as obtained 
    from corresponding JSON key in the report.
    :type vulns_list: list
    :return: A list of dictionaries each containing relevant information on a 
    vulnerability.
    :rtype: list[dict, Any]
    """
    logger = logging.getLogger(__name__)

    def _construct_affected_functions_string_(functions_dict: dict) -> str:
        outStr = ""
        for function, versions in functions_dict.items():
            outStr += function + "\n".join([version for version in versions])
            outStr += "\n"
        
        # Return constructed string without the final new line.
        return outStr[:-1]

    processed_vulns_list = []
    for vuln_index in range(0, len(vulns_list)):
        try:
            vuln = vulns_list[vuln_index]
            vulnDict = {
                "Vulnerability ID": vuln["advisory"]["id"],
                "Package Name": vuln["advisory"]["package"],
                "Package Version": vuln["package"]["version"],
                "Vulnerability Title": vuln["advisory"]["title"],
                "Description": vuln["advisory"]["description"],
                "Package Source (URL)": vuln["package"]["source"].replace("registry+", ""),
                # The date the vulnerability was first discovered in the wild.
                "Date First Discovered": vuln["advisory"]["date"],
                # Any aliases of the vulnerability, seperated by `\n`.
                "Vulnerability Aliases": "\n".join(alias for alias in vuln["advisory"]["aliases"]) if len(vuln["advisory"]["aliases"]) else "",
                # Any vulnerability categories seperated by `\n`.
                "Vulnerability Categories": "\n".join(category for category in vuln["advisory"]["categories"]) if len(vuln["advisory"]["categories"]) else "",
                # Any vulnerability references seperated by `\n`.
                "Vulnerability References": "\n".join(reference for reference in vuln["advisory"]["references"]) if len(vuln["advisory"]["references"]) else "",
                # "Registry source where the vulnerability is created."
                "Vulnerability Source": vuln["advisory"]["source"].replace("registry+", "") if vuln["advisory"]["source"] else "",
                "Vulnerability URL": vuln["advisory"]["url"],
                # Whether or not the vulnerability has been withdrawn
                "Vulnerability Withdrawn": vuln["advisory"]["withdrawn"],
                # Any patched versions for the component.
                "Patched Versions": "\n".join(version for version in vuln["versions"]["patched"]) if len(vuln["versions"]["patched"]) else "",
                # Any known unaffected versions
                "Unaffected Versions": "\n".join(version for version in vuln["versions"]["unaffected"]) if len(vuln["versions"]["unaffected"]) else "",
            }
        except Exception as e:
            logger.exception(f"Exception parsing vulnerability index {vuln_index}.")
            continue

        affectedDict = {}
        if "affected" in vuln:
            # The value of the key can be `null`.
            if vuln["affected"]:
                try:
                    affectedDict = {
                        "Affected Architecture": "\n".join([arch for arch in vuln["affected"]["arch"]]) if len(vuln["affected"]["arch"]) else "",
                        "Affected OS(es)": "\n".join([arch for arch in vuln["affected"]["os"]]) if len(vuln["affected"]["os"]) else "",
                        "Affected Functions": _construct_affected_functions_string_(vuln["affected"]["functions"]) if len(vuln["affected"]["functions"]) else ""
                    }
                except Exception as e:
                    logger.exception(f"Exception when parsing `affected` for vulnerability index: {vuln_index}.") 
                     
        vulnDict = vulnDict | affectedDict

        processed_vulns_list.append(vulnDict)

    logger.info("Parsed vulnerabilities.")
    return processed_vulns_list

def parse_cargo_file(cargo_file_path: str) -> dict[str, Any]:
    """
    Parse the JSON contents of a cargo-audit JSON report.
    
    :param cargo_file_path: The path to the cargo-audit JSON report.
    :type cargo_file_path: str
    :return: A list of dictionaries. Each dictionary represents a vulnerability.
    :rtype: dict[str, Any]
    """
    logger = logging.getLogger(__name__)
    
    with open(cargo_file_path, "r", encoding='utf-8') as fd:
        cons = json.loads(fd.read())
    
    logger.info(f"Opened contents of: {cargo_file_path}")

    try:
        resultsDict = {
            "cargo components count": cons["lockfile"]["dependency-count"]
        }
        logger.info("Obtained `cargo components count.")
    except Exception as e:
        resultsDict = {
            "cargo components count": "-"
        }
        logger.exception('`cargo components count` not be obtained.')

    # parse vulnerabilities
    if "vulnerabilities" in cons:
        if cons["vulnerabilities"]["found"]:
            resultsDict["vulnerabities"] = parse_cargo_vulnerabilities_list(cons["vulnerabilities"]["list"])
            logger.info("`Parsed cargo vulnerabilities.`")
        else:
            logger.info("No vulnerabilities were found within the cargo report.")
    else:
        logger.info("The `vulnerabilities` key was not found within the cargo report.")

    return resultsDict
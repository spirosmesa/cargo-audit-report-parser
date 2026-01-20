def get_cargo_vulnerabilities_col_descriptions() -> list[Tuple[str, str]]:
    """
    Get a list of tuples, each containing the a column name and a column description.
    
    :return: Returns the list of tuples.
    :rtype: list[Tuple[str, str]]
    """
    return [
            ("Vulnerability ID", "The ID of the vulnerability."),
            ("Package Name", "The name of the vulnerable package."),
            ("Package Version", "The version of the vulnerable package."),
            ("Vulnerability Title", "The title of the vulnerability."),
            ("Description", "A description of the vulnerability."),
            ("Package Source (URL)", "The URL of the package. Most frequently a GH link."),
            ("Date First Discovered", "The date the vulnerability was first discovered in the wild."),
            ("Vulnerability Aliases", "A list of any known vulnerability aliases, seperated by `\n`."),
            ("Vulnerability Categories", "A list of categories that fit vulnerability, seperated by `\n`"),
            ("Vulnerability References", "Any vulnerability references seperated by `\n`"),
            ("Vulnerability Source", "Registry source where the vulnerability is created."),
            ("Vulnerability URL", "URL of the security advisory, if any exists."),
            ("Vulnerability Withdrawn", "Whether or not the vulnerability has been withdrawn"),
            ("Patched Versions", "A list of patched versions for the component, if any exist."),
            ("Unaffected Versions", "A list of known unaffected versions, if any exist."),
    ]

def get_cargo_affected_vulnerabilities_col_descriptions() -> list[Tuple[str, str]]:
    """
    Return a list of tuples, each containing the name of the columns that correspond
    to the `affected` section of the generated report, alongside their des
    
    :return: Description
    :rtype: list[Tuple[str, str]]
    """
    return [
        ("Affected Architecture", "A list of any known affected architectures, delimited by `\n`."),
        ("Affected OS(es)", "A list of any known affected OSes, delimited by `\n`."),
        ("Affected Functions", "A list of any known affected functions, delimited by `\n`."),
    ]
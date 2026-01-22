from openpyxl import Workbook, load_workbook
from pathlib import Path
from typing import Any
from typing import Tuple

def _open_or_create_workbook(filepath: str) -> Workbook:
    """
    Checks if a workbook is already available or creates one based the provided
    `filepath`. The method `save(filepath)` still needs to be used on the returned
    object to save it to the disk.
    
    :param filepath: The filepath of the workbook to create or open.
    :type filepath: str
    :return: Either the newly created Workbook object or the opened Workbook object.
    :rtype: Workbook
    """
    path = Path(filepath)

    if path.exists():
        return load_workbook(path)
    else:
        return Workbook()

def _write_col_descriptors(wb: Workbook) -> None:
    pass

def write_to_workbook(cargo_results: dict[str, Any], 
        filepath: str, 
        col_descs: list[Tuple[str, str]] | None = None) -> None:
    """
    Write the cargo results to a XLSX file. The method optionally writes the
    column descriptors to the file in a new tab.
    
    :param cargo_results: Description
    :type cargo_results: dict[str, Any]
    :param filepath: Description
    :type filepath: str
    :param write_col_descs: Description
    :type write_col_descs: bool
    """
    activeWb = _open_or_create_workbook(filepath)

    if col_descs:




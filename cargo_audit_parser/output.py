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

def _write_col_descriptors(wb: Workbook, descriptors: list[Tuple[str, str]]) -> None:
    """
    Write column descriptors in the provided `wb` object, in a sheet named `Cargo Column Descriptors`.
    If the sheet already exists, delete its contents first.
    
    :param wb: The `Workbook` object to write to.
    :type wb: Workbook
    :param descriptors: The list of column descriptors to write.
    :type descriptors: list[Tuple[str, str]]
    """
    def __write_to_sheet__(ws):        
        for index in range(0, len(descriptors)):
            titleLoc = f"A{index+1}"
            descLoc = f"B{index+1}"

            ws[titleLoc] = descriptors[index][0]
            ws[descLoc] = descriptors[index][1]

    sheetTitle = "Cargo Column Descriptors"
    if sheetTitle in wb.sheetnames:
        ws = wb[sheetTitle]

        # delete existing contents
        for row in ws.rows:
            for cell in row:
                cell.value = None
        __write_to_sheet__(ws)

    else:
        ws = wb.create_sheet(title = "Cargo Column Descriptors")
        __write_to_sheet__(ws)

def _workbook_cleanup_(wb: Workbook):
    """
    Remove the default sheet in the workbook named `Sheet`, if exists.
    
    :param wb: The `Workbook` object to manipulate.
    :type wb: Workbook
    """
    if "Sheet" in wb.sheetnames:
        del wb["Sheet"]
    

def write_to_workbook(cargo_results: dict[str, Any], 
        filepath: str, 
        column_descriptors: list[Tuple[str, str]] | None = None) -> None:
    """
    Write the cargo results to a XLSX file. The method optionally writes the
    column descriptors to the file in a new tab.
    
    :param cargo_results: The processed results obtained from `cargo-audit`.
    :type cargo_results: dict[str, Any]
    :param filepath: The filepath of the file to write to.
    :type filepath: str
    :param column_descriptors: The column descriptors to write in a sheet named
    `Cargo Column Descriptors`. If the exists it is erased first.
    :type column_descriptors: list[Tuple[str, str]] | None
    """
    activeWb = _open_or_create_workbook(filepath)

    if column_descriptors:
        _write_col_descriptors(activeWb, column_descriptors)

    # TODO: Write cargo results
    # TODO: Remove default sheet named "Sheet"
    # TODO: Resize columns to fit cell contents.
    # TODO: Style based on findings and scan date.

    _workbook_cleanup_(activeWb)
    activeWb.save(filepath)



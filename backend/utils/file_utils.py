import os

def validate_excel_file(filename: str) -> bool:
    return filename.endswith((".xls", ".xlsx"))

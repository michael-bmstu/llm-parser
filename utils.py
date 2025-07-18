from tabula import read_pdf
import os

def extract_tabels(file_path: str) -> str:
    """
    Extract tables from .pdf file and convert them to string
    """
    tables = read_pdf(file_path, pages="all")
    os.system('clear')
    for i, t in enumerate(tables):
        tables[i] = t.dropna(how='all').dropna(axis=1, how='all')
    print("Reading done")
    tables_txt = ""
    for t in tables:
        if t.empty:
            continue
        tables_txt += t.to_string(index=False, header=False, na_rep="",)
    print(len(tables_txt), len(tables_txt.split()))
    return tables_txt
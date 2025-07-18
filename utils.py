from tabula import read_pdf

def extract_tabels(file_path: str) -> str:
    """
    Extract tables from .pdf file and convert them to string
    """
    tables = read_pdf(file_path, pages="all")
    for i, t in enumerate(tables):
        tables[i] = t.dropna(how='all').dropna(axis=1, how='all')

    tables_txt = ""
    for t in tables:
        if t.empty:
            continue
        tables_txt += t.to_string(index=False, header=False, na_rep="",)
    return tables_txt
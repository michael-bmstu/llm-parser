from tabula import read_pdf
import os
from langchain_mistralai import ChatMistralAI
from models import IFRS


def extract_tabels(file) -> str:
    """
    Extract tables from .pdf file and convert them to string
    """
    tables = read_pdf(file, pages="all")
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

def create_model(params: dict[str, str]) -> ChatMistralAI:
    llm = ChatMistralAI(
        model="mistral-medium-latest",
        temperature=0.1,
        api_key=params["api_key"],
    )
    return llm.with_structured_output(IFRS)

def process_txt(tables_txt: str, llm_parser: ChatMistralAI) -> dict[str, float]:
    messages = [
    ("system", "You are an experienced financial analyst, process the IFRS reports"),
    ("human", tables_txt)
    ]
    answer = llm_parser.invoke(messages)
    return answer.model_dump()

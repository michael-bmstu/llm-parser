from tabula import read_pdf
from langchain_mistralai import ChatMistralAI
try:    # for running interface.py
    from app.model import IFRS
    from logger import setup_logger
except: # for running main.py
    from .model import IFRS
    from .logger import setup_logger

logger = setup_logger()

def extract_tabels(file) -> str:
    """Extracts tables from a PDF file and converts them to a string.

    This function reads all pages of the specified PDF file, processes the tables by removing 
    empty rows and columns, and concatenates the non-empty tables into a single string.

    Args:
        file: The path to the PDF file or a file-like object from which to extract tables.

    Returns:
        str: A string representation of the extracted tables, with each table's content 
             concatenated and formatted without indices or headers.
    """
    logger.info("Starting to extract tables from the PDF file.")
    tables = read_pdf(file, pages="all")
    logger.debug(f"Number of tables read from PDF: {len(tables)}")
    for i, t in enumerate(tables):
        tables[i] = t.dropna(how='all').dropna(axis=1, how='all')

    logger.info("Reading done. Processing tables to string.")
    tables_txt = ""
    for t in tables:
        if t.empty:
            continue
        tables_txt += t.to_string(index=False, header=False, na_rep="",)
    logger.info(f"Extracted text length: {len(tables_txt)}, Word count: {len(tables_txt.split())}")
    return tables_txt

def create_model(params: dict[str, str]) -> ChatMistralAI:
    """Creates and configures a ChatMistralAI model instance.

    Args:
        params (dict[str, str]): A dictionary containing parameters for model configuration.
            Expected keys:
                - 'api_key': The API key for authenticating with the ChatMistralAI service.

    Returns:
        ChatMistralAI: An instance of the ChatMistralAI model configured with the specified parameters.
    """
    llm = ChatMistralAI(
        model="mistral-medium-latest",
        temperature=0.1,
        api_key=params["api_key"],
    )
    return llm.with_structured_output(IFRS)

def process_txt(tables_txt: str, llm_parser: ChatMistralAI) -> dict[str, float]:
    """Processes IFRS reports using a ChatMistralAI model.

    Args:
        tables_txt (str): A string containing the text of the IFRS reports to be processed.
        llm_parser (ChatMistralAI): An instance of the ChatMistralAI model used for parsing the reports.

    Returns:
        dict[str, float]: A dictionary containing the processed results, where keys are result identifiers 
                          and values are the corresponding numerical outputs.
    """
    messages = [
    ("system", "You are an experienced financial analyst, process the IFRS reports"),
    ("human", tables_txt)
    ]
    answer = llm_parser.invoke(messages)
    return answer.model_dump()

from langchain_mistralai import ChatMistralAI
from models import IFRS
from config import mistral_params
import os
import utils

DATA = "data"

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.1,
    api_key=mistral_params["api_key"],
)
prepared_llm = llm.with_structured_output(IFRS)

# files = os.listdir(DATA)

parsed_tabels_txt = utils.extract_tabels(os.path.join(DATA, "mts-2024.pdf"))
messages = [
    ("system", "You are an experienced financial analyst, process the IFRS reports"),
    ("human", parsed_tabels_txt)
]
answer = prepared_llm.invoke(messages)
print(answer)
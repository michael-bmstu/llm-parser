from langchain_mistralai import ChatMistralAI
from models import IFRS
from config import mistral_params
import os
import utils

DATA = "data"

llm = ChatMistralAI(
    model="mistral-medium-latest",
    temperature=0.1,
    api_key=mistral_params["api_key"],
)
prepared_llm = llm.with_structured_output(IFRS)

# files = os.listdir(DATA)
fn = "mts-2024.pdf"
parsed_tabels_txt = utils.extract_tabels(os.path.join(DATA, fn))
messages = [
    ("system", "You are an experienced financial analyst, process the IFRS reports"),
    ("human", parsed_tabels_txt)
]
print("LLM request")
answer = prepared_llm.invoke(messages)
print("Answer:")
print(answer)
with open(f"{DATA}/{fn.split(".")[0]}.json", "w", encoding="utf-8") as f:
    f.write(answer.model_dump_json())
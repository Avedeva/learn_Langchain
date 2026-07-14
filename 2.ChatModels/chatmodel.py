from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model="tencent/hy3:free",
    base_url= "https://openrouter.ai/api/v1",
    api_key= api_key)



result = llm.invoke("What is the capital of India? less than 20 words")
print(result.content)

# can use open router as open ai compatable in langchain

print("-------------------------")

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task='text-generation',
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("india capital is what ?")
print(result.content)

# here is used the hugging face
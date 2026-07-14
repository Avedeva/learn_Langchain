from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(model='your_model_here')

result  = llm.invoke("what is the capital of all the top 10 biggest countries")

print(result)

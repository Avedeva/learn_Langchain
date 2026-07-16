from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=0.8,
    base_url="https://openrouter.ai/api/v1"

)

prompt1 = PromptTemplate(
    template="Tell mejoke about {topic}",
    input_variables=['topic'])

prompt2 = PromptTemplate(
    template = "explan me this {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result = chain.invoke({"topic":"cricket"})

print(result)
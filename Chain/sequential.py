from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=0,
    base_url="https://openrouter.ai/api/v1"

)

temp_1 = PromptTemplate(
    template="short report about {topic}",
    input_variables=['topic']
)

temp_2 = PromptTemplate(
    template="""
        Give me 5 facts about
    {report}
    """,
    input_variables=['report']
)

parser = StrOutputParser()
chain = temp_1|model|parser|temp_2|model|parser

result = chain.invoke({'topic':'importance of sleep'})

print(result,"\n------------------------------------------------------")

chain.get_graph().print_ascii()

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

template = PromptTemplate(
    template="""

        Genereate 5 facts about {topic}
    """,
    input_variables=['topic']
)

parser = StrOutputParser()


chain = template|model|parser

result = chain.invoke({'topic':'Football'})

print(result)
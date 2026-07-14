from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=1.3,
    base_url="https://openrouter.ai/api/v1"

)


class Character(BaseModel):
    name: str
    age : int
    race : str
    height: int
    ability : str

parser = JsonOutputParser(pydantic_object=Character )


template_1 = PromptTemplate(
        template="""
Give the name, age, ability, race, and height of a fictional character.{format_instructions}
""",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = template_1|model|parser

result = chain.invoke({})
print(result)




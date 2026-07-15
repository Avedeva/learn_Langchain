from langchain_openai import ChatOpenAI
from typing import Literal
from pydantic import BaseModel,Field
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from dotenv import load_dotenv
import os

load_dotenv()
api_key_1 = os.getenv("OPENROUTER_API_KEY")


model= ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key_1,
    temperature=0,
    base_url="https://openrouter.ai/api/v1"

)

class Sentiment(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="Either return Poistve or negative based on sentiment")

parser = PydanticOutputParser(pydantic_object=Sentiment)
parser_2 = StrOutputParser()

prompt_1 = PromptTemplate(
    template = """Classify the sentiment as negitive or positive based on the \n {feedback} \n {format_instructions}  """,
    input_variables = ['feedback'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

prompt_2 = PromptTemplate(
    template = 'give resonable reply according to the positive feedback {sentiment}',
    input_variables=['sentiment']
)

prompt_3 = PromptTemplate(
    template = 'give resonable reply according to the negative feedback {sentiment}',
    input_variables=['sentiment']
)


branch = RunnableBranch(
    (lambda x : x.sentiment =='positive', prompt_2|model|parser_2),
    (lambda x: x.sentiment =='negative', prompt_3|model|parser_2),

    RunnableLambda(lambda x:"no sentient")
)

classifier_chain = prompt_1|model|parser


chain = classifier_chain|branch

result = chain.invoke({'feedback':'The fuck is this product hell naah'})

print(result)
print("\n-------------------------------------\n")

chain.get_graph().print_ascii()
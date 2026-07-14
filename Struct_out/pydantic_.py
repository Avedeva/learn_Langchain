#  structured output with pydantic

from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from typing import Literal,Optional
from pydantic import BaseModel,Field

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=1.5,
    base_url="https://openrouter.ai/api/v1"

)
class Review(BaseModel):
    Rating : str = Field(description="Rating of the in the review")
    Semantic : Literal["pos","neg"] = Field(description="what was them semantic feeling for the review positive or negative")
    summary : str = Field(description="summary of the review")
    worth : Optional[str] = Field(default=None,description="is the review worth the consideration")



struct_model = model.with_structured_output(Review)

result = struct_model.invoke(""" **The Devil's Advocate (1997) – Short Review**

*The Devil's Advocate* is a gripping psychological thriller that blends legal drama with supernatural horror. Led by compelling performances from Keanu Reeves, Al Pacino, and Charlize Theron, the film explores themes of ambition, greed, temptation, and the moral compromises people make in pursuit of success.

Al Pacino steals every scene with his charismatic yet unsettling portrayal of John Milton, delivering a performance that is both captivating and terrifying. While the film's pacing slows in parts and its nearly two-and-a-half-hour runtime feels slightly stretched, its thought-provoking themes and memorable climax make it highly engaging.

Overall, *The Devil's Advocate* is a stylish, intelligent thriller that raises timeless questions about free will, power, and the price of ambition.

**Rating: 8.5/10**""")


print(result)
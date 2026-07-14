#(structured output with typed dict)
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=1.5,
    base_url="https://openrouter.ai/api/v1"

)

class Review(TypedDict):
    Rating : Annotated[int,"Rating of the in the review"]
    Semantic : Annotated[str,"what was the semantic feeling of the review positive or negative or neutral"]
    worth : (Annotated[Optional[str],"worth the watch or not"])
    summary : Annotated[str,"summary of the review"]



struct_model = model.with_structured_output(Review)

result = struct_model.invoke("""**The Devil's Advocate (1997) – Short Review**

*The Devil's Advocate* is a gripping psychological thriller that blends legal drama with supernatural horror. Led by compelling performances from Keanu Reeves, Al Pacino, and Charlize Theron, the film explores themes of ambition, greed, temptation, and the moral compromises people make in pursuit of success.

Al Pacino steals every scene with his charismatic yet unsettling portrayal of John Milton, delivering a performance that is both captivating and terrifying. While the film's pacing slows in parts and its nearly two-and-a-half-hour runtime feels slightly stretched, its thought-provoking themes and memorable climax make it highly engaging.

Overall, *The Devil's Advocate* is a stylish, intelligent thriller that raises timeless questions about free will, power, and the price of ambition.

**Rating: 8.5/10**
""")


print(result)


# mmine doesn't woek as i have open source but will work in open ai or gemini big closed model's

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def generate_summary(transcript: str) -> str:
    """
    Summarise meeting transcript and extract decisions + action items.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
Summarise the meeting transcript in 5‑7 bullet points.
Then list:
1. **Decisions Made** (bullet list)
2. **Action Items** (task • owner • due date if mentioned)

Transcript:
{text}
"""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"text": transcript})

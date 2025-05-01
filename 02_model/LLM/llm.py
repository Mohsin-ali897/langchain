
import langchain # type: ignore 
import os # type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv # type: ignore
load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash',api_key=gemini_api_key)
result =llm.invoke('Hello, how are you?')
print(result.content)

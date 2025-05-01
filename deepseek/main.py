
# from langchain_deepseek import ChatDeepSeek # type: ignore
# import os # type: ignore
# from dotenv import load_dotenv # type: ignore
# load_dotenv()
# api_key = os.getenv('DEEPSEEK_API_KEY')
# llm = ChatDeepSeek(
#     model="deepseek-chat",  # or "deepseek-reasoner"
#     temperature=0.5,
#     deepseek_api_key=api_key
#     # max_tokens=None,
#     # timeout=None,
#     # max_retries=2,
#     # other parameters...
# )
# result =llm.invoke('Hello, how are you?')
# print(result.content)



# # llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',api_key=os.getenv('AIzaSyARpQZTA9o416bEj8Qzxsq0EJ_nZevf8ug'))
# # result =llm.invoke('Hello, how are you?')
# # print(result)

from langchain_deepseek import ChatDeepSeek  # type: ignore
import os  # type: ignore
from dotenv import load_dotenv  # type: ignore

# Load environment variables
load_dotenv()

# Get API key from .env file
api_key = os.getenv('DEEPSEEK_API_KEY')

# Use `openai_api_key` instead of `deepseek_api_key`
llm = ChatDeepSeek(
    model="deepseek-chat",  # or "deepseek-reasoner"
    temperature=0.5,
    openai_api_key=api_key  # Corrected parameter
)

# Invoke the model
result = llm.invoke('Hello, how are you?')
print(result.content)

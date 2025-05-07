import chainlit as cl # type: ignore
import os
from agents import Agent, Runner, AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel # type:ignore
from dotenv import load_dotenv, find_dotenv # type: ignore
from openai.types.responses import ResponseTextDeltaEvent # type: ignore

#? step 1: load the environment variables 

load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")


#? step 2: setting up the external client  
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

#? step 3: setting up the Chat Completions Model

model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash', 
    openai_client = provider,
)

#? step 4: setting up the configuration for the agent 

run_config = RunConfig(
    model = model,
    model_provider = provider,
    tracing_disabled = True,
)


#? step 5: setting up the agent

agent:Agent = Agent(
    name='Assistant',
    instructions='A helpful assistant',
    model = model,
)
# Result = Runner.run_sync(agent, 'what is the capital of France?', run_config=run_config)
# print(Result.final_output)


#? step 6: setting up the chainlit conservertion history 
@cl.on_chat_start
async def start():
    """
    This function is called when the chat starts.
    """
    cl.user_session.set('History', [])
    await cl.Message(
        content="Hello! I am your assistant. How can I help you today?"
    ).send()


#? step 7: setting up the chainlit message handler 
@cl.on_message
async def handle_message(message: cl.Message):
    """
    Handle the message from the user.
    """
    History = cl.user_session.get('History')
    
    History.append({'role':'user', 'content':message.content})
    
    Result = Runner.run_streamed(agent,
                                History, 
                                run_config=run_config
                                )
    msg = cl.Message(content="")
    await msg.send()
    async for event in Result.stream_events():
        if event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
            token = event.data.delta
            
            await msg.stream_token(token)
            
    # await cl.Message(content=Result.final_output).send()
    History.append({'role':'assistant', 'content':Result.final_output})
    cl.user_session.set('History', History)



    

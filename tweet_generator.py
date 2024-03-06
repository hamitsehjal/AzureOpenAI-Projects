''' Azure OpenAI Project - Tweet Generator '''

import os
from typing import List
from openai import AzureOpenAI
from dotenv import load_dotenv
# load environmental variables
load_dotenv()
# Configure AzureOpenAI Client
client=AzureOpenAI(
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
api_key = os.getenv("AZURE_OPENAI_API_KEY"),
api_version = os.getenv("AZURE_API_VERSION"),
)

def ask_gpt(my_client,messages):
    '''make request to OpenAI GPT model using client and messages'''
    response=my_client.chat.completions.create(model="gpt-35",messages=messages)
    return response.choices[0].message.content

SYSTEM_PROMPT="You are a tweet generator. \
Your task is to generate tweets, based on the TOPICS and HASTAGS that are given to you. \
You should respect the instructions: the TONE, the LENGTH, and the STYLE"

def generate_tweet(
        topics: str, 
        hastags: str, 
        tone: str='Casual', 
        style: str='informal',
        length_characters: int=240, 
        ):
    '''Generate tweet based on the parameters'''
    
    # topics=",".join(topics)
    # hastags=",".join(['#' + tag for tag in hastags])
    user_prompt=f"\
        TOPICS: {topics} \
        HASTAGS: {hastags} \
        TONE: {tone} \
        LENGTH: {length_characters} characters \
        STYLE: {style}"
    
    return ask_gpt(client,[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":user_prompt}])
    
     

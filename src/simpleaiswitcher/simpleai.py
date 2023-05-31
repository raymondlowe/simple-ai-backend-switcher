
from enum import Enum

# pip3 install poe-api
import poe

# pip install openai
import openai
# openai.organization = "YOUR_ORG_ID"
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.Model.list()

#pip install llama-cpp-python
# https://github.com/abetlen/llama-cpp-python
from llama_cpp import Llama
# >>> llm = Llama(model_path="./models/7B/ggml-model.bin")
# >>> output = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
# >>> print(output)


class AIBackEndType(Enum):
    OpenAI = 1
    Poe = 2
    LLAMACPP = 3

 

class SimpleAI:
    """
    A class for creating an AI agent that uses a specified backend and access token.

    Attributes:
    -----------
    backEnd : AIBackEndType
        The backend that the agent will use for natural language processing.
    AccessToken : str
        The access token required to authenticate requests to the backend.

        For OpenAIGPT34 the token will be the OpenAI API key
        For PoeGPT35 it will be the cookie
        for LLAMACPP it will be ignored
    model : str
        a string that indicates which model to use from the backend provoiders, 
        such as "chatgpt3.5", "capybara" or "./wizardvicuna.bin"


    """

    def __init__(self, backEnd: AIBackEndType, AccessToken: str, model: str = ''):
        self.backEnd = backEnd
        self.AccessToken = AccessToken
        if self.backEnd == AIBackEndType.OpenAI:
            openai.api_key = self.AccessToken
        if self.backEnd == AIBackEndType.Poe:
            # create poe object
            self.poeclient = poe.Client(AccessToken)
            pass
        if self.backEnd == AIBackEndType.LLAMACPP:
            # create the llama
            pass
        if not model:
            if self.backEnd == AIBackEndType.OpenAI:
                self.model = 'gpt-3.5-turbo'
            elif self.backEnd == AIBackEndType.Poe:
                self.model = 'capybara'
            elif self.backEnd == AIBackEndType.LLAMACPP:
                self.model = 'default.bin'
                
        else:
            self.model = model

    def reply(self, message, clear_conversation: bool = False):
        if self.backEnd == AIBackEndType.OpenAI:
            response = openai.ChatCompletion.create(model=self.model, 
                                                    messages=[{"role": "user", 
                                                                "content": message}])
            return response['choices'][0]['message']['content']

        if self.backEnd == AIBackEndType.Poe:
            for chunk in self.poeclient.send_message(self.model, message, clear_conversation, timeout = 20):
                pass
            response = chunk['text']

            return response
        
        if self.backEnd == AIBackEndType.LLAMACPP:
            pass
        

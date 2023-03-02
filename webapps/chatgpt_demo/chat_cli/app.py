from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path = './.env'

def request(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.6,
    )
    return response

class ChatBot:
    def __init__(self):
        self.chat_history = [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
        ]

    def chat_request(self, text):
        self.chat_history.append({"role": "user", "content": text})
        # https://platform.openai.com/docs/guides/chat/introduction
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.chat_history
        )
        resp = resp.choices[0].message.content
        self.chat_history.append({"role": "system", "content": resp})
        return resp

while True:
    bot = ChatBot()
    user_input = prompt(
        '> ',
        history=FileHistory('history.txt'),
        auto_suggest=AutoSuggestFromHistory())
    # print(user_input)
    response = bot.chat_request(user_input)
    print(response)
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from scrape import searchKeyword

class SearchBot:
    def __init__(self):
        pass

    def chat_request(self, text):
        if text.startswith("/"):
            return self.special_commands(text)
        return ""

    def special_commands(self, text):
        if text.startswith("/search"):
            return self.search_fn(text)

    def search_fn(self, text):
        query = text.removeprefix("/search ")
        results = searchKeyword(query)
        content = "\n".join([str(r) for r in results])
        filename = query.lower().replace(" ", "_")
        self.write_to_file(filename, content)
        return content

    def write_to_file(self, filename, content):
        outputFile = open(filename + ".txt", "w")
        outputFile.write(content)
        outputFile.close()
    

while True:
    bot = SearchBot()
    user_input = prompt(
        '> ',
        history=FileHistory('history.txt'),
        auto_suggest=AutoSuggestFromHistory())
    response = bot.chat_request(user_input)
    print(response)
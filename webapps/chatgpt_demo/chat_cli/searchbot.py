from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from scrape import searchKeyword, scrapeLinks, TechBlogScraper
import os

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
        if text.startswith("/scrape"):
            return self.scrape_links_fn(text)

    def scrape_links_fn(self, text):
        text = text.removeprefix("/scrape ")
        res = []
        if "marktechpost" in text:
            scraper = TechBlogScraper.MarkTechPost()
            res, ans = scraper.scrapeLinks()
            # Write full content
            content = "\n".join([str(r) for r in ans])
            self.write_to_file("blogs", text, content)
        else:
            scrapeLinks(text)
        return res

    def search_fn(self, text):
        query = text.removeprefix("/search ")
        results = searchKeyword(query)
        content = "\n".join([str(r) for r in results])
        self.write_to_file("search_results", query, content)
        return content

    def write_to_file(self, outputdir, filename, content):
        # Lowercase and underscore filename
        filename = filename.lower().replace(" ", "_")
        if not os.path.exists(outputdir):
            # print("Creating output directory..")
            os.makedirs(outputdir)
        outputFile = open(outputdir + "/" + filename + ".txt", "w")
        outputFile.write(content)
        outputFile.close()
    

while True:
    bot = SearchBot()
    user_input = prompt(
        '> ',
        history=FileHistory('history.hidden.txt'),
        auto_suggest=AutoSuggestFromHistory())
    response = bot.chat_request(user_input)
    print(response)
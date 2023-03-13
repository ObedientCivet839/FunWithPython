from trafilatura import fetch_url, extract
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.yahoo import Search as YahooSearch

def searchKeyword(query):
    # https://pypi.org/project/search-engine-parser/
    engine = GoogleSearch()
    search_args = (query, 1)
    results = engine.search(*search_args)
    ans = []
    for d in results:
        ans.append(Result(d['descriptions'], d['links'], d['titles']))
    return ans

class Result:
    def __init__(self, descriptions, links, titles):
        self._desc = descriptions
        self._ln = links
        self._tl = titles
        self._ft = self.getFullText(links)
    
    def __str__(self):
        res = "Title: " + self._tl + "\n"
        res += "Link: " + self._ln + "\n"
        res += "Description: " + self._desc + "\n"
        if self._ft:
            res += "Full text:\n"
            res += self._ft + "\n\n"
        return res

    def getFullText(self, url):
        # https://trafilatura.readthedocs.io/en/latest/usage-python.html
        downloaded = fetch_url(url)
        result = extract(downloaded, include_comments=False, include_tables=False, include_links=False)
        return result

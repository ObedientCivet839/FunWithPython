from trafilatura import fetch_url, extract

from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.yahoo import Search as YahooSearch

def searchByEngine(engine, search_args):
    results = engine.search(*search_args)
    ans = []
    for r in results:
        ans.append(convertResult(r))
    return ans

def query(engine, search_args):
    searchEngine = factory(engine)
    return searchByEngine(searchEngine, search_args)

def convertResult(d):
    return Result(d['descriptions'], d['links'], d['titles'])

def getFullText(url):
    # https://trafilatura.readthedocs.io/en/latest/usage-python.html
    downloaded = fetch_url(url)
    result = extract(downloaded, include_comments=False, include_tables=False, include_links=False)
    return result

class Result:
    def __init__(self, descriptions, links, titles):
        self._desc = descriptions
        self._ln = links
        self._tl = titles
        self._ft = getFullText(links)
    
    def __str__(self):
        res = self._tl + "\n"
        res += self._ln + "\n"
        res += self._desc + "\n"
        if self._ft:
            res += self._ft + "\n\n\n"
        return res

def factory(engine):
    if engine == "G":
        search = GoogleSearch()
    elif engine == "Y":
        search = YahooSearch()
    elif engine == "B":
        search = BingSearch()
    return search

def displaySearch(engine, args, file):
    answers = query(engine, args)
    cnt= f"-------------{engine}------------\n"
    for a in answers:
        cnt += f"{a}" + "\n"
    cnt += "\n\n"
    print(cnt)
    file.write(cnt)
    return cnt

if __name__ == '__main__':
    topic = 'audiolm'
    outputFile = open(topic + ".txt", "w")

    args = (topic, 1)
    displaySearch("G", args, outputFile)
    displaySearch("Y", args, outputFile)
    displaySearch("B", args, outputFile)

    outputFile.close()
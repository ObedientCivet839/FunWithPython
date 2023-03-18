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
    # BUG(P3): Treat wikipedia as a separate source and remove footnotes (e.g. [1],[2])
    for d in results:
        ans.append(Result(d['descriptions'], d['links'], d['titles']))
    return ans

class Result:
    def __init__(self, descriptions, link, titles):
        self._desc = descriptions
        self._ln = link
        self._tl = titles
        self._ft = self.getFullText(link)
    
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

 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

def scrapeLinks(url):
    # https://pythonprogramminglanguage.com/get-links-from-webpage/
    req = Request(url)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        href = link.get('href')
        if href:
            links.append(str(href))
    return links

class TechBlogScraper:
    def __init__(self, url, linkRE, extraFilter=None) -> None:
        self._url = url
        self._linkRE = linkRE # only take links that match this regex
        self._extraFilter = extraFilter
    
    @classmethod
    def MarkTechPost(cls):
        def extra_filter(links):
            # Remove duplicate links
            links = map(lambda x: x.removesuffix("#respond"), links)
            links = list(set(links))
            return sorted(links)
        return TechBlogScraper(
            url="https://www.marktechpost.com/", 
            linkRE=r'https://www.marktechpost.com/\d+/\d+/\d+/.*',
            extraFilter=extra_filter)
    
    def scrapeLinks(self):
        res = scrapeLinks(self._url)
        filter_fn = lambda x: re.search(self._linkRE, x)
        res = list(filter(filter_fn, res))
        if self._extraFilter:
            res = self._extraFilter(res)
        ans = []
        for url in res:
            ans.append(Result("", url, url))
        return res, ans


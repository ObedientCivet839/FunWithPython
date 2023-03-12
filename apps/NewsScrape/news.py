from uplink import Consumer, get, Path, Query
import os
API_KEY = "d70cd97a986d4369b39cc7be2f0a597a"
BASE_URL = "https://newsapi.org/v2/"
# everything?q={query}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}"


def getNews():
    import requests
    api_url = BASE_URL.format(
        query='Apple', from_date='2023-01-03', to_date='2023-01-04', api_key=API_KEY)
    response = requests.get(api_url)
    print(response.json())

# ENDPOINT="everything""top-headlines"

class NewsClient(Consumer):

    @get("everything")
    def get_news(
        self,
        api_key: Query("apiKey"),
        sort_by: Query("sortBy"),
        language: Query("language"),
        from_date: Query("from"),
        to_date: Query("to"),
        query: Query("q"),
        page_size: Query("pageSize"),
        page: Query("page"),
        # sources: Query("sources"),
    ):
        """Fetches the data for everything"""
        pass

    @get("everything")
    def get_news_from_source(
        self,
        api_key: Query("apiKey"),
        sort_by: Query("sortBy"),
        language: Query("language"),
        page_size: Query("pageSize"),
        page: Query("page"),
        sources: Query("sources"),
    ):
        """Fetches the data for everything"""
        pass

    @get("top-headlines/sources")
    def get_sources(
        self,
        api_key: Query("apiKey"),
        language: Query("language"),
    ):
        """Fetches sources"""
        pass

c = NewsClient(base_url=BASE_URL)

def printArticle(artl):
    print("="*os.get_terminal_size().columns)
    print(artl['title'])
    print(artl['url'])
    print("From:", artl['source']['name'])
    print("Posted: ", artl["publishedAt"])
    print(artl["content"])

# Sort By options
# relevancy, popularity, publishedAt.
# relevancy = articles more closely related to q come first.
# popularity = articles from popular sources and publishers come first.
# publishedAt

# domains
# A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com)

# cnn
# cbs-news
# abc-news
# business-insider
# bloomberg
# bleacher-report
# engadget
# entertainment-weekly
# espn
# fortune
# hacker-news
# newsweek
# reddit-r-all
# talksport
# techcrunch
# the-verge
# the-wall-street-journal
# the-washington-post
# time
# usa-today
# vice-news
# wired

def getSources():
    response = c.get_sources(
        api_key=API_KEY,
        language="en",
    )
    for a in response.json()['sources']:
        print(a['id'])

# getSources()


def top10DailyNews(query):
    response = c.get_news(
        api_key=API_KEY,
        sort_by="popularity",
        language="en",
        query=query,
        from_date='2023-01-03',
        to_date='2023-01-04',
        page_size='10',
        page='1')

    for a in response.json()['articles']:
        printArticle(a)

# top10DailyNews('Sports')

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def getFullText(url):
    # url = 'http://web.mta.info/developers/turnstile.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # html = requests.get(url).text
    # print(html)
    # soup = soup.find("div", {"id": "content"})
    text = soup.find_all(text=True)
    # print(text)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'footer',
        'image',
        'meta',
        'head', 
        'input',
        'script',
        'style',
        'button',
        # there may be more elements you don't want, such as "style", etc.
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    print(output)


def topFromSource(s):
    response = c.get_news_from_source(
        api_key=API_KEY,
        # sort_by="popularity",
        sort_by="publishedAt",
        sources=s,
        language="en",
        page_size='10',
        page='1')

    for a in response.json()['articles']:
        printArticle(a)
        getFullText(a['url'])



# topFromSource('the-wall-street-journal')
# topFromSource('the-verge')
# topFromSource('fortune')
topFromSource('hacker-news')
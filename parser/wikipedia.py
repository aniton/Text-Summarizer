import requests
from parser import wikipedia_fetcher as wf
from bs4 import BeautifulSoup

S = requests.Session()


def wiki_parser(title):
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": title,
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    try:
        html = DATA["parse"]["text"]["*"]
        text = BeautifulSoup(html, features="html.parser").get_text()

        return text

    except:
        return "Nan"

#
# def wiki_url(url):
#
#     PARAMS = {
#         "action": "parse",
#         "page": url,
#         "format": "json"
#     }
#
#     R = S.get(url=url, params=PARAMS)
#     DATA = R.json()
#     html = DATA["parse"]["text"]["*"]
#     text = BeautifulSoup(html).get_text()
#     return text





import requests
from bs4 import BeautifulSoup
from digger.models.Book import Book

def requestAndParse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    page = requests.get(url,headers=headers)
    html = BeautifulSoup(page.text, 'html.parser')
    return html

def cleanPrice(string: str):
    s = string.replace('R$','')
    s = s.replace(' ','')
    s = s.replace('\n','')
    s = s.replace('\xa0','')
    s = s.replace('Por:','')
    return s

checkIfNone = lambda x: type(x) != type(None)
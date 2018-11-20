import requests
from bs4 import BeautifulSoup
from digger.models.Book import Book
from babel.numbers import parse_decimal
import unicodedata
import re

def requestAndParse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    page = requests.get(url,headers=headers)
    html = BeautifulSoup(page.text, 'html.parser')
    return html

def containsName(other, string):
    s1 = re.sub('^[a-zA-Z0-9_]+$', '', other)
    s2 = re.sub('^[a-zA-Z0-9_]+$', '', string)
    s1 = toAscii(s1)
    s2 = toAscii(s2)
    print(s1)
    print(s1)
    s1 = s1.lower()
    s2 = s2.lower()
    return s1 in s2

toAscii = lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore')


def cleanPrice(string: str):
    s = string.replace('R$','')
    s = s.replace(' ','')
    s = s.replace('\n','')
    s = s.replace('\xa0','')
    s = s.replace(':','')
    s = s.replace('Por','')
    s = s.replace('por','')
    return s

def priceFloat(string: str):
    p = cleanPrice(string)
    try:
        p = float(parse_decimal(p,locale='pt_BR'))
    except :
        p = None
    return p

checkIfNone = lambda x: type(x) != type(None)
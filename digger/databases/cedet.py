from bs4 import BeautifulSoup
from digger.databases import helpers
from digger.models.Book import Book

def ecclesiae(bookName):
    url = "https://ecclesiae.com.br/index.php?route=product/search&search=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapper, html.select('div.product')))
    return books

def deiaetiba(bookName):
    url = "https://livraria.deiaetiba.com.br/index.php?route=product/search&search=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapper, html.select('div.product')))
    return books

def bernardo(bookName):
    url = "https://livrariadobernardo.com/index.php?route=product/search&search=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapper, html.select('div.product')))
    return books

def seminarioFilosofia(bookName):
    url = "https://livraria.seminariodefilosofia.org/index.php?route=product/search&search=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapper, html.select('div.product')))
    return books

def nandoMoura(bookName):
    url = "https://https://livraria.nandomoura.com/index.php?route=product/search&search=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapper, html.select('div.product')))
    return books

def mapper(product):
    return Book(
        image=product.find('img')['src'],
        price= product.findAll('span')[1].text,
        url=product.find('a')['href']
    )
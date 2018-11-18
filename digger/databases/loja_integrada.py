from bs4 import BeautifulSoup
from digger.databases import helpers
from digger.models.Book import Book

def centroDomBosco(bookName):
    url = "https://loja.centrodombosco.org/buscar?q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapper, html.select('div.listagem-item')))
    return books

def saoTomas(bookName):
    url = "https://santotomas.lojaintegrada.com.br/buscar?q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapper, html.select('div.listagem-item')))
    return books

def mapper(product):
    return Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('strong.preco-promocional').text),
            url=product.find('a')['href']
        )
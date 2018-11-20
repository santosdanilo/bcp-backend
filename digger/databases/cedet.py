from bs4 import BeautifulSoup
from digger.databases import helpers
from digger.models.Book import Book
from digger.models.Store import manyStores

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
    print(html.select('div.product'))
    return books

def seminarioFilosofia(bookName):
    url = "https://livraria.seminariodefilosofia.org/index.php?route=product/search&search=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapper, html.select('div.product-list div')))
    return books

def mapper(product):
    check_price = product.find('span',{'class': 'price-new'})
    if helpers.checkIfNone(check_price):
        price = check_price.text
    else:
        price = product.select_one('div.price').text
        
    print(product.select_one('div.name a').text + " " + price) 
    return Book(
        image=product.find('img')['src'],
        price=helpers.priceFloat(price),
        url=product.select_one('div.product-image a')['href'],
        name=product.select_one('div.name a').text
    )

def nandoMoura(bookName):
    url = "https://livraria.nandomoura.com/index.php?route=product/search&search=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
        image=product.find('img')['src'],
        price=helpers.priceFloat(product.select_one('div.cart-price span.prices').text),
        url=product.find('a')['href'],
        name=product.select_one('span.title a').text,
        store=manyStores("nandoMoura")
    ), html.select('section.features-books div.slide')))
    return books

stores = { 
    'ecclesiae': ecclesiae,
    'deiaetiba': deiaetiba,
    'bernardo': bernardo,
    'seminarioFilosofia': seminarioFilosofia,
    'nandoMoura': nandoMoura
}
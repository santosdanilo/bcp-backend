from bs4 import BeautifulSoup
from digger.databases import helpers
from digger.models.Book import Book
from digger.models.Store import manyStores

def eRealizacoes(bookName):
    url = "https://www.erealizacoes.com.br/busca?palavra=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image="https://www.erealizacoes.com.br/" + product.find('img')['src'],
            price=helpers.cleanPrice(product.find('p', {'class':'preco-atual'}).text),
            url="https://www.erealizacoes.com.br/" + product.find('a')['href'],
            name=product.select_one('h3 a').text,
            store=manyStores("eRealizacoes")
    ), html.select('div.lista-livros ul li')))
    return books

def livrariaFolha(bookName):
    url = "https://livraria.folha.com.br/busca?q=" + bookName + "&product_type=book&type_search=Buscar"
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.find('ins').text),
            url=product.find('a')['href'],
            name=product.find('h3', {'class':'title-prod'}).text,
            store=manyStores("livrariaDaFolha")
        ), html.select('section.cover-products div.spam2')))
    return books

def quadrante(bookName: str):
    url = "https://www.quadrante.com.br/catalogsearch/result/?q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapQuadrante, html.select('ul.products-grid li.item div.box-hover')))

    return books

def mapQuadrante(product):
    check_price = product.find('span', {'class': 'regular-price'})
    check_out_stock = product.find('div', {'class': 'out-of-stock'})
    if not helpers.checkIfNone(check_out_stock):
        if helpers.checkIfNone(check_price):
            price = product.select_one('span.regular-price span.price').text
        else :
            price = product.select_one('p.special-price span.price').text
    else :
        price = 'Fora de Estoque'
    return Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(price),
            url=product.find('a')['href'],
            name=product.select_one('h2.product-name a').text,
            store=manyStores("quadrante")
        )

def caritatem(bookName):
    url = "https://www.livrariacaritatem.com.br/search/?q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.select_one('div.item-image-container img')['src'],
            price=helpers.cleanPrice(product.select_one('div#price_display').text),
            url=product.find('a')['href'],
            name=product.find('h2',{'class':'item-name'}).text,
            store=manyStores('caritatem')
        ), html.select('section.product-grid div.item')))
    return books

def estanteVirtual(bookName):
    url = "https://www.estantevirtual.com.br/busca?q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('strong.busca-price.m-min span').text),
            url=product['href']
        ), html.select('a.busca-box')))
    return books

def familiaCrista(bookName):
    url = "https://www.livrariasfamiliacrista.com.br/catalogsearch/result/?q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapFamiliaCrista, html.select('section.category-products li.item')))
    return books

def mapFamiliaCrista(product):
    check_price = product.find('span', {'class': 'regular-price'})
    check_out_stock = product.find('div', {'class': 'out-of-stock'})
    if not helpers.checkIfNone(check_out_stock):
        if helpers.checkIfNone(check_price):
            price = product.select_one('span.regular-price span.price').text
        else :
            price = product.select_one('p.special-price span.price').text
    else :
        price = 'Fora de Estoque'
    return Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(price),
            url=product.find('a')['href'],
            name=product.select_one('h2.product-name a').text,
            store=manyStores("familiaCrista")
        )

def paulus(bookName):
    url = "https://www.paulus.com.br/loja/search.php?q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=" https://www.paulus.com.br/loja/" + product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('span.preco').text),
            url=product.select_one('a')['href'],
            name=product.find('p',{'class':'titulo'}).text,
            store=manyStores('paulus')
        ), html.select('ul#produto-lista li')))
    return books

def santaCruz(bookName):
    url = "https://www.stacruzartigoscatolicos.com.br/loja/busca.php?loja=431290&palavra_busca=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('span.price').text),
            url=product.select_one('a')['href']
        ), html.findAll('li',{'class':'produto-item'})))
    return books

def shalom(bookName):
    url = "https://livrariashalom.org/catalogsearch/result/index/?cat=9&q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('span.price').text),
            url=product.select_one('a')['href'],
            name=product.find('a',{'class':'product-item-link'}).text,
            store=manyStores('shalom')
        ), html.select('ol.products div.product-item-info')))
    return books

def cultorDeLivros(bookName):
    url = "https://www.cultordelivros.com.br/busca?busca=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('div.precoPor span.fbits-valor').text),
            url="https://www.cultordelivros.com.br" + product.select_one('a')['href'],
            name=product.find('h3',{'class':'spotTitle'}).text,
            store=manyStores("cultorDeLivros")
        ), html.select('div.spots-interna div.spotContent')))
    return books

def loyola(bookName):
    url = "https://www.livrarialoyola.com.br/busca/" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('ins').text),
            url=product.select_one('a')['href']
        ), html.select('nav.listProducts li')))
    return books

def cancaoNova(bookName):
    url = "https://loja.cancaonova.com/catalogsearch/result/?cat=7&q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(mapCancaoNova, html.select('ul.products-grid div.content--product')))
    return books

def mapCancaoNova(product):
    check_price = product.find('span', {'class': 'regular-price'})
    check_out_stock = product.find('div', {'class': 'out-of-stock'})
    if not helpers.checkIfNone(check_out_stock):
        if helpers.checkIfNone(check_price):
            price = product.select_one('span.regular-price span.price').text
        else :
            price = product.select_one('p.special-price span.price').text
    else :
        price = 'Fora de Estoque'
    return Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(price),
            url=product.find('a', {'class':'product-image'})['href'],
            name=product.select_one('h2.product-name a').text,
            store=manyStores("cancaoNova")
        )

def sociedadeChestertonBrasil(bookName):
    url = "https://www.sociedadechestertonbrasil.org/loja/"
    html = helpers.requestAndParse(url)
    books = list(map(mapSociedadeChestertonBrasil, 
            html.select('div.content-area div.product-inner'))
    )
    return books

def mapSociedadeChestertonBrasil(product):
    price = ''
    check_price = product.find('ins')
    if helpers.checkIfNone(check_price):
        price = product.select_one('ins span.woocommerce-Price-amount')
    else :
        price = product.select_one('span.price')
    
    return Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(price.text),
            url=product.find('a')['href'],
            name=product.select_one('li.title a').text
        )


def minhaBibliotecaCatolica(bookName):
    return []

stores = { 
    'eRealizacoes': eRealizacoes,
    'livrariaFolha': livrariaFolha,
    'quadrante': quadrante,
    'caritatem': caritatem,
    'estanteVirtual': estanteVirtual,
    'paulus': paulus,
    'santaCruz': santaCruz,
    'shalom': shalom,
    'cultorDeLivros': cultorDeLivros,
    'loyola': loyola,
    'cancaoNova': cancaoNova,
    'sociedadeChestertonBrasil': sociedadeChestertonBrasil,
    'minhaBibliotecaCatolica': minhaBibliotecaCatolica,
    'familiaCrista': familiaCrista
         }

def getBookStore(bookStore: str):
    return stores[bookStore]

# mercadoLivre
# amazon br
# amazon eua
# submarino
# americanas
# cultura

# loyola
# armazem católico
# canção nova
# ave maria
# https://www.centrosaojosemaria.com.br/shop/
# instituto jackson figueiredo
# hugo de sao vitor
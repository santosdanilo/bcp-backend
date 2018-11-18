from bs4 import BeautifulSoup
from digger.databases import helpers
from digger.models.Book import Book

def eRealizacoes(bookName):
    url = "https://www.erealizacoes.com.br/busca?palavra=" + bookName
    html = helpers.requestAndParse(url)
    books = []
    for product in html.select('div.lista-livros ul li'):
        price = product.findAll('p', {'class':'preco-atual'})[0].text
        price = helpers.cleanPrice(price)
        book = Book(
            image=product.find('img')['src'],
            price=price,
            url=product.find('a')['href']
        )
        books.append(book)

    return books

def livrariaFolha(bookName):
    url = "https://livraria.folha.com.br/busca?q=" + bookName + "&product_type=&type_search=Buscar"
    html = helpers.requestAndParse(url)
    books = []
    for product in html.select('section.cover-products div.spam2'):
        book = Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.find('ins').text),
            url=product.find('a')['href']
        )
        books.append(book)

    return books

def quadrante(bookName):
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
            name=product.select_one('h2.product-name a').text
        )

def caritatem(bookName):
    url = "https://www.livrariacaritatem.com.br/search/?q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('div#price_display').text),
            url=product.find('a')['href']
        ), html.select('div.item')))
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
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('p.special-price span.price').text),
            url=product.select_one('a')['href']
        ), html.select('section.category-products li.item')))
    return books

def paulus(bookName):
    url = "https://www.paulus.com.br/loja/search.php?q=amor" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('span.preco').text),
            url=product.select_one('a')['href']
        ), html.select('ul#produto-lista li')))
    return books

def santaCruz(bookName):
    url = "https://www.stacruzartigoscatolicos.com.br/loja/busca.php?loja=431290&palavra_busca=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('span.price').text),
            url=product.select_one('a')['href']
        ), html.select('div#Vitrine li.produto-item')))
    return books

def shalom(bookName):
    url = "https://livrariashalom.org/catalogsearch/result/index/?cat=9&q=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('span.price').text),
            url=product.select_one('a')['href']
        ), html.select('ol#products div.product-item-info')))
    return books

def cultorDeLivros(bookName):
    url = "https://www.cultordelivros.com.br/busca?busca=" + bookName
    html = helpers.requestAndParse(url)
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('div.precoPor span.fbits-valor').text),
            url=product.select_one('a')['href']
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
    books = list(map(lambda product: Book(
            image=product.find('img')['src'],
            price=helpers.cleanPrice(product.select_one('p.special-price span.price').text),
            url=product.select_one('a')['href']
        ), html.select('ul.products-grid li.product--item')))
    return books

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
    return {}

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
    'minhaBibliotecaCatolica': minhaBibliotecaCatolica
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
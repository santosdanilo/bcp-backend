from digger.databases import core
from digger.databases import cedet
from digger.databases import loja_integrada
from digger.databases import helpers

def getBooksFrom(bookStore, bookName):
    getBookStore = {**core.stores, **cedet.stores}
    getBook = getBookStore[bookStore]
    books = getBook(bookName)
    books = list(filter(lambda x: helpers.containsName(bookName, x.name), books))
    return books
import pytest
from digger.databases import core
from digger.databases import loja_integrada
from digger.models.Book import Book

class TesteCentroDomBosco(object): 
    def test_CentroDomBosco_FindBook(self):
        bookName = "Teologia Moral I"
        mock = Book(
            image='https://cdn.awsli.com.br/300x300/618/618258/produto/27781519/8a9370e179.jpg',
            price='95,00',
            url='https://loja.centrodombosco.org/teologia-moral-santo-afonso-de-ligorio'
        )
        response = loja_integrada.centroDomBosco(bookName)[0]
        assert mock == response

class TesteSaoTomas(object): 
    def test_SaoTomas_FindBook(self):
        bookName = "Da Arte do Belo"
        mock = Book(
            image='https://cdn.awsli.com.br/300x300/369/369566/produto/28636980/760d73c5f7.jpg',
            price='85,00',
            url='https://santotomas.lojaintegrada.com.br/daartedobelo'
        )
        response = loja_integrada.saoTomas(bookName)[0]
        assert mock == response
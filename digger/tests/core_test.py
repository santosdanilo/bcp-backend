import pytest
from digger.databases import core
from digger.databases import loja_integrada
from digger.models.Book import Book

class TesteRealizacoes(object): 
    def test_eRealizacoes_FindBook(self):
        bookName = "A Faca Entrou"
        mock = Book(
            image='/upload/produto/417/afacaentrou_frente160.jpg',
            price=54.90,
            url='/produto/a-faca-entrou---assassinos-reais-e-a-nossa-cultura'
        )
        response = core.eRealizacoes(bookName)[0]
        assert mock == response

class TesteLivrariaFolha(object): 
    def test_LivrariaFolha_FindBook(self):
        bookName = "A Sabedoria dos Antigos"
        mock = Book(
            image='//images1.folha.com.br/livraria/images/a/7/1160107-160x160.png',
            price=3.90,
            url='https://livraria.folha.com.br/livros/filosofia/sabedoria-antigos-francis-bacon-1160107.html'
        )
        response = core.livrariaFolha(bookName)[0]
        assert mock == response

class TesteQuadrante(object): 
    def test_quadrante_FindBook(self):
        bookName = "Vida eucarística"
        mock = Book(
            image='https://www.quadrante.com.br/media/catalog/product/cache/1/small_image/147x231/9df78eab33525d08d6e5fb8d27136e95/v/i/vida-eucaristica_1.jpg',
            price=21.60,
            url='https://www.quadrante.com.br/vida-eucaristica'
        )
        response = core.quadrante(bookName)[1]
        assert mock == response

class TesteFamiliaCrista(object): 
    def test_familiaCrista_FindBook(self):
        bookName = "Os Quatro Amores"
        mock = Book(
            image='https://www.livrariasfamiliacrista.com.br/media/catalog/product/cache/1/small_image/243x300/8104d67811b5b3c5190375b34be1f1fe/0/6/06_1.jpg',
            price=27.92,
            url='https://www.livrariasfamiliacrista.com.br/livro-os-quatro-amores-c-s-lewis.html'
        )
        response = core.familiaCrista(bookName)[1]
        assert mock == response

class TestePaulus(object): 
    def test_paulus_FindBook(self):
        bookName = "Youcat"
        mock = Book(
            image='images/products/M/9789723017717.jpg',
            price='ProdutoIndisponível',
            url='https://www.paulus.com.br/loja/youcat-update-confissao_p_3466.html'
        )
        response = core.paulus(bookName)[0]
        assert mock == response

class TesteCultorDeLivro(object): 
    def test_cultorDeLivros_FindBook(self):
        bookName = "As três idades da vida interior"
        mock = Book(
            image='https://cultordelivros.fbitsstatic.net/img/p/as-tres-idades-da-vida-interior-78497/254979.jpg?w=270&h=405&v=201811131024',
            price=170.00,
            url='/produto/as-tres-idades-da-vida-interior-78497'
        )
        response = core.cultorDeLivros(bookName)[0]
        assert mock == response

class TesteSociedadeChestertonBrasil(object): 
    def test_sociedadeChestertonBrasil_FindBook(self):
        bookName = "As três idades da vida interior"

        mock = Book(
            name="A Sabedoria do Padre Brown",
            image='https://www.sociedadechestertonbrasil.org/wp-content/uploads/2018/02/A-inocência-do-padre-Brown-1200-265x353.png',
            price=170.00,
            url='/produto/as-tres-idades-da-vida-interior-78497'
        )
        response = core.sociedadeChestertonBrasil(bookName)[0]
        assert mock == response
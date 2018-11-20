class Store(dict):
    name=""
    image= ""

    def __init__(self, image, name):
        self.image = image 
        self.name = name
        dict.__init__(self, image=image, name=name)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.name in other.name
        return False

def manyStores(name: str):
    store = {
        'quadrante': Store(
                     name="Quadrante",
                     image="https://www.quadrante.com.br/skin/frontend/linkstore/default/images/logo.gif"
                        ),
        'eRealizacoes': Store(
                        name="É Realizações",
                        image="http://www.erealizacoes.com.br/img/logo.png"
                        ),
        'cancaoNova': Store(
            name="Canção Nova",
            image="https://s1.cancaonova.com/skin/frontend/cancaonova/default/assets/img/cn_logo.png"
        ),
        'cultorDeLivros': Store(
            name="Cultor de Livros",
            image="https://recursos.cultordelivros.com.br/i/cultor-logo.svg"
        ),
        'shalom': Store(
            name="Shalom",
            image="https://livrariashalom.org/media/logo/websites/1/shalom_2.png"
        ),
        'livrariaDaFolha': Store(
            name="Livraria da Folha",
            image="https://s3.amazonaws.com/media.cuponeria.com.br/2014/03/logofolha.jpg"
        ),
        'caritatem': Store(
            name="Caritatem",
            image="https://d26lpennugtm8s.cloudfront.net/stores/645/935/themes/common/logo-218845004-1524498244-0cfe2d7929c1dab6f501a4ec4f5d2bb21524498245-480-0.png?0"
        ),
        'paulus': Store(
            name="Paulus",
            image="https://www.paulus.com.br/loja/templates/responsivo/images/logo.jpg"
        ),
        'familiaCrista': Store(
            name="Família Cristã",
            image="https://www.livrariasfamiliacrista.com.br/skin/frontend/familia/2017/images/logo.png"
        ),
        'ecclesiae': Store(
            name="Ecclesiae",
            image="https://scontent.fbsb9-1.fna.fbcdn.net/v/t1.0-1/1912080_617983061607364_1659207268_n.jpg?_nc_cat=107&_nc_ht=scontent.fbsb9-1.fna&oh=78c907a75a72dda0f33044216aba89a0&oe=5C815EEF"
        ),
        'nandoMoura': Store(
            name="Nando Moura",
            image="https://livraria.nandomoura.com/image/data/logo/logo-nm-branco-170.png"
        ),
        'sociedadeChestertonBrasil': Store(
            name="Sociedade Chesterton Brasil",
            image="https://www.sociedadechestertonbrasil.org/wp-content/uploads/2017/10/cropped-Chesterton_logo-vermelhored-1.png"
        )
    }
    return store[name]
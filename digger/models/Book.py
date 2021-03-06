class Book(dict):
    name=""
    image= ""
    price = ""
    url = ""
    store = ""

    def __init__(self, image, price, url, name="", store=""):
        self.image = image 
        self.price = price
        self.url = url
        self.name = name
        dict.__init__(self, image=image, price=price, url=url, name=name, store=store)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.price == other.price and \
                self.url   == other.url and self.name in other.name
        return False
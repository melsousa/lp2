import uuid


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @staticmethod
    def Product(name, price): #métodos estáticos não define self
        # UIID4 é mais seguro pois não cria um id baseado no endreço da rede
        id = uuid.uuid4()  # UUID aleatório
        return Product(id, name, price)

    def id(self):
        return self.id

    def name(self):
        return self.name

    def price(self):
        return self.price

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt: {self.name}, id: {self.id}, cena: {self.price} pln")

    def __str__(self):
        return f"Produkt: {self.name}, id: {self.id}, cena: {self.price}"

produkt = Product(1, "Woda", 2.99)
produkt.print_info()


print(produkt)
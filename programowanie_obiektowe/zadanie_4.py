# class Basket:
#
#     def __init__(self, product, count, price):
#         self.product = product
#         self.count = count
#         self.price = price
#
#     def product(self):
#         self
#

class BasketEntry:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity

    def report(self):
        return f'- {self.product.name'

class Basket:

    def __init__(self):
        self.entry = []

    def add_product(self, product, quantity):
    #     # add = True
    #     for position in self.entry:
    #         if position[0] == product:
    #             position[1] += quantity
    #             break
    #     else:
    #         self.entry.append([product, quantity])

        basket_entry = BasketEntry(product, quantity)
        for be in self.entry:
            if be.product == product:
                be.quantity += quantity
                break
            else:
                self.entry.append(basket_entry)

    def count_total_price(self):
        total = 0
        for e in self.entry:
            total += e.count_price
        return total


    def generate_report(self):
        report = "Produkty w koszyku :\n"
        for e in self.entry:
            report += f'- {e.product.name} ({e.product.id}), cena: {e.product.price} x {e.quantity}\n'
        report += f"W sumie: {self.count_total_price()}"
        return report


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        """Wypisanie imforacji o produkcie"""

        print(f"Produkt {self.name}, id: {self.id}, cena: {self.price} PLN")



def test_basket_init():
    basket = Basket()
    assert basket.entry == []

def test_product_init():
    product = Product(1, 'Woda', 10)
    assert product.id == 1
    assert product.name == "Woda"
    assert product.price == 10

def test_basket_add_product():
    basket = Basket()
    product = Product(1, 'Woda', 10)
    basket.add_product(product, 5)
    assert len(basket.entry) == 1

def test_basket_add_product_twice():
    basket = Basket()
    product = Product(1, 'Woda', 10)
    basket.add_product(product, 5)
    basket.add_product(product, 3)
    assert len(basket.entry) == 1


def test_basket_count_total_price():
    basket = Basket()
    product1 = Product(1, 'Woda', 10)
    product2 = Product(2, 'Ogorki', 5)
    basket.add_product(product1, 5)
    basket.add_product(product2, 3)
    assert basket.count_total_price() == 5*10 + 3*5


def test_generate_report():
    basket = Basket()
    product = Product(1, 'Woda', 10)
    basket.add_product(product, 5)
    basket.add_product(product, 3)


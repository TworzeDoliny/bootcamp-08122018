class ElectricCar:


    def __init__(self, range):
        self.range = range

    def drive(self, distance):
        self.range -= distance
        if self.range <= 0:
            print("Podładuj baterię")


    def charge(self, way):
        self.range += way
        self.way = range

car = ElectricCar(100)
car.drive(50)
print(car.range)
car.drive(16)
print(car.range)
car.charge(50)
print(car.charge)


# def test_electric_car_init():
#     car = ElectricCar(100)
#     assert car.range == 100
#
# def test_electric_car():
#     car = ElectricCar(100)
#     assert car.drive(50) == 50
#
# def test_electric_car_charge():
#     car = ElectricCar(50)
#     assert car.charge(50) == 100
#
#






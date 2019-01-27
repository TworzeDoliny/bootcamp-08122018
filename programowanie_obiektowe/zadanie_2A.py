# class Dog:
#
#     species = 'Pies pospolity'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.species = Dog.species
#
# azor = Dog("azor", 12)
# piesel = Dog("piesel", 15)
# pimpek = Dog("pimpek", 18)
#
# def oldest_dog(*args):
#     dog_ages = []
#     for dog in args:
#         print(dog.age, dog)
#
#     dog_ages.sort()
#     return dog_ages[-1][1]
#
# dog = oldest_dog(azor, piesel, pimpek)
# dog.name

# oldest_dog(azor, piesel, pimpek)
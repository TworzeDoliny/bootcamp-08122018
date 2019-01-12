# # przykłady_input
#
# # x = float(input("Podaj wartość x:"))
# # y = float(input("POdaj wartość y:"))
#
# # print("Suma:", x + y)
#
# # Przykłady wartośći logiczne
# # operatory porównania
# # ==, <, >, <=, >=, !=
#
# x = 2
# y = 5
#
# print(x > 1 or y > 1)
# print(True or True)
# print(x <1 or y < 1)


# ctrl  + alt + L = pep8, czyli dodaje spacje aby program był czytelny


# Przyłady = pętla while

# i = 0
# while True:
#     if i == 5:
#         continue
#     print(i)
#     i += 1
#     if i == 10:
#         break



#  Napisy

tekst = 'Zla pogoda'
x = 0
while x < len(tekst):
    print(tekst[x])
    x += 1


for litera in enumerate(tekst):
    print(litera)

for x in range(10):
    print(x)

krotka = (1, 2, 3)
print(type(krotka))
print(krotka)
print(krotka[1])

for sc in krotka:
    print(sc)

print(dir(krotka))
print(krotka.count(1))

krotka2 = ("Napis 1", "Napis 2", 1, 2, 3)
print(krotka2.index("Napis 1"))
print(krotka2.count("Napis 1"))


x = (1,2,4,6,7,8,9)
x = x + (1,)
print(x[1:5])



# LISTY

lista = [1,2,3,4,5,6,7,8,9]
print(type(lista))
print(lista[1:5])
print(dir(lista))

print(lista)
lista.append("AA")
print(lista)
print(id(lista))
lista.extend(['a', 'b'])
print(lista)
lista.append(['a', 'b'])
print(lista)
print(lista[-1][-1])
print("jak działa pop")
print(lista)
print(lista.pop())
print(lista)


# print([].pop())
lista = [1,2,5,7,4,9]
print(lista)
print("sortowanie")
print(lista.sort())
print(lista)









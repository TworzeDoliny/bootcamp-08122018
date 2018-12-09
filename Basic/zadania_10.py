# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))
# operacja = int(input("Jaka operacja: ",
#
#
# if operacja == a + b :
#
# print(a + b)
# elif a - b:
# print(a - b)
# elif a * b:
# print(a * b)
# elif a / b: \
#     print(a / b)




# dodawanie = "a + b"
# odejmowanie = "a - b"
# mnozenie = "a * b"
# dzielenie = "a / b"
#
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))
#
# if dodawanie:
#     print(dodawanie)
# if odejmowanie:
#     print(odejmowanie)
# if mnozenie:
#     print(mnozenie)
# if dzielenie:
#     print(dzielenie)


# rozwiązanie najprostsze

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
operacja = input("Podaj rodzaj operacji: ")

if operacja == "+":
    print(a + b)
elif operacja == "-":
    print(a - b)
elif operacja == "/":
    if b == 0:
        print("Operacja niedozwolona")
    else:
        print(a / b)
elif operacja == "*":
    print(a * b)
else:
    print("Operacja nie powiodła się")





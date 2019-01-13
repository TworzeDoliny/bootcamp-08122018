liczby = [1, 2, 3, 4]

liczby2 = [5, 6, 7, 8]

liczby3 = [9, 10, 11, 12]

for i, l in enumerate(liczby):
    print(f"Indeks-{i}, wartość={l}")

for i, l in enumerate(liczby2):
    print(f"Indeks-{i}, wartość={l}")

for i, l in enumerate(liczby3):
    print(f"Indeks-{i}, wartość={l}")


def drukuj(lista):
    for i, l in enumerate(liczby):
        print(f"Indeks={i}, wartość={l}")


drukuj(liczby)
drukuj(liczby2)
drukuj(liczby3)

print(liczby)
print(liczby2)
print(liczby3)

def potega(podstawa, wykladnik=2):
    return podstawa ** wykladnik

print(potega(4, 2))
print(potega(4))
print(potega(4, 3))




def wykonaj_operacje(operacja, *args):
    print(args)
    print(type(args))
    return operacja(args)

print(wykonaj_operacje(min, 10, 20, 30, 40 ,50))
print(wykonaj_operacje(sum, 10, 20, 30, 40 ,50))
print(wykonaj_operacje(max, 10, 20, 30, 40 ,50))


# 8888** Napisz funkcję, która przyjmie dowolną liczbę napisów
# 1. Zwróci te napisy połączone znakiem nowej linii

def napisy(*args, funkcja = None):
    tekst = "\n".join(args)
    if funkcja:
        tekst = funkcja(tekst)

    return tekst


print(napisy('a', 'b', 'c', 'd'))

print("-"*10)

def upper(napis):
    return napis.upper()

print(napisy('a', 'b', 'c', 'd'))
print("-"*10)
print(napisy('a', 'b', 'c', 'd', funkcja=str.upper))




print("ala ma kota". replace("ala", "domi"))
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

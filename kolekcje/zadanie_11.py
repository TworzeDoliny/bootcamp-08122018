# liczby = set()
# print = input("Podaj swoje liczby: ")
# range(0, 101)

liczby = set()
parzyste = set(range(0, 101, 2))
while True:
    komenda = input("Podaj liczbę lub [k] by zakończyć: ")
    if komenda == 'k':
        break
    else:
        liczby.add(int(komenda))

print(liczby)
print("Liczb uniklanych jest: ", len(liczby))
print("Z tego parzystych jest: ", len(liczby & parzyste))

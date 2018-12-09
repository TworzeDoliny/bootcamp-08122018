dane = input("Podaj liczby, rozdziel je spacjami: ")
dane = dane.split()
dane2 = []

for d in dane:
    dane2.append((int(d)))

dane = [int(d) for d in dane]

dane = map(int, dane)
print(list(dane))


print(dane)
print(dane2)

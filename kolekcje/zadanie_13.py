# liczby = lista(i * 0.1 for i in range(0, 10))
# print(liczby)


print([x/10 for x in range(11)])


print({(x, x**2, x**3) for x in range(-10, 11)})


napisy = {"Ala ma kota", "kot ma alę", "wal sie na ryj"}
print({x: len(x) for x in napisy})


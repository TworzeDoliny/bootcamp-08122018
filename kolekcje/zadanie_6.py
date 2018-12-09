liczby = [5, 2, 8, 4, 1]

temp = liczby[0]
liczby[0] = liczby[2]
liczby[2] = temp

liczby[0], liczby[2] = liczby[2], liczby[0]

for i in range(len(liczby)):
    print(i)


# lista = []
# for i in range(10):
#     print("Podaj liczbę: ")
#     x = int(input())
#     lista = lista / 2
#     lista.append(x)
#     print(sum(lista))
#
#
liczby = []

i = 0
while i < 10:
    liczba = input("Podaj liczbę lub k by zakończyć: ")
    if liczba == 'k':
        break


    liczba = int(liczba)
    liczby.append(i)
    i += 1

print("Średnia wynosi: ", sum(liczby) / len(liczby))



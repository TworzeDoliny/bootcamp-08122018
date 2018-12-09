
maksimum = None
minimum = None
liczba = None


while True:
    komenda = input("Podaj liczbę lub k aby zakończyć: ")
    if komenda == 'k':
        break
    if len(komenda) > 0 and komenda[0] == '-' and komenda[1:].isdigit():
        liczba = int(komenda[1:])
        liczba = -liczba
    elif komenda.isdigit():
        liczba = int(komenda)
    else:
        print("nie podałeś liczby")

    if liczba or liczba ==0:
         if maksimum is None or liczba > maksimum:
             maksimum = liczba
         if minimum is None or liczba < minimum:
             minimum = liczba


print("Znalezione maksimum to: ", maksimum)
print("Znlaezione minimum to: ", minimum)

# produkty = {'marchew', 'cebula', 'rzodkiew'}
# cena = 15
# print(produkty)
# print = input("Podaj nazwę produktu:")
# print = input("Podaj wagę produktu:")
#
# if produkty == 'marchew':
#     print(f"")


produkty = {
    "marchew": 1.99,
    "cebula": 4.22,
    "rzodkiew": 2.22
}

magazyn = {
    "marchew": 10,
    "cebula": 10,
    "rzodkiew": 10
}

rola = input("Czy jesteś [klient]em [kl], czy [dostawcą] [d], [q] by zakończyć : ")
if rola.lower() in['klient', 'k']:...
elif rola.lower() in ['dostawca', 'd']:
    do_dodania = input("Podaj produkt w formacie [nazwa ilosc cena]: ")
    if len( do_dodania.split()) == 3:
        nazwa, ilosc, cena = do_dodania.split()
        try:
            ilosc = float(ilosc)
        except ValueError:
            print("Niepoprawna cena")
        cena = float(cena)

    else:
        print("Podałeś produkt w niepoprawnym formacie")

    print(nazwa, ilosc, cena, sep ="\t")

    produkty[nazwa] = cena
    magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc

    print("Dziękuję, Produkt dodany")


#     ścieżka dostawcy
#     dodanie produktu = 'd'
#     zmiana ceny - 'z'

while True:
    print("Nasz sklep oferuje: ")

    for produkt, cena in produkty.items():
        print(f' -{produkt} - {cena}')

    zakup = input("Co chcesz kupić? [k] by zakończyć: ")
    if zakup.lower() == 'k':
        print("Zapraszamy ponownie")
        break
    waga = float(input(f" Ile kg chcesz kupić? -[{zakup}] "))


    if waga > magazyn[zakup]:
        print()
        print("Brak produktów")
        print(f"W magazynie pozostało: {magazyn[zakup]}")
        print()
    else:
        cena = produkty.get(zakup)
        if cena:
            koszt = waga * produkty[zakup]
            print(f"Za [{zakup}] zapłacisz: {koszt}")
            magazyn[zakup] -= waga

        else:
            print("To nie jest nasz produkt")



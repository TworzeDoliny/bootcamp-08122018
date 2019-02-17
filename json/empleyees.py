# import json
#
# pracownicy = []
#
# json_list = json.dumps(pracownicy)
#
# komenda = print(input("Co chcesz zrobić? [d - dodaj, w- wypisz]: "))
#
# if komenda == 'd':
#
#
# with open("pracownicy.txt", 'w') as fp:
#     json.dump(pracownicy, fp)
#
#

import json
import getpass


try:
    with open("employees.json") as fp:
        pracownicy = json.load(fp)
except FileNotFoundError:
    pracownicy = []

def dodaj_pracownika(pracownicy):
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    rok_urodzenia = input("Podaj rok urodzenia: ")
    pensja = input("Pensja: ")


    pracownik = {"imie": imie,
                 "nazwisko": nazwisko,
                 "rok_urodzenia": rok_urodzenia,
                 "pensja": pensja}

    pracownicy.append(pracownik)

    with open("employees.json", 'w') as fp:
        json.dump(pracownicy, fp)


# def wypisz_pracownikow(pracownicy):
#     print("Pracownicy: ")
#     with open("employees.json", 'r') as fp:
#         json.dumps(pracownicy)
#         print(json.dumps(pracownicy))

def wypisz_pracownikow(pracownicy):
    print("Pracownicy: ")
    for nr, pracownik in enumerate(pracownicy, start=1):
        print(f"-[{nr}] {pracownik['imie']} {pracownik['nazwisko']} -rok: {pracownik['rok_urodzenia']},"
              f"pensja: {pracownik['pensja']} ")



def usun_pracownika(pracownicy):
    nr = input("Którego pracownika usunąć?: ")
    haslo= getpass.getpass("Podaj hasło: ")
    if haslo != "Tajne":
        print("Złe hasło")
        return

    del pracownicy[int(nr) - 1]

    with open("employees.json", 'w') as fp:
        json.dump(pracownicy, fp)

wybor = input("Co chcesz zrobić? [d-dodaj, w-wypisz, u-usuń]: ")


if wybor == "d":
    dodaj_pracownika(pracownicy)
elif wybor == "w":
    wypisz_pracownikow(pracownicy)
elif wybor == "u":
    wypisz_pracownikow(pracownicy)
    usun_pracownika(pracownicy)





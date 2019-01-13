
# DEKORATORY

def pobierz_dane():
    print("Pobrałem dane")

def loguj_uzycie(func):
    """To będzie dekorator, Wypisze tekst przed i po uruchomieniu funkcji"""

    def wrapper(*args, **kwargs):
        print("To sie wykona przed")
        # func(*args, **kwargs)
        print("To się wykona po")
        return f"Wynik: {func(*args, **kwargs)}"


    return wrapper

@loguj_uzycie

def potega(podstawa, wykladnik):
    wynik = podstawa ** wykladnik
    print(wynik)
    return wynik

def pobierz_dane():
    print("Pobrałem dane")

print("Bez dekoratora")
pobierz_dane()

print("Udekorowane")
pobierz_dane == loguj_uzycie(pobierz_dane)
pobierz_dane()

potega == loguj_uzycie(potega)
print(potega(2, 4))


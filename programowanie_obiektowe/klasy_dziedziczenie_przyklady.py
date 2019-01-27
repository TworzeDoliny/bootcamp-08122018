class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Cześć jestem {self.imie} {self.nazwisko}")


class Pracownik(Osoba):

    def pracuj(self):
        print("Pracuję...")

    def __init__(self, imie, naziwsko, stanowisko):
        super().__init__(imie, naziwsko)
        self.stanowisko = stanowisko

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Pracuję jako {self.stanowisko}")


osoba = Osoba("Adam", "Słodowy")
osoba.przedstaw_sie()

pracownik = Pracownik("Robert", "Korzeniowski", "trener")
pracownik.przedstaw_sie()
pracownik.pracuj()

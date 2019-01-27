import pytest
import random


class Postac:

    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    @property
    def atak(self):
        # return self._atak + sum([e.bonus_do_ataku for e in self.ekwipunek])
        bonusy = 0

        for przedmiot in self.ekwipunek:
            bonusy += przedmiot.bonus_do_ataku
        return self._atak + bonusy

    def otrzymaj_obrazenia(self, obrazenia):
        self.zdrowie -= obrazenia
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, pkt_zdrowia):
        if self.zdrowie == 0:
            return False
        self.zdrowie += pkt_zdrowia
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

    def dodaj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def zabierz_przedmiot(self, przedmiot):
        self.ekwipunek.remove(przedmiot)

    def moc_ataku(self):
        return random.randint(self.atak / 2, self.atak)

    def __str__(self):
        napis = f"Jestem {self.imie} mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.\n"
        for przedmiot in self.ekwipunek:
            napis += str(przedmiot)

        return napis

class Przedmiot:

    def __init__(self, nazwa, bonus_do_ataku):
        self.nazwa = nazwa
        if isinstance(bonus_do_ataku, int):
            self.bonus_do_ataku = bonus_do_ataku
        else:
            raise ValueError("Bonus powinien być liczbą")


    def __str__(self):
        return f"Ekwipunek: {self.nazwa}, {self.bonus_do_ataku}"



franek = Postac("Franciszek", 40, 200)
print(franek)
przedmiot = Przedmiot("Miecz Strachu", 10)
franek.dodaj_przedmiot(przedmiot)
print(przedmiot)
print("-"*30)
kacper = Postac("Duszek Kacperek", 50, 210)
print(kacper)




def walka(atakujacy, broniacy):


    print(f"Walka {atakujacy.imie} vs {broniacy.imie}")
    print(atakujacy)
    print(broniacy)
    print("-"*30)

    while atakujacy.zdrowie > 0 and broniacy.zdrowie > 0:
        moc_ataku_atakujacego = atakujacy.moc_ataku()
        print(f"{atakujacy.imie} uderza {broniacy.imie} z mocą {moc_ataku_atakujacego}")
        broniacy.otrzymaj_obrazenia(moc_ataku_atakujacego)

        print("-"* 30)

        if broniacy.zdrowie > 0:
            moc_ataku_broniacego = broniacy.moc_ataku()
            print(f"{broniacy.imie} zwraca atakiem {atakujacy.imie} z mocą {moc_ataku_broniacego}")
            atakujacy.otrzymaj_obrazenia(moc_ataku_broniacego)

    print("Koniec walki")
    print(atakujacy)
    print(broniacy)

def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert"
    assert postac.atak == 1
    assert postac.zdrowie == 20
    assert postac.max_zdrowie == 20


def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymaj_obrazenia(200)
    assert postac.zdrowie == 0


def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(50)
    assert postac.zdrowie == 170


def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0


def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200


def test_przedmiot():
    przedmiot = Przedmiot("Miecz Strachu", 10)
    assert przedmiot.nazwa == "Miecz Strachu"
    assert przedmiot.bonus_do_ataku == 10


def test_przedmiot_bonus_is_not_int():
    with pytest.raises(ValueError):
        przedmiot = Przedmiot("Miecz Strachu", "dziesięć")


def test_postać_dodaj_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Sztylet prawdy", 40)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot)
    assert postac.atak == 45
    assert przedmiot in postac.ekwipunek


def test_zabierz_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Sztylet prawdy", 40)
    postac.dodaj_przedmiot(przedmiot)
    assert przedmiot in postac.ekwipunek
    assert postac.atak == 45
    postac.zabierz_przedmiot(przedmiot)
    assert postac.atak == 5
    assert przedmiot not in postac.ekwipunek

def moc_ataku():
    postac = Postac("Rafał", 50, 200)
    assert postac.atak == 50
    moc_atak = postac.moc_atak()
    assert (postac.atak // 2) <= moc_atak <= postac.atak
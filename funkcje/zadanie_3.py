#
# def policz_znaki(napis):
#     wynik = 0
#     czy_zliczac = False
#
#
#     for znak in napis:
#         if znak == "<":
#             czy_zliczac = True
#         elif znak == ">":
#             czy_zliczac = False
#         elif czy_zliczac:
#             wynik += 1
#
#     return wynik
#
# def policz_znaki1(napis1):
#     wynik1 = 0
#     czy_zliczac1 = False
#
#     for znak1 in napis1:
#         if znak1 == "[":
#             czy_zliczac1 = True
#         elif znak1 == "]":
#             czy_zliczac1 = False
#         elif czy_zliczac1:
#             wynik1 += 1
#
#     return wynik1
#
# def policz_znaki2(napis2):
#     wynik2 = 0
#     czy_zliczac2 = False
#
#     for znak2 in napis2:
#         if znak2 == "<<":
#             czy_zliczac2 = True
#         elif znak2 == ">>":
#             czy_zliczac2 = False
#         elif czy_zliczac2:
#             wynik2 *= 2
#
#     return wynik2

def policz_znaki(napis, start="<", stop=">"):

    wynik = 0
    poziom = 0

    for znak in napis:
        if znak == start:
            poziom += 1
        if znak == stop:
            poziom -= 1
        elif poziom:
            wynik += poziom

    return wynik



def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki("") == 0
def test_policz_znaki_w_pełnym_napisie():
    assert policz_znaki("ala ma kota") == 0

def test_policz_znaki_pierwszy_poziom():
    assert policz_znaki("ala ma <kota> a kota ma ale") == 4
    assert policz_znaki("ala ma <kota> a kota <ma> ale") == 6

def test_policz_znaki_1_poziom_ale_nawiasy_kilka_razy():
    assert policz_znaki("ala ma <kota> a kot <ma> ale") == 6

def test_policz_znaki_1_poziom_inne_nawiasy():
    assert policz_znaki("ala ma [kota] a kot [ma ] ale") == 7

def test_policz_znaki_w_nawiasach_zagniezdzonych():
    assert policz_znaki("ala ma <<kota>> a kot <ma> ale") == 10
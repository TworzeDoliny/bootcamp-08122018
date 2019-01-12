
def wiecej_niz(napis, prog):
    wynik = set()
    unikalne = set(napis)
    for l in unikalne:
        if napis.count(l) > prog:
            wynik. add(l)
    return wynik



def test_wiecej_niz():
    assert wiece_niz('ala ma kota a kot ma ale', 3) == {'a', ''}
    assert  wiecej_niz('aaa bbb ccc', 3) == {'a', 'b'}

def test_wiecej_niz_dla_pustego_napisu():
    assert test_wiecej_niz('', 3) == set()


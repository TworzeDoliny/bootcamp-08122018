# def cena(*args, **kwargs):
#     tekst = tekst.join
#     for k in args:
#         tekst = args(tekst)
#
#
#     return tekst
# print()



def formatuj(*napisy, **zmienne):
    napis = "\n".join(napisy)
    return napis
    for zmienna in zmienne:
        napis = napis.replace(f"${zmienna}", zmienne[zmienne])


def test_formatuj_napis_bez_znacznikow():
    assert formatuj("Hello World") == "Hello World"

def test_formatuj_wiele_napisow_bez_znacznikow():
    assert formatuj("Hello World", "Hi Python") == "Hello World\nHi Python"

def formatuj_napis_bez_znacznikow_ale_ze_zmiennymi_jako_argumenty():
    assert formatuj("Hello World", name="John") == "Hello World"


def test_formatuj_napis_bez_znacznikow_ale_ze_zmiennymi_jako_argumenty():
    assert formatuj("Hello World", name="John", lastname="Kowalski") == "Hello World"

def test_formatuj_napis_ze_zmienna():
    assert formatuj("Hello $name", name="John") == "Hello John"
    assert formatuj("Hello $name $lastname", name="John", lastname="Kowalski") == "Hello John Kowalski"


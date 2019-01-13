# lista = [10, 20, 30, 40]
#
# def rekuprint(lista):
#     if len(lista) == 1:
#         print(lista[0])
#     else:
#         print(lista[0])
#         rekuprint(lista[1:])
#
# rekuprint(lista)
#
#
# def powieksz_o_jeden(liczba):
#     liczba += 1
#     print(liczba)
#     powieksz_o_jeden(liczba)
#
# powieksz_o_jeden(1)


def hi():
    return "Hi!"

def goodmornig():
    return "Good Morning sir"

def przywitaj_sie(greeting_function):
    print(greeting_function())
przywitaj_sie(hi)
przywitaj_sie(goodmornig)



def sprawdz_czy(x, funkcja1, funkcja2):
    return funkcja1(x) and funkcja2(x)
def sprawdz_czy_podzielna_przez_2_i_3(x):
    return x%2 == 0 and x%3 == 0
print(sprawdz_czy(125, sprawdz_czy_podzielna_przez_2_i_3, lambda x: x > 5))





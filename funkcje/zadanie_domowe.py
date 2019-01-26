# ## Zad 1
# # # # Napisz funkcję (lub funkcje), które zwrócą maksymalną spośród 3 liczb.
# # # # W rozwiązaniu skorzystaj tylko z możliwośći definiowania funkcji i używania w nich operatorów porównania
# # # # ## Zad 2
# # # # Napisz funkcję, która:
# # # # 1. Jeśli jej argument będzie listą, tuplą bądź zbiroem, zwróci sumę jej elementów
# # # # 2. Jeśli jej argument będzie słownikiem, zwróci sumę wartości
# # # # W obu przypadkach ignoruj napisy - o ile napisy nie reprezentują liczb
# # # # ## Zad 3
# # # # Napisz funkcję, która sprawdzi czy podany napis jest palindromem
# # # # ## zad 4
# # # # Napisz funkcję, które wypisze n pierwszych wierszy trójkąta Pascala
# # # # ## Zad 5
# # # # Napisz funkcję, która sprawdzi, czy napis jest pangramem.
# # # # ## Zad 6
# # # # Napisz funkcję, które sprawdzi, czy zadana liczba jest doskonała
# # # # ## Zad 7
# # # # Napisz dekorator, który będzie printował w konsoli czas wykonania dekorowanej funkcji.


# Zad1

def max_z_dwoch(a, b):
    if a > b:
        return a
    else:
        return b


def max_z_trzech(x, y, z):
    return max_z_dwoch(x, max_z_dwoch(x, y))


assert 0 == max_z_trzech(0, 0, 0)
assert 3 == max_z_trzech(1, 2, 3)
assert 12 == max_z_trzech(10, 2, -3)

# zad2

def sumator(arg):
    total = 0
    if isinstance(arg, dict):
        arg = arg.values()

    for x in arg:
        try:
            x = int(x)
            total += x
        except ValueError:
            pass
    return total


assert sumator([1, 2, 3]) == 6
assert sumator([10, 20, 30]) == 60
assert sumator([1, 2, 'a', 3]) == 6
assert sumator([1, 2, '4', 3]) == 10
assert sumator({'a': 10, 1: 20, 'c': 30, 'd': '40'}) == 100


# zad3
napis = "To jest napis"
napis = napis.lower().split()
"".join(napis)








assert czy_palindrom("Kobyła ma mały bok") == True
assert czy_palindrom("Zakopane na pokaz") == True
assert czy_palindrom("Ala ma kota") == False
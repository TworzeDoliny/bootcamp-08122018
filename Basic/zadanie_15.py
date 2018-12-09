# from random import randint
# from random import choice
# lista = [1, 10]
#
# print(choice(lista))
#
# x = randint(1, 10)
# y = randint(1, 10)
#
# ruch = choice
#
# if x <1 and y >10 or x >10 and y <1:
#     print("Jesteś poza polem, przegrałeś")
#
#
#      if ruch == "prawo":
#          x += 1
#      if ruch == "lewo":
#          x -= 1
#      if ruch == "gora":
#          y += 1
#      if ruch == "dol":
#          y -= 1
#      if ruch == "prawogora":
#          x += 1
#          y += 1
#      if ruch == "lewogora":
#          x -= 1
#          y += 1
#      if ruch == "prawodol":
#          x += 1
#          y -= 1
#      if ruch == "lewodol":
#          x -= 1
#          y -= 1




from random import randint

gracz_x = randint(1, 10)
gracz_y = randint(1, 10)
skarb_x = randint(1, 10)
skarb_y = randint(1, 10)

min_l_krokow_po_wyl = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
liczba_krokow = 0
DEBUG = False

while True:

    min_l_krokow_przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    print(f"Twoja pozycja to: {gracz_x}, {gracz_y}")

    if DEBUG:
        print("DEBUG info: ")
        print(f"Pozycja skarbu to: {skarb_x}, {skarb_y}")
        print("Minimalna liczba kroków", min_l_krokow_po_wyl)

    kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo, d-prawo: ")
    if kierunek == "w":
        gracz_y += 1
    elif kierunek == "s":
        gracz_y -= 1
    elif kierunek == "d":
        gracz_x += 1
    elif kierunek == "a":
        gracz_x -= 1

    liczba_krokow += 1
    min_l_krokow_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    if gracz_x < 1 or gracz_y <1 or gracz_x > 10 or gracz_y >10:
        print("Wyszedłeś poza plansze, przegrałeś !")
        break

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print("Wygrałeś")
        print(f"Minimalna liczba kroków wynosiła: {min_l_krokow_po_wyl}")
        print(f"Zrobiłeś kroków: {liczba_krokow}")
        break


    if min_l_krokow_po_ruchu < min_l_krokow_przed_ruchem:
        print("ciepło")
    else:
        print("zimnno")

    if liczba_krokow >= min_l_krokow_po_wyl * 2:
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        print("Przekroczyłeś dopuszczalną liczbę kroków, skarb zmienił położenie ")
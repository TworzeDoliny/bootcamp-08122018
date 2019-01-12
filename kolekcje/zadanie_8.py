# print("Napisz zdanie")
# napis = input()
#
# for i in range(len(napis)):
#     if napis
#
text = input("Podaj tekst:")


# text1 = "Ala ma kota"
# text2 = "Ala <ma> kota"
# text3 = "Ala <> ma"
dlugosc = 0
licz = False


dlugosc = 0

for znak in text:
    if znak == "<":
        licz = True
    elif znak == ">":
        licz = False
        break
    elif licz:
        dlugosc += 1

# print(dlugosc)
# assert dlugosc == 0
print(f"Ilość znaków pomiędzy <> wynosi: {dlugosc}")



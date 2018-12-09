# lista = []
# baza = [20, -3, 12, -89, 22, -67]
#
# a = "dodatnie"
# b = "ujemne"
#
# if a >= 1:
#     print("Są to liczby dodatnie")
# elif b <= 1:
#     print("Są to liczby ujemne")
#


baza = [22, 34, 12, -3, -44, -34]

dodatnie = 0
ujemne = 0

for liczba in baza:
    if liczba > 0:
        dodatnie += 1
    elif liczba < 0:
        ujemne += 1

print(f"Liczba dodatnich: {dodatnie}, liczby ujemnie: {ujemne}")

licznik_dodatnich = len([x for x in baza if x > 0])
licznik_ujemnych = len([x for x in baza if x < 0])
print(f"Liczby dodatnie: {licznik_dodatnich}, Liczby ujemne: {licznik_ujemnych}")

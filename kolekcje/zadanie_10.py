#
# znaki = {}
# text = "Ala ma kota"
#
# for znak in text:
#     if znak in znaki:
#         znaki[znak] += 1
#     else:
#         znaki[znak] = 1
#
# print("Statystyka: ")
#
# for z, c in znaki.items():
#     print(f" - {z} wystąpił {c}")



znaki = {}
text = "Ala ma kota"

for znak in text:
    znaki[znak] += 1

print("Statystyka: ")

for z, c in znaki.items():
     print(f" - {z} wystąpił {c}")



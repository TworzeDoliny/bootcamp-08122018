licznik = 0

for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        licznik += 1

print(licznik)
print("W przedziale od 0 - 100 jest", licznik, "liczb podzielnych prze 3 i 5")






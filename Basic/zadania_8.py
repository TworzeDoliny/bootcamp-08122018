długosc = int(input("Długość : "))
szerokosc = int(input("Szerokość : "))
wysokosc = int(input("Wysokość : "))

objetosc = długosc * szerokosc * wysokosc

print(f"Objętość wynosi: {objetosc} ")
print(f"Czy większe od 1 litra: {objetosc > 1000}")

if objetosc < 1000:
    print("Objętość jest większa niż 1 litr")
else:
    print("Objętość jest mniejsza niż 1 litr")

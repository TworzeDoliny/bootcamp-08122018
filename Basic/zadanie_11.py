x = int(input("Podaj pozycję gracza x: "))
y = int(input("Podaj pozycję gracza y: "))


if x < 0 or x >100 or y < 0 or y >100:
    print("Gracz jest poza polem")
elif x <= 10 and y <= 10:
    print("Gracz znajduję się w lewym dolnym rogu")
elif x >=90 and y <=10:
    print("Gracz znajduje się w prawym dolnym rogu")
elif x <= 10 and y >= 90:
    print("Gracz znajduje się w lewym górnym rogu")
elif x >= 90 and y >= 90:
    print("Gracz znajduje się w prawym górnym rogu")
elif x >= 10 and y >= 10 or x <= 90 and y <= 90:
    print("Gracz znajduje się w środku pola")
elif x > 100 and y > 100:
    print("Gracz jest poza polem")
elif x >= 10 and y >= 10 or x <=90 or y <= 10:
    print("Gracz znajdue się na dolnej krawędzi")
elif x >= 90 and y <= 90 or x >= 90 and y >= 10:
    print("gracz znajduje się na prawej krawedzi")
elif x >= 10 and y <= 90 or x <= 90 and y <= 90:
    print("Gracz znajduje sie na gornej krawedzi")
elif x <= 10 and y <= 10 or x <= 10 and y <= 90:
    print("Gracz znajduje się na lewej krawędzi")
elif x < 0 or x >100 or y < 0 or y >100:
    print("Gracz jest poza polem")



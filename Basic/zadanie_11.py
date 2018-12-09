x = int(input("Podaj pozycję gracza x: "))
y = int(input("Podaj pozycję gracza y: "))

if x <= 10 and y <= 10:
    print("Gracz znajduję się w lewym dolnym rogu")
elif x >=90 and y <=10:
    print("Gracz znajduje się w prawym dolnym rogu")
elif x<= 10 and y/
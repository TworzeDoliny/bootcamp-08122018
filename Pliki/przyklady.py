

with open("readme.txt", encoding="utf-8") as f:
    print(f.read())

with open("readme3.txt.", "w") as f:
    f.write("Ala ma kotan i psa")

with open("readme3.txt.", "a") as f:
    f.write("\na pies ma ale i kota")
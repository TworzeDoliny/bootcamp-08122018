ILE_DNI = 7
temperatura = 0
x = 1
while x < ILE_DNI:
    temperatura_x = float(input(f"Podaj temperature w dniu {x} lub [k] by zakończyć: "))
    if temperatura_x == 'k':
        break
    temperatura += temperatura_x
    x += 1

print("Średnia temperatura wynosiła: ", temperatura/(x - 1))

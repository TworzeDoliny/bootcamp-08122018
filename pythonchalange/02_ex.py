from string import ascii_letters

with open("tutaj wpisz plik w którym szukasz liter") as f:
    dane= f.read()

out = []

for z in dane:
    if z in ascii_letters:
        out.append(z)

import re

pattern = re.compile("[a-z]")
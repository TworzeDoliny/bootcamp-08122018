import re

s = "Ala ma kota! Kot ma Ale. Kot lubi mleko. Nie lubi ryb. "
print(s)
print(re.findall(r'([A-Z]\w*)\W.*?[\.\!]', s))



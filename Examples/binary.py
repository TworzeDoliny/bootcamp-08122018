

with open(r'C:\Program Files (x86)\Microsoft Office\Stationery\1033\CURRENCY.GIF', 'rb') as f:
    img = f.read()
    # print(img.decode('latin'))

import struct

print(struct.unpack('<HH', img[6:10]))


# for x in range(0, 10):
#     print(x,'', end='')
#     for y in range(0, 10):
#         print(y, '', end= '')
#     print((x * y))
#
#



for i in range(0, 10):
    print(f"{i:4}", end='')
print()
print()

for x in range(0, 10):
    print(f"{x:4}", end='')
    for y in range(0, 10):
        print(f"{x*y:4}", end='')
        print()

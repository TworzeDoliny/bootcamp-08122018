# liczby = [2, 6, 12, 14, 16, 77, 52, 1, 4, 9]
# min = 0
# for i in range(len(liczby)):
#     if liczby[i] < liczby [min]:
#         print("Znalazłem minimum")
#         print("Nowa wartość minimum to: ", liczby[i])
#         print("Nowy indeks minimum to: ", i)
#         min = i
#
# liczby[1], liczby[min]  = liczby[min], liczby[1]

# liczby = [2, 6, 12, 14, 16, 77, 52, 1, 4, 9]
# min = 0
#
#
# for i in range(1,len(liczby)):
#         liczby = min[i]
#         j = i - 1
#         while j >=0 and min[j]>liczby:
#             min[j + 1] = min[j]
#             j = j - 1
#         min[j + 1] = liczby
#
# print(liczby)

liczby = [2, 6, 12, 14, 16, 77, 52, 1, 4, 9]
min = 0


for i in range(len(liczby)):
    min = i
    for j in range(i, len(liczby)):
        if liczby[j] < liczby[min]:
            min = j
    liczby[i], liczby[min] = liczby[min], liczby[i]

print(liczby)

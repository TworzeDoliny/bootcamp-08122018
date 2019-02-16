# import os
#
# path =
#
# for root, dirs, files in os.walk(path):
#     for filename in files:
#         print(filename)
#
#
#
# fname = input("Wpisz nazwe pliku: ")
# num_lines = 0
# with open(fname, 'r') as f:
#     for line in f:
#         num_lines += 1
# print("Liczba linii:")
# print(num_lines)


import os

def check_dir(path):
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            if name.endswith(".py"):
                print(os.path.join(path, name))
        if os.path.isdir(name):
            check_dir(os.path.join(path, name))

check_dir(os.getcwd())


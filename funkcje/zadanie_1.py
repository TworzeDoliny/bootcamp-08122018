        # print = input("Podaj liczbę: ")
        #
        #
        # def czy_jest_pierwsza(a):
        #     for a % a == 1 and a % 1 == 1:
        #         return True
        #     else:
        #         return False

        # assert czy_jest_pierwsza(17) = True
        # assert czy_jest_pierwsza(10) = False

        # def lop(lpp):
        #     if lpp == 0 and lpp == 1:
        #         return False
        #     if lpp


def czy_jest_pierwsza(a):
    for i in range(2, a//2 +1):
        if a % 1 == 0:
            return False
    return True

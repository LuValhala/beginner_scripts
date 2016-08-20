# -*- coding: utf-8 -*-
def dvojkova(binary):
    print('Dvojková sústava')
    vysledok = 0
    binary=str(binary)
    for c in range(len(binary) - 1, -1, -1):
        vysledok += int(binary[c]) * (2 ** (len(binary) - c - 1))
    print(binary,"=",vysledok)

def sestnastkova(sixtn):
    print('Sestnastkova sustava')
    slovnik = {}
    for i in range(10):
        slovnik[str(i)] = i
    for i in range(6):
        slovnik[chr(65 + i)] = 10 + i
    vysledok = 0
    for c in range(len(sixtn) - 1, -1, -1):
        vysledok += slovnik[sixtn[c]] * (16 ** (len(sixtn) - c - 1))

    print(sixtn, "=", vysledok)

dvojkova("110011")
sestnastkova("36DE8F")

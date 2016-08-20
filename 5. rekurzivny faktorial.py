# -*- coding: utf-8 -*-

def faktorial(i):
    if i > 1:
        return(i * faktorial(i - 1))
    else:
        return(1)
si = input("Zadaj celé číslo: ")
i = None
while i == None:
    try:
        i = int(si)
    except ValueError:
        si = input("Zadaj CELÉ číslo: ")
    else:
        break
print("{}! = {}".format(i, faktorial(i)))
        

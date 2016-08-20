# -*- coding: utf-8 -*-
#nie su osetrene unicode znaky
#vypis mocniny
import random

def expo(m, ex, topr = False):
    if topr:
        print("{}^{}".format(m, ex), end = '')
    else:
        return("{}^{}".format(m, ex))

#rozklad na prvocislo
def rozklad(cislo):
    piv = 2
    rest = cislo
    roz = []
    while rest != 1:
        ex = 0
        while 0 == rest % piv:
            ex += 1
            rest = rest // piv
        if 0 != ex:
            roz.append((piv, ex,))
        piv += 1
    return roz

#prinr rozkladu
def print_rozkladu(roz, topr = False):
    zoznam = [expo(i[0], i[1]) for i in roz]
    if topr:
        print(*zoznam, sep = ' ', end = '')
    else:
        return(' '.join(zoznam))
for i in range(5):
    x=random.randint(10,500)
    print("{} = {}".format(x, print_rozkladu(rozklad(x))))
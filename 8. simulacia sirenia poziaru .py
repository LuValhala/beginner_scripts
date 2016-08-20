# -*- coding: utf-8 -*-
"""
ZADANIE: simulujte šírenie požiaru akýmkoľvek spôsobom na aspoň 5 cyklov, výstup má byť video, gifko alebo súbor obrázkov
simulacia sirenia poziaru z ohniska pomocou kniznice numpy simulovanej na nulovej matici s jedným ohniskom
prvy cyklus simuluje casove periodz, dalsie dva idu po riadkoch a stlpcoch, ak najde cislo v matici vyssie ako 1(poziar)
tak vygeneruje nahodne cislo - podla neho sa ohen rozsiri do novej strany do novej matice
nemoze ale horiet donekonecna tak vsetky hodnoty vyssie ako 5 ostanu piatimi, Ľuboš Valčo
"""

import numpy as np
import random
import matplotlib
from matplotlib import pyplot as plt

x=30
y=30
a0 = np.zeros((x, y))
a1 = np.zeros((x, y))
a2 = np.zeros((x, y))
a3 = np.zeros((x, y))
a4 = np.zeros((x, y))
a5 = np.zeros((x, y))
a6 = np.zeros((x, y))
a7 = np.zeros((x, y))
a8 = np.zeros((x, y))
a9 = np.zeros((x, y))
a10 = np.zeros((x, y))
a11 = np.zeros((x, y))
a12 = np.zeros((x, y))
a13 = np.zeros((x, y))
a14 = np.zeros((x, y))

h=[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14]

#zapálenie
a0[14,14] = 1

for k in range(len(h)-1):
    for i in range(0,30):
        for j in range(0,30):
            #podmienka sirenia, existencia poziaru na danom bode
            if h[k][i,j] >= 1:
                h[k+1][i,j] = h[k][i,j]            
                r=random.randint(1,10)
                #náhodné šírenie do 1 alebo 2 strán
                if r ==1:
                    h[k+1][(i+1),j] = h[k][(i+1),j]+1
                if r ==2:
                    h[k+1][i,(j+1)] = h[k][i,(j+1)]+1
                if r ==3:
                    h[k+1][(i-1),j] = h[k][(i-1),j]+1
                if r ==4:
                    h[k+1][i,(j-1)] = h[k][i,(j-1)]+1
                if r ==5:
                    h[k+1][(i-1),j] = h[k][(i-1),j]+1
                if r ==6:
                    h[k+1][(i+1),j] = h[k][(i+1),j]+1
                    h[k+1][(i-1),j] = h[k][(i-1),j]+1
                if r==7:
                    h[k+1][(i-1),j] = h[k][(i-1),j]+1
                    h[k+1][i,(j-1)] = h[k][i,(j-1)]+1
                if r==7:
                    h[k+1][(i+1),j] = h[k][(i+1),j]+1
                    h[k+1][i,(j+1)] = h[k][i,(j+1)]+1
                if r==8:
                    h[k+1][(i+1),j] = h[k][(i+1),j]+1
                    h[k+1][i,(j-1)] = h[k][i,(j-1)]+1
                if r==9:
                    h[k+1][i,(j+1)] = h[k][i,(j+1)]+1
                    h[k+1][(i-1),j] = h[k][(i-1),j]+1
                #vybuch požiaru do okolia
                if r==10:
                    h[k+1][(i+1),j] = h[k][(i+1),j]+1
                    h[k+1][(i+2),j] = h[k][(i+2),j]+1
                    h[k+1][(i-1),j] = h[k][(i-1),j]+1
                    h[k+1][(i-2),j] = h[k][(i-2),j]+1
                    h[k+1][i,(j+1)] = h[k][i,(j+1)]+1
                    h[k+1][i,(j+2)] = h[k][i,(j+2)]+1
                    h[k+1][i,(j-1)] = h[k][i,(j-1)]+1
                    h[k+1][i,(j-2)] = h[k][i,(j-2)]+1
    #zhladenie, predpokladame ze nie je viac co spalit
    if k > 2:
        if h[k+1][i,j] >= 5:
            h[k+1][i,j] = 5
    
    #ulozenie obrazku v priecinku kde je skript 
    plt.imsave("{}.png".format(k), h[k], cmap='gray')
    if k == len(h)-2:
        plt.imsave("{}.png".format(k+1), h[k+1], cmap='gray')



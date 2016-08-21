# -*- coding: utf-8 -*-
"""
ZADANIE: simulate the fire spread, at least 5 cycles and the output must be a video, gif file or a dozen of images 
showing the spread. Epicentre of the fire as a number 1 is placed inside of a numpy array of zeroes. With each cycle the
fire spreads in random direction. Cycles in orded: first stimulate time of the fire, second and third are to calculate 
the y and x axis. Trigger for further release of the fire is existing fire (value higher than zero)
Since there is no more material to be burned, any number higher than 5 will be cut back to 5 with a simple IF statement
Ľuboš Valčo, Originaly realeased december 2015. August 2016: repaired the code to be more readable and less repeatable.
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



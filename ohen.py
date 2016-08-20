#simulacia sirenia poziaru z ohniska pomocou kniznice numpy simulovanej na nulovej matici s jedným ohniskom
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

a0[14,14] = 1

#README: az neskor som si uvedomil ze som mohol spravit jedec zoznam prazdnych matic(napr."h") a ten zoznam pouzit ako cyklus for k in h: a tak obalit cely cyklus bez kopirovania....
#tak sa mi to ale nechcelo uz prepisovat nabuduce uz budem viac mudrejsi a menej "zbytocne spamujuci"
#prvy cyklus ide po riadkoch druhy po stlpcoch, ak najde cislo v matici vyssie ako 1 cize poziar tak vygeneruje nahodne cislo - podla neho sa ohen rozsiri do novej strany do novej matice
#nemoze ale horiet donekonecna tak vsetky hodnoty vyssie ako 5 ostanu piatimi

for i in range(0,30):
    for j in range(0,30):
        if a0[i,j] >= 1:
            a1[i,j] = a0[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a1[(i+1),j] = a0[(i+1),j]+1
            if r ==2:
                a1[i,(j+1)] = a0[i,(j+1)]+1
            if r ==3:
                a1[(i-1),j] = a0[(i-1),j]+1
            if r ==4:
                a1[i,(j-1)] = a0[i,(j-1)]+1
            if r ==5:
                a1[(i-1),j] = a0[(i-1),j]+1
            if r ==6:
                a1[(i+1),j] = a0[(i+1),j]+1
                a1[(i-1),j] = a0[(i-1),j]+1
            if r==7:
                a1[(i-1),j] = a0[(i-1),j]+1
                a1[i,(j-1)] = a0[i,(j-1)]+1
            if r==7:
                a1[(i+1),j] = a0[(i+1),j]+1
                a1[i,(j+1)] = a0[i,(j+1)]+1
            if r==8:
                a1[(i+1),j] = a0[(i+1),j]+1
                a1[i,(j-1)] = a0[i,(j-1)]+1
            if r==9:
                a1[i,(j+1)] = a0[i,(j+1)]+1
                a1[(i-1),j] = a0[(i-1),j]+1
            if r==10:
                a1[(i+1),j] = a0[(i+1),j]+1
                a1[(i+2),j] = a0[(i+2),j]+1
                a1[(i-1),j] = a0[(i-1),j]+1
                a1[(i-2),j] = a0[(i-2),j]+1
                a1[i,(j+1)] = a0[i,(j+1)]+1
                a1[i,(j+2)] = a0[i,(j+2)]+1
                a1[i,(j-1)] = a0[i,(j-1)]+1
                a1[i,(j-2)] = a0[i,(j-2)]+1

for i in range(0,30):
    for j in range(0,30):
        if a1[i,j] >= 1:
            a2[i,j] = a1[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a2[(i+1),j] = a1[(i+1),j]+1
            if r ==2:
                a2[i,(j+1)] = a1[i,(j+1)]+1
            if r ==3:
                a2[(i-1),j] = a1[(i-1),j]+1
            if r ==4:
                a2[i,(j-1)] = a1[i,(j-1)]+1
            if r ==5:
                a2[(i-1),j] = a1[(i-1),j]+1
            if r ==6:
                a2[(i+1),j] = a1[(i+1),j]+1
                a2[(i-1),j] = a1[(i-1),j]+1
            if r==7:
                a2[(i-1),j] = a1[(i-1),j]+1
                a2[i,(j-1)] = a1[i,(j-1)]+1
            if r==7:
                a2[(i+1),j] = a1[(i+1),j]+1
                a2[i,(j+1)] = a1[i,(j+1)]+1
            if r==8:
                a2[(i+1),j] = a1[(i+1),j]+1
                a2[i,(j-1)] = a1[i,(j-1)]+1
            if r==9:
                a2[i,(j+1)] = a1[i,(j+1)]+1
                a2[(i-1),j] = a1[(i-1),j]+1
            if r==10:
                a2[(i+1),j] = a1[(i+1),j]+1
                a2[(i+2),j] = a1[(i+2),j]+1
                a2[(i-1),j] = a1[(i-1),j]+1
                a2[(i-2),j] = a1[(i-2),j]+1
                a2[i,(j+1)] = a1[i,(j+1)]+1
                a2[i,(j+2)] = a1[i,(j+2)]+1
                a2[i,(j-1)] = a1[i,(j-1)]+1
                a2[i,(j-2)] = a1[i,(j-2)]+1                

for i in range(0,30):
    for j in range(0,30):
        if a2[i,j] >= 1:
            a3[i,j] = a2[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a3[(i+1),j] = a2[(i+1),j]+1
            if r ==2:
                a3[i,(j+1)] = a2[i,(j+1)]+1
            if r ==3:
                a3[(i-1),j] = a2[(i-1),j]+1
            if r ==4:
                a3[i,(j-1)] = a2[i,(j-1)]+1
            if r ==5:
                a3[(i-1),j] = a2[(i-1),j]+1
            if r ==6:
                a3[(i+1),j] = a2[(i+1),j]+1
                a3[(i-1),j] = a2[(i-1),j]+1
            if r==7:
                a3[(i-1),j] = a2[(i-1),j]+1
                a3[i,(j-1)] = a2[i,(j-1)]+1
            if r==7:
                a3[(i+1),j] = a2[(i+1),j]+1
                a3[i,(j+1)] = a2[i,(j+1)]+1
            if r==8:
                a3[(i+1),j] = a2[(i+1),j]+1
                a3[i,(j-1)] = a2[i,(j-1)]+1
            if r==9:
                a3[i,(j+1)] = a2[i,(j+1)]+1
                a3[(i-1),j] = a2[(i-1),j]+1
            if r==10:
                a3[(i+1),j] = a2[(i+1),j]+1
                a3[(i+2),j] = a2[(i+2),j]+1
                a3[(i-1),j] = a2[(i-1),j]+1
                a3[(i-2),j] = a2[(i-2),j]+1
                a3[i,(j+1)] = a2[i,(j+1)]+1
                a3[i,(j+2)] = a2[i,(j+2)]+1
                a3[i,(j-1)] = a2[i,(j-1)]+1
                a3[i,(j-2)] = a2[i,(j-2)]+1

for i in range(0,30):
    for j in range(0,30):
        if a3[i,j] >= 1:
            a4[i,j] = a3[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a4[(i+1),j] = a3[(i+1),j]+1
            if r ==2:
                a4[i,(j+1)] = a3[i,(j+1)]+1
            if r ==3:
                a4[(i-1),j] = a3[(i-1),j]+1
            if r ==4:
                a4[i,(j-1)] = a3[i,(j-1)]+1
            if r ==5:
                a4[(i-1),j] = a3[(i-1),j]+1
            if r ==6:
                a4[(i+1),j] = a3[(i+1),j]+1
                a4[(i-1),j] = a3[(i-1),j]+1
            if r==7:
                a4[(i-1),j] = a3[(i-1),j]+1
                a4[i,(j-1)] = a3[i,(j-1)]+1
            if r==7:
                a4[(i+1),j] = a3[(i+1),j]+1
                a4[i,(j+1)] = a3[i,(j+1)]+1
            if r==8:
                a4[(i+1),j] = a3[(i+1),j]+1
                a4[i,(j-1)] = a3[i,(j-1)]+1
            if r==9:
                a4[i,(j+1)] = a3[i,(j+1)]+1
                a4[(i-1),j] = a3[(i-1),j]+1
            if r==10:
                a4[(i+1),j] = a3[(i+1),j]+1
                a4[(i+2),j] = a3[(i+2),j]+1
                a4[(i-1),j] = a3[(i-1),j]+1
                a4[(i-2),j] = a3[(i-2),j]+1
                a4[i,(j+1)] = a3[i,(j+1)]+1
                a4[i,(j+2)] = a3[i,(j+2)]+1
                a4[i,(j-1)] = a3[i,(j-1)]+1
                a4[i,(j-2)] = a3[i,(j-2)]+1
for i in range(0,30):
    for j in range(0,30):
        if a4[i,j] >= 5:
            a4[i,j] = 5

for i in range(0,30):
    for j in range(0,30):
        if a4[i,j] >= 1:
            a5[i,j] = a4[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a5[(i+1),j] = a4[(i+1),j]+1
            if r ==2:
                a5[i,(j+1)] = a4[i,(j+1)]+1
            if r ==3:
                a5[(i-1),j] = a4[(i-1),j]+1
            if r ==4:
                a5[i,(j-1)] = a4[i,(j-1)]+1
            if r ==5:
                a5[(i-1),j] = a4[(i-1),j]+1
            if r ==6:
                a5[(i+1),j] = a4[(i+1),j]+1
                a5[(i-1),j] = a4[(i-1),j]+1
            if r==7:
                a5[(i-1),j] = a4[(i-1),j]+1
                a5[i,(j-1)] = a4[i,(j-1)]+1
            if r==7:
                a5[(i+1),j] = a4[(i+1),j]+1
                a5[i,(j+1)] = a4[i,(j+1)]+1
            if r==8:
                a5[(i+1),j] = a4[(i+1),j]+1
                a5[i,(j-1)] = a4[i,(j-1)]+1
            if r==9:
                a5[i,(j+1)] = a4[i,(j+1)]+1
                a5[(i-1),j] = a4[(i-1),j]+1
            if r==10:
                a5[(i+1),j] = a4[(i+1),j]+1
                a5[(i+2),j] = a4[(i+2),j]+1
                a5[(i-1),j] = a4[(i-1),j]+1
                a5[(i-2),j] = a4[(i-2),j]+1
                a5[i,(j+1)] = a4[i,(j+1)]+1
                a5[i,(j+2)] = a4[i,(j+2)]+1
                a5[i,(j-1)] = a4[i,(j-1)]+1
                a5[i,(j-2)] = a4[i,(j-2)]+1
        if a5[i,j] >= 5:
                a5[i,j] = 5
for i in range(0,30):
    for j in range(0,30):
        if a5[i,j] >= 5:
            a5[i,j] = 5

for i in range(0,30):
    for j in range(0,30):
        if a5[i,j] >= 1:
            a6[i,j] = a5[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a6[(i+1),j] = a5[(i+1),j]+1
            if r ==2:
                a6[i,(j+1)] = a5[i,(j+1)]+1
            if r ==3:
                a6[(i-1),j] = a5[(i-1),j]+1
            if r ==4:
                a6[i,(j-1)] = a5[i,(j-1)]+1
            if r ==5:
                a6[(i-1),j] = a5[(i-1),j]+1
            if r ==6:
                a6[(i+1),j] = a5[(i+1),j]+1
                a6[(i-1),j] = a5[(i-1),j]+1
            if r==7:
                a6[(i-1),j] = a5[(i-1),j]+1
                a6[i,(j-1)] = a5[i,(j-1)]+1
            if r==7:
                a6[(i+1),j] = a5[(i+1),j]+1
                a6[i,(j+1)] = a5[i,(j+1)]+1
            if r==8:
                a6[(i+1),j] = a5[(i+1),j]+1
                a6[i,(j-1)] = a5[i,(j-1)]+1
            if r==9:
                a6[i,(j+1)] = a5[i,(j+1)]+1
                a6[(i-1),j] = a5[(i-1),j]+1
            if r==10:
                a6[(i+1),j] = a5[(i+1),j]+1
                a6[(i+2),j] = a5[(i+2),j]+1
                a6[(i-1),j] = a5[(i-1),j]+1
                a6[(i-2),j] = a5[(i-2),j]+1
                a6[i,(j+1)] = a5[i,(j+1)]+1
                a6[i,(j+2)] = a5[i,(j+2)]+1
                a6[i,(j-1)] = a5[i,(j-1)]+1
                a6[i,(j-2)] = a5[i,(j-2)]+1
for i in range(0,30):
    for j in range(0,30):
        if a6[i,j] >= 5:
            a6[i,j] = 5
                
for i in range(0,30):
    for j in range(0,30):
        if a6[i,j] >= 1:
            a7[i,j] = a6[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a7[(i+1),j] = a6[(i+1),j]+1
            if r ==2:
                a7[i,(j+1)] = a6[i,(j+1)]+1
            if r ==3:
                a7[(i-1),j] = a6[(i-1),j]+1
            if r ==4:
                a7[i,(j-1)] = a6[i,(j-1)]+1
            if r ==5:
                a7[(i-1),j] = a6[(i-1),j]+1
            if r ==6:
                a7[(i+1),j] = a6[(i+1),j]+1
                a7[(i-1),j] = a6[(i-1),j]+1
            if r==7:
                a7[(i-1),j] = a6[(i-1),j]+1
                a7[i,(j-1)] = a6[i,(j-1)]+1
            if r==7:
                a7[(i+1),j] = a6[(i+1),j]+1
                a7[i,(j+1)] = a6[i,(j+1)]+1
            if r==8:
                a7[(i+1),j] = a6[(i+1),j]+1
                a7[i,(j-1)] = a6[i,(j-1)]+1
            if r==9:
                a7[i,(j+1)] = a6[i,(j+1)]+1
                a7[(i-1),j] = a6[(i-1),j]+1
            if r==10:
                a7[(i+1),j] = a6[(i+1),j]+1
                a7[(i+2),j] = a6[(i+2),j]+1
                a7[(i-1),j] = a6[(i-1),j]+1
                a7[(i-2),j] = a6[(i-2),j]+1
                a7[i,(j+1)] = a6[i,(j+1)]+1
                a7[i,(j+2)] = a6[i,(j+2)]+1
                a7[i,(j-1)] = a6[i,(j-1)]+1
                a7[i,(j-2)] = a6[i,(j-2)]+1
for i in range(0,30):
    for j in range(0,30):
        if a7[i,j] >= 5:
            a7[i,j] = 5

for i in range(0,30):
    for j in range(0,30):
        if a7[i,j] >= 1:
            a8[i,j] = a7[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a8[(i+1),j] = a7[(i+1),j]+1
            if r ==2:
                a8[i,(j+1)] = a7[i,(j+1)]+1
            if r ==3:
                a8[(i-1),j] = a7[(i-1),j]+1
            if r ==4:
                a8[i,(j-1)] = a7[i,(j-1)]+1
            if r ==5:
                a8[(i-1),j] = a7[(i-1),j]+1
            if r ==6:
                a8[(i+1),j] = a7[(i+1),j]+1
                a8[(i-1),j] = a7[(i-1),j]+1
            if r==7:
                a8[(i-1),j] = a7[(i-1),j]+1
                a8[i,(j-1)] = a7[i,(j-1)]+1
            if r==7:
                a8[(i+1),j] = a7[(i+1),j]+1
                a8[i,(j+1)] = a7[i,(j+1)]+1
            if r==8:
                a8[(i+1),j] = a7[(i+1),j]+1
                a8[i,(j-1)] = a7[i,(j-1)]+1
            if r==9:
                a8[i,(j+1)] = a7[i,(j+1)]+1
                a8[(i-1),j] = a7[(i-1),j]+1
            if r==10:
                a8[(i+1),j] = a7[(i+1),j]+1
                a8[(i+2),j] = a7[(i+2),j]+1
                a8[(i-1),j] = a7[(i-1),j]+1
                a8[(i-2),j] = a7[(i-2),j]+1
                a8[i,(j+1)] = a7[i,(j+1)]+1
                a8[i,(j+2)] = a7[i,(j+2)]+1
                a8[i,(j-1)] = a7[i,(j-1)]+1
                a8[i,(j-2)] = a7[i,(j-2)]+1
for i in range(0,30):
    for j in range(0,30):
        if a8[i,j] >= 5:
            a8[i,j] = 5

for i in range(0,30):
    for j in range(0,30):
        if a8[i,j] >= 1:
            a9[i,j] = a8[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a9[(i+1),j] = a8[(i+1),j]+1
            if r ==2:
                a9[i,(j+1)] = a8[i,(j+1)]+1
            if r ==3:
                a9[(i-1),j] = a8[(i-1),j]+1
            if r ==4:
                a9[i,(j-1)] = a8[i,(j-1)]+1
            if r ==5:
                a9[(i-1),j] = a8[(i-1),j]+1
            if r ==6:
                a9[(i+1),j] = a8[(i+1),j]+1
                a9[(i-1),j] = a8[(i-1),j]+1
            if r==7:
                a9[(i-1),j] = a8[(i-1),j]+1
                a9[i,(j-1)] = a8[i,(j-1)]+1
            if r==7:
                a9[(i+1),j] = a8[(i+1),j]+1
                a9[i,(j+1)] = a8[i,(j+1)]+1
            if r==8:
                a9[(i+1),j] = a8[(i+1),j]+1
                a9[i,(j-1)] = a8[i,(j-1)]+1
            if r==9:
                a9[i,(j+1)] = a8[i,(j+1)]+1
                a9[(i-1),j] = a8[(i-1),j]+1
            if r==10:
                a9[(i+1),j] = a8[(i+1),j]+1
                a9[(i+2),j] = a8[(i+2),j]+1
                a9[(i-1),j] = a8[(i-1),j]+1
                a9[(i-2),j] = a8[(i-2),j]+1
                a9[i,(j+1)] = a8[i,(j+1)]+1
                a9[i,(j+2)] = a8[i,(j+2)]+1
                a9[i,(j-1)] = a8[i,(j-1)]+1
                a9[i,(j-2)] = a8[i,(j-2)]+1
for i in range(0,30):
    for j in range(0,30):
        if a9[i,j] >= 5:
            a9[i,j] = 5

for i in range(0,30):
    for j in range(0,30):
        if a9[i,j] >= 1:
            a10[i,j] = a9[i,j]            
            r=random.randint(1,10)
            if r ==1:
                a10[(i+1),j] = a9[(i+1),j]+1
            if r ==2:
                a10[i,(j+1)] = a9[i,(j+1)]+1
            if r ==3:
                a10[(i-1),j] = a9[(i-1),j]+1
            if r ==4:
                a10[i,(j-1)] = a9[i,(j-1)]+1
            if r ==5:
                a10[(i-1),j] = a9[(i-1),j]+1
            if r ==6:
                a10[(i+1),j] = a9[(i+1),j]+1
                a10[(i-1),j] = a9[(i-1),j]+1
            if r==7:
                a10[(i-1),j] = a9[(i-1),j]+1
                a10[i,(j-1)] = a9[i,(j-1)]+1
            if r==7:
                a10[(i+1),j] = a9[(i+1),j]+1
                a10[i,(j+1)] = a9[i,(j+1)]+1
            if r==8:
                a10[(i+1),j] = a9[(i+1),j]+1
                a10[i,(j-1)] = a9[i,(j-1)]+1
            if r==9:
                a10[i,(j+1)] = a9[i,(j+1)]+1
                a10[(i-1),j] = a9[(i-1),j]+1
            if r==10:
                a10[(i+1),j] = a9[(i+1),j]+1
                a10[(i+2),j] = a9[(i+2),j]+1
                a10[(i-1),j] = a9[(i-1),j]+1
                a10[(i-2),j] = a9[(i-2),j]+1
                a10[i,(j+1)] = a9[i,(j+1)]+1
                a10[i,(j+2)] = a9[i,(j+2)]+1
                a10[i,(j-1)] = a9[i,(j-1)]+1
                a10[i,(j-2)] = a9[i,(j-2)]+1
for i in range(0,30):
    for j in range(0,30):
        if a10[i,j] >= 5:
            a10[i,j] = 5

plt.imsave('a0.png', a0, cmap='gray')
plt.imsave('a1.png', a1, cmap='gray')
plt.imsave('a2.png', a2, cmap='gray')
plt.imsave('a3.png', a3, cmap='gray')
plt.imsave('a4.png', a4, cmap='gray')
plt.imsave('a5.png', a5, cmap='gray')
plt.imsave('a6.png', a6, cmap='gray')
plt.imsave('a7.png', a7, cmap='gray')
plt.imsave('a8.png', a8, cmap='gray')
plt.imsave('a9.png', a9, cmap='gray')
plt.imsave('a10.png', a10, cmap='gray')

#spravit lepsie rozlisenie by sa dalo vynasobenim matice napr. na dvojnasobok riadkov a stlpcov 
#ak hladas gifko tak je mi luto robil som ho mimo tohoto lebo som nemal prave v case najlepsej nalady nervy na instalovanie dalsej kniznice - ak to vadi mozem sa na to pozret este

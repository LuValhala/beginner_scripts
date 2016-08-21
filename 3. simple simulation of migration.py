"""
This script is simulating the migration of birds. It was also needed for a school subject (programming 1).
It uses the matplotlib library to catch every move of the randomly moving bird and print it on a plot.
Script then proceeds to save those plots as images.
Ľuboš Valčo, november 2015
"""

import random
import matplotlib.pyplot as plt
x=0
y=0

for i in range(1,11):
  o = random.randrange(1,100)
  if o > 20:
    x=x
    y=y+32
    plt.scatter(x, y, c="blue")
  if (20<=o<=50): 
    z = random.randrange(1,32)
    x = x +(32 - z)
    y = y + z
    plt.scatter(x, y, c="blue")
  if (50<o<70):
    x=x+32
    y=y
    plt.scatter(x, y, c="blue")
  if (70<=o<=100):
    x=x
    y=y-32
    plt.scatter(x, y, c="blue")  
  plt.savefig("tura%i.png" %i)
  
if x >= 98 and y >= 98:
  print "jo"
else:
  print "nie"
print plt

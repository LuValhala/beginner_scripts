# -*- coding: utf-8 -*-
"""
This was the final challange in our school programming course(subject) or rather final exam.
Our only input was empty screen, no internet connection and a diagram with the inputs and outputs 
of a recursive function to sort a list of numbers originaly called as "Merge-sort"
So this whole recursion works with upper(horny) and lower(dolny) index of the inputted list(data).
Keeps on splitting the list until there is only one object of the list at the time and starts merging them
based on whichever is smaller. Continues with larger and larger lists allways comparing only two values which smaller 
is allways added to new list. This process is much faster than comparing each numbers with eachother.
Lists can contain duplicates, negatives and decimals.
Ľuboš Valčo, june 2016
"""
#na zaklade vstupnych indexov rekurzivne zoradit zoznam:
#najprv rozdelit napoly az dokym nezostanu jednotlive objekty zoznamu
#spajat postupne ale vzdy iba po dva co je rychlejsie a setri pamat
def merg( data, dolny, horny ):
  dolny_horny = ( dolny + horny ) // 2
  horny_dolny = dolny_horny + 1
  if dolny < horny:
    merg( data, dolny, dolny_horny )
    merg( data, horny_dolny, horny )
  d = dolny
  hd = horny_dolny
  listt = [None] * ( horny - dolny + 1 )
  index = 0
  while d <= dolny_horny and hd <= horny:
    if data[d] < data[hd] :
      listt[index] = data[d]
      d += 1
    else:
      listt[index] = data[hd]
      hd += 1
    index += 1
  if d <= dolny_horny :
    listt[index:] = data[d:horny_dolny]
  if hd <= horny:
    listt[index:] = data[hd:horny + 1]
  index = 0
  while dolny <= horny:
    data[dolny] = listt[index]
    dolny += 1
    index += 1
k = [1,6,8,5,36,71,26,6,1,568,2]
print (k)
merg(k, 0, len(k)-1)
print (k)

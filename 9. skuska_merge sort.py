# -*- coding: utf-8 -*-
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
"""
Basic text game created as my first ever "file.py". 
Pressing the right keys in console input will lead you to the end of the game.
This text game was created for school subject and is completely in slovak language.
Variables in this file are quite random, but were used to hold the cycle before the "key to open the door" was found. 
After that is achieved, you can continue through the game.
Ľuboš Valčo, october 2014
"""
print "Zobudil som sa s prazdnou flasou tatranskeho caju 72% v ruke a som v nejakej novej budove. Chcem sa odtial dostat a zistit co sa stalo"
q = 0
while q == 0:
  x = input("Vstal som a mam na vyber ist: (1)vlavo (2)dopredu (3)vpravo (napis cislo pre postup) \n")
  if x == 3:
    print "Presunul som sa na chodbu"
    q = 1
  if x == 2:
    print "Narazil som do steny"
    q = 0
  if x == 1:
    print "Hmm nic tam neni"
    q = 0

q = 0
while q == 0:
  x = input("Je tu tma iba pred sebou vidim trochu svetla (1)vlavo (2)dopredu (3)vpravo \n")
  if x == 2:
    print "prisiel si k presklennemu vyhladu na bratislavu a zamyslel si sa"
    q = 1
  else:
    print "nic nevidis a vracias sa"
    q = 0

q = 0
print "Takze som sa spil jak delo a nepamatam si ako som sa sem dostal...som v novej budove Prirodovedeckej fakulty!"
while q == 0:
  x = input("Nemam ani penazenku ani mobil...(1)vlavo (2)dopredu (3)vpravo \n")
  if x == 1:
    print "Pokracujem do hlavnej haly"
    q = 1
  if x == 2:
    print "Okno je zamknute"
    q = 0
  if x == 3:
    print "Hmm tu nic nie je"
    q = 0

z = 0
w = 0
u = 0
o = 0
q = 0
c = 0
print "Je tu nejaky stavebny material a co nevidim! na zemi je taka ista flasa tatranskeho caju ako som mal v ruke. Musi tu byt nieco! su tu viacere miestnosti, mozno tie mi pomozu"
while q == 0:
  x = input("Som v hlavnej hale, do ktorej miestnosti pojdem? 1 2 3 4 \n")
  if x == 1:
    print "V tejto miestnosti je prednaskova sien A"
    q = 0
  if x == 2:
    print "V tejto miestnosti je prednaskova sien B"
  if x == 4:
    if o == 0:
      print "Zachody su nove no otacam sa hned pri vchode bez hlbsieho skumania naspat" 
      q = 0
    if o == 1:
      q = 1
  if x == 3:
    if u == 0:
      print "V tejto mensej miestnosti su znamky ze som tu bol."
      while z == 0:
        x = input("Fuf dost tu fuci prievan. Su tu nejake veci na stole(1) kopa prikryta plachtou(2) a nejaky batoh(3) co skusim? \n")
        if x == 3:
          print "V batohu je mikina, malovatka, ruz, kondomy, neznamy telefon a nedopita flasa borovicky"
        if x == 2:
          print "Nepride mi zaujimava, vyzera ako keby robotnici odlozili svoje pristroje pod plachtu aby na ne nefukalo"
        if x == 1:
          print "Na stole su styri penazenky a tri mobily, jeden z nich je moj!"
          while c == 0:
            print "Beriem do ruky mobil a skusim niekomu zavolat"
            x = input("Zavolam 1-Adrianovi 2-Ivane 3-Marekovi 4-Lukasovi 5-Julii 6-Daniele 7-Kristine...iba tito mozu vediet co sa stalo \n")
            if x == 1:
              print "Nespravne cislo?"
              c = 0
            if x == 2:
              print "Zvonim,...zvonim...nezdviha"
              c = 0
            if x == 3:
              print "Cislo ktore volate je momentalne nedostupne"
              c = 0
            if x == 4:
              print "Zvonim,...zvonim,...zvonim,...dochadza mi baterka? polozit..."
              c = 0
            if x == 5:
              print "Zazvonil telefon z batohu! co ale vyvolalo myknutie niecoho pod plachtou"
              while w == 0:
                x = input("Plachta sa pohla...zeby?? (1-prieskum plachty) (2-zdesenie a nechapave pozeranie na hmyriacu sa prikrytu kopku) \n")
                if x == 1:
                  print "Zhodil som plachtu a pod nou boli ku podivu moji zaspati kamosi Marek a Julia, klepali sa od zimy, v spolocnom objati prikryti plachtou proti prievanu!"
                  w = 1
                  c = 1
                  z = 1
                  o = 1
                  u = 1
                  print "Marek a Julia maju lepsiu pamat na to co sa stalo, ma s nami byt aj Kristina, vraj utekala na wc. Zeby som ju tam prehliadol?"
                else: 
                  print "Ukludnis sa"
                  w = 0
            if x == 6:
              print "Jej nechcem volat...je v zahranici"
              c = 0
            if x == 7:
              print "Tejto hnusobe nechcem volat, neznasa ma"
              c = 0
    if u == 1:
      print "Odtialto sme prisli"

print "tak som zobral celu partiu a odisli sme naspet cez otvorene okno vzadu v budove, nikomu sa na stastie nic nestalo len kika mala riadnu opicu. nikto nic nestratil len chudakovi marekovi padol mobil do zachoda ked sa snazil zachranit kiku"
print "ja som jej vraj chcel ist pomoct tiez nakolko julia nechcela byt vyhrievana mojim telom tak som hladal nahradu a stratil som sa... To co mala byt lahka oslava noveho skloskeho roku sa zvrhlo do pribehu na ktori nezabudneme (:D)"
print "Vytvoril: LUBOS VALCO (s mekcenmi nad prvym L, S, a C) 10.10.2015 pribeh je vymysleny"
#ponaucenie pre juliu? nemala miesat tatranak s pomstou z lesa...

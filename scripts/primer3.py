#! /usr/bin/python3
import time
from copy import copy, deepcopy

global spremenljivka #tako definiramo globalno spremenljivko - vrstico napiši tudi v funkciji
spremenljivka = 1
spr2 = True
spr3 = 0.4
spr4 = "Besedilo"
spr5 = 'Besedilo'
spr6 = b'f3a'
toJeSpremenljivka7 = 7

seznam = [0.4, 0.6, 6.3] # To je seznam - list
t = (4, 3, 7) # to je tuple
d = {"avto":"škoda", "ime":"Aleš", "Starost":32} # to je slovar - dictionary

print(seznam[2]) #tako se indeksira tuple in list
print(t[0])
print(d["ime"]) #tako se indeksira slovar


"""
To je večvrstični komentar


Tukaj si pogledamo kako se izpisuje vrednosti:
"""
print("Seznam na mestu 2: " + str(seznam[2]))
print("Seznam na mestu 2: " + repr(seznam[2]))
print(f"SEznam na mestu 2: {seznam[2]}, na mestu 1 pa : {seznam[1]}")

#tako se spremeni vrednosti v seznamih in slovarjih
seznam[0] = 30
d["Starost"] = 33

print(d)
print(seznam)

seznam.append(88)
seznam.insert(0, 66)
d["naslov"] ="Tržaška 25"

print(d)
print(seznam)

novseznam = seznam

novnovseznam = copy(seznam) # kopiramo objekt (samo prvi nivo)
novnovnovseznam = deepcopy(seznam) #kopiramo cel objekt !!!pozor, procesno zahtevno!!

x, y, z = t

_, _, x1, y1, _ = seznam

print(x, y, z)
print(x1, y1)

a = b = c = 66


def main():
    print("Hello world!")

if __name__ == "__main__":
    main()
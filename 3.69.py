"""Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt,
amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal
osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a
függvény hívását is!"""

def harommal_oszthatok(lista):

    harom = 0
    for i in lista:
        if i % 3 == 0:
           harom += 1
    return harom
lista = [6, 4, 3, 1, 12, 15]
print(harommal_oszthatok(lista))
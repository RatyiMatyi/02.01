"""Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt,
ami a paraméterként átvett listaelemeket (egész számokat) összeadja és
az összegükkel tér vissza! A program tartalmazza a függvény hívását is!"""


def osszegzo(lista):
    return sum(lista)


szamok = [1, 2, 3, 4, 5]

eredmeny = osszegzo(szamok)
print("Az összeg:", eredmeny)




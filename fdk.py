"""Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt,
amely True értékkel tér vissza, ha a paraméterként átvett listaelemek
(egész számok) között van páros, ellenkező esetben a visszatérési
érték False! A program tartalmazza a függvény hívását is"""

def paros_e(lista):
    paros = True
    for szam in lista:
        if szam % 2 != 0:
            paros = False
    return paros

lista = [4, 2, 4, 3, 2]

print(paros_e(lista))



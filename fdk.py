"""Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt,
amely True értékkel tér vissza, ha a paraméterként átvett listaelemek
(egész számok) között van páros, ellenkező esetben a visszatérési
érték False! A program tartalmazza a függvény hívását is"""

def paros_e(lista):
    paros = False
    for szam in lista:
        if szam % 2 == 0:
            paros = True
    return paros

lista = [1, 3, 5, 3, 1]

print(paros_e(lista))



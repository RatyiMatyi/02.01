"""Alakítsd át az előző programot úgy, hogy a felhasználó által megadott
számokat tárolja el a program egy listában, és ezt értékelje ki a függvény!
(Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)"""

szamok = []
folytat = True
while folytat:
    szam = int(input("Adj meg egy pozitív számot"))
    if szam < 0:
        folytat = False
    else:
        szamok.append(szam)
print(szamok)


def harommal_oszthatok(lista):

    harom = 0
    for i in lista:
        if i % 3 == 0:
           harom += 1
    return harom
lista = szamok
print(harommal_oszthatok(lista))
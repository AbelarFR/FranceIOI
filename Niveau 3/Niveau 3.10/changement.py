#-------------------------------------------------------------------------------
# Name:        Changement de base
# Purpose:     France-IOI niveau 3.10
#
# Author:      Sébastien
#
# Created:     16/10/2022
#-------------------------------------------------------------------------------

# Convertit un nombre décimal en une liste de chiffres dans la base d'arrivée
def convertir(n, base):
    chiffres = []
    if n >= base:
        chiffres = convertir(n//base, base)
    chiffres.append(n % base)
    return chiffres

# Convertit une liste de chiffres dans la base de départ en un nombre décimal
def decimal(chiffres, base):
    n = 0
    for c in chiffres:
        n = base*n + c
    return n

if __name__ == '__main__':
    b1, b2, _ = map(int, input().split())
    chiffres = list(map(int, input().split()))
    n = decimal(chiffres, b1)
    chiffres = convertir(n, b2)
    print(" ".join(map(str, chiffres)))

"""
10 2 2
4 2
---
100 10 3
2 20 3
"""
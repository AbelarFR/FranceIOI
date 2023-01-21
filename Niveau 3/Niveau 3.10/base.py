#-------------------------------------------------------------------------------
# Name:        Écriture dans une base quelconque
# Purpose:     France-IOI niveau 3.10
#
# Author:      Sébastien
#
# Created:     16/10/2022
#-------------------------------------------------------------------------------

def convertir(n, base):
    chiffres = []
    if n >= base:
        chiffres = convertir(n//base, base)
    chiffres.append(n % base)
    return chiffres

if __name__ == '__main__':
    n, base = map(int, input().split())
    chiffres = convertir(n, base)
    print(len(chiffres))
    print(" ".join(map(str, chiffres)))

"""
1234 100
---
254 16
---
29 3
"""
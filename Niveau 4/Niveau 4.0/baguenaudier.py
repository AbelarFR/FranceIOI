#-------------------------------------------------------------------------------
# Name:        Baguenaudier
# Purpose:     France-IOI niveau 4.0
#
# Author:      Sébastien
#
# Created:     19/11/2022
#-------------------------------------------------------------------------------

import time

def modifier(cases, k, valeur):
    if k > 1:
        remplir(cases, k-1)
    if k > 2:
        for i in range(k-2, 0, -1):
            vider(cases, i)
    cases[k] = valeur
    print(k)

def vider(cases, k):
    if cases[k]: modifier(cases, k, False)

def remplir(cases, k):
    if not cases[k]: modifier(cases, k, True)

def main():
    n = int(input())
    cases = [True]*(n+1)
    for k in range(n, 0, -1):
        vider(cases, k)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
##  print("Temps d'exécution :", end-start, "ms")

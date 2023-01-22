#-------------------------------------------------------------------------------
# Name:        Longueur des descriptions
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     22/01/2023
#-------------------------------------------------------------------------------

import time

def calculerLongueurChemin(objets, i):
    if objets[i] == 0:
        return 1
    else:
        return 1 + calculerLongueurChemin(objets, objets[i]-1)

def main():
    nbObjets = int(input())
    objets = list(map(int, input().split()))

    lMax = 0
    for i in range(nbObjets):
        l = calculerLongueurChemin(objets, i)
        if l > lMax : lMax = l

    print(lMax)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
##  print("Temps d'exécution :", end-start, "ms")

"""
8
3 3 7 3 6 7 0 0
"""
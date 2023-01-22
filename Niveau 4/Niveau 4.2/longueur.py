#-------------------------------------------------------------------------------
# Name:        Longueur des descriptions
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     22/01/2023
#-------------------------------------------------------------------------------

import time

def main():
    nbObjets = int(input())
    contenants = list(map(int, input().split()))

    encore = True
    longueurs = [1]*nbObjets
    while encore:
        encore = False
        for i in range(nbObjets):
            if contenants[i] > 0:
                longueurs[i] += longueurs[contenants[i]-1]
                contenants[i] = contenants[contenants[i]-1]
                encore = True

    print(max(longueurs))

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Temps d'exécution :", end-start, "ms")

"""
8
3 3 7 3 6 7 0 0
---
4
0 1 2 3
---
5
2 3 4 5 0
"""
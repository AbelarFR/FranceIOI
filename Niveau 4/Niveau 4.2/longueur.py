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

    lMax = 0
    encore = True
    while encore:
        encore = False
        contenants2 = [0]*nbObjets
        for i in range(nbObjets):
            if contenants[i] > 0:
                if contenants[contenants[i]-1] > 0:
                    contenants2[i] = contenants[i]
                encore = True
        lMax += 1
        contenants = contenants2

    print(lMax)

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
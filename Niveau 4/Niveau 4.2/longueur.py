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
    objets = list(map(int, input().split()))

    lMax = 0
    for i in range(nbObjets):
        l = 1
        contenant = objets[i]
        while contenant > 0:
            l += 1
            contenant = objets[contenant-1]
        if l > lMax : lMax = l

    print(lMax)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Temps d'exécution :", end-start, "ms")

"""
8
3 3 7 3 6 7 0 0
"""
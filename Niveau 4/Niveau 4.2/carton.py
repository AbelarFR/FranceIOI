#-------------------------------------------------------------------------------
# Name:        Carton commun
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     26/01/2023
#-------------------------------------------------------------------------------

import time

def listerPeres(contenants, objet):
    liste = [objet]
    pere = objet
    while pere > 0:
        pere = contenants[pere]
        liste.insert(0, pere)
    return liste

def main():
    nbObjets = int(input())
    contenants = [0] + list(map(int, input().split()))

    nbRecherches = int(input())
    for n in range(nbRecherches):
        objet1, objet2 = map(int, input().split())
        peres1 = listerPeres(contenants, objet1)
        peres2 = listerPeres(contenants, objet2)
        peres = zip(peres1, peres2)
        for i, p in enumerate(peres):
            if p[0] != p[1]:
                i -= 1
                break
        print(peres1[i])

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Temps d'exécution :", end-start, "ms")

"""
8
3 3 7 3 6 7 0 0
3
1 5
5 7
2 8
"""
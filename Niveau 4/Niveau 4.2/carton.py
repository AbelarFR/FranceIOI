#-------------------------------------------------------------------------------
# Name:        Carton commun
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     26/01/2023
#-------------------------------------------------------------------------------

import time

def main():
    nbObjets = int(input())
    contenants = [0] + list(map(int, input().split()))

    nbRecherches = int(input())
    for n in range(nbRecherches):
        objet1, objet2 = map(int, input().split())

        trace = [False]*(nbObjets+1)
        noeud = objet1
        trace[noeud] = True
        while noeud > 0:
            noeud = contenants[noeud]
            trace[noeud] = True

        noeud = objet2
        while not trace[noeud]:
            noeud = contenants[noeud]

        print(noeud)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Temps d'exécution :", end-start, "s")

"""
8
3 3 7 3 6 7 0 0
3
1 5
5 7
2 8
"""
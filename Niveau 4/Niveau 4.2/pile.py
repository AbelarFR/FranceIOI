#-------------------------------------------------------------------------------
# Name:        Pile de cartons
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     27/01/2023
#-------------------------------------------------------------------------------

import time

def afficherChemin(arbre, noeud):
    for fils in arbre[noeud]:
        print('A', fils)
        afficherChemin(arbre, fils)
        print('R', fils)

def main():
    nbNoeuds = int(input())
    arbre = [None]*(nbNoeuds+1)
    for noeud in range(nbNoeuds+1):
        fils = list(map(int, input().split()))
        arbre[noeud] = fils[1:]

    afficherChemin(arbre, 0)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
##    print("Temps d'exécution :", end-start, "ms")

"""
7
2 3 2
0
0
2 6 4
3 5 1 7
0
0
0
"""
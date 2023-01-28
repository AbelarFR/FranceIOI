#-------------------------------------------------------------------------------
# Name:        Anti-virus
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     28/01/2023
#-------------------------------------------------------------------------------

import time

def afficher(noeuds, masque):
    for n in noeuds:
        chaine = str(n)
        match = len(chaine) == len(masque)
        i = 0
        while match and i < len(chaine):
            match = masque[i] == '?' or masque[i] == chaine[i]
            i += 1
        if match:
            print(n, end=' ')

def main():
    # Crée l'arbre
    nbNoeuds = int(input())
    arbre = [[] for _ in range(nbNoeuds+1)]
    for fils, pere in enumerate(map(int, input().split()), 1):
        arbre[pere].append(fils)
    masque = input()

    # Affiche les fils niveau par niveau
    peres = [0]
    while peres:
        fils = []
        for noeud in peres:
            fils += arbre[noeud]
        afficher(fils, masque)
        peres = fils
    print()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Temps d'exécution :", end-start, "s")

"""
8
3 3 7 3 6 7 0 0
?
---
12
0 0 1 1 2 2 2 3 3 3 4 4
1?
"""
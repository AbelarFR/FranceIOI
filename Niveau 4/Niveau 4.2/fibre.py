#-------------------------------------------------------------------------------
# Name:        Fibre optique
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     28/01/2023
#-------------------------------------------------------------------------------

import time

def explorer(arbre, dejaVu, noeud, compteur):
    for voisin in arbre[noeud]:
        if not dejaVu[voisin]:
            dejaVu[voisin] = True
            compteur += 1
            compteur = explorer(arbre, dejaVu, voisin, compteur)
    return compteur

def main():
    # Crée l'arbre
    nbNoeuds = int(input())
    voisins = [[] for _ in range(nbNoeuds)]
    for _ in range(nbNoeuds-1):
        noeud1, noeud2 = map(int, input().split())
        voisins[noeud1].append(noeud2)
        voisins[noeud2].append(noeud1)

    resultat = nbNoeuds
    for noeud in range(nbNoeuds):
        dejaVu = [False]*nbNoeuds
        dejaVu[noeud] = True
        tailleBrancheMax = 0
        # Compte le nombre de noeuds dans branche de chaque noeud
        for voisin in voisins[noeud]:
            dejaVu[voisin] = True
            tailleBranche = explorer(voisins, dejaVu, voisin, 1)
            if tailleBrancheMax < tailleBranche:
                tailleBrancheMax = tailleBranche
        if resultat > tailleBrancheMax:
            resultat = tailleBrancheMax
    print(resultat)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Temps d'exécution :", end-start, "s")

"""
10
1 8
3 4
8 3
2 3
2 6
7 6
5 6
5 9
6 0
"""
#-------------------------------------------------------------------------------
# Name:        Fibre optique
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     28/01/2023
#-------------------------------------------------------------------------------

import time

# Variables globales
resultat = 0

# Compte le nombre de PC dans chaque branche qui part de 'noeud'
# et retient le maximum.
# Retourne le nombre de PC dans la branche dont 'noeud' est la racine.
def compter(arbre, pere, noeud):
    global resultat
    compteur = 1
    tailleBrancheMax = 0
    for voisin in arbre[noeud]:
        if voisin != pere:
            tailleBranche = compter(arbre, noeud, voisin)
            if tailleBrancheMax < tailleBranche:
                tailleBrancheMax = tailleBranche
            compteur += tailleBranche
    if tailleBrancheMax < len(arbre) - compteur:
        tailleBrancheMax = len(arbre) - compteur
    if resultat > tailleBrancheMax:
        resultat = tailleBrancheMax
    return compteur

def main():
    global resultat
    # Crée l'arbre
    nbNoeuds = int(input())
    voisins = [[] for _ in range(nbNoeuds)]
    for _ in range(nbNoeuds-1):
        noeud1, noeud2 = map(int, input().split())
        voisins[noeud1].append(noeud2)
        voisins[noeud2].append(noeud1)

    resultat = nbNoeuds
    _ = compter(voisins, -1, 0)
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
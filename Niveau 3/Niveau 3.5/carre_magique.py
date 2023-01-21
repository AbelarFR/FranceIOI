#-------------------------------------------------------------------------------
# Name:        Carré magique
# Purpose:     France-IOI niveau 3.5
#
# Author:      Sébastien
#
# Created:     17/09/2022
#-------------------------------------------------------------------------------

def main():
    n = int(input())
    tableau = [[int(c) for c in input().split()] for _ in range(n)]

    somme = sum(tableau[0])
##    print(somme)

    # Vérifie que chaque nombre est présent une seule fois
    magique = True
    present = [False]*(n*n)
    for ligne in tableau:
        for val in ligne:
            if val <= 0 or val > n*n or present[val-1]:
                magique = False
##              print(val, "présent plusieurs fois")
                break
            else:
                present[val-1] = True

    # Vérifie la somme de chaque ligne
    if magique:
        for ligne in tableau[1:]:
            if sum(ligne) != somme:
                magique = False
##              print("somme d'une ligne différente")
                break

    # Vérifie la somme de chaque colonne
    if magique:
        for c in range(n):
            s = 0
            for l in range(n):
                s += tableau[l][c]
            if s != somme:
                magique = False
##              print("somme de la colonne", c, "différente")
                break

    # Vérifie la somme de la première diagonale
    if magique:
        s = 0
        for i in range(n):
            s += tableau[i][i]
        if s != somme:
##          print("somme de la première diagonale différente")
            magique = False

    # Vérifie la somme de la seconde diagonale
    if magique:
        s = 0
        for i in range(n):
            s += tableau[i][n-i-1]
        if s != somme:
##          print("somme de la seconde diagonale différente")
            magique = False

    if magique:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()

"""
3
6 1 8
7 5 3
2 9 4
"""
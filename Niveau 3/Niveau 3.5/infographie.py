#-------------------------------------------------------------------------------
# Name:        Infographie
# Purpose:     France-IOI niveau 3.5
#
# Author:      Sébastien
#
# Created:     17/09/2022
#-------------------------------------------------------------------------------

def main():
    # Initialise l'image
    nbLignes, nbColonnes = map(int, input().split())
    output = [['.']*nbColonnes for _ in range(nbLignes)]

    # Ajoute chaque rectangle
    nbRectangles = int(input())
    for _ in range(nbRectangles):
        rectangle = input().split()
        iLig1 = int(rectangle[0])
        iCol1 = int(rectangle[1])
        iLig2 = int(rectangle[2])
        iCol2 = int(rectangle[3])
        couleur = rectangle[4]

        for l in range(iLig1, iLig2+1):
            for c in range(iCol1, iCol2+1):
             output[l][c] = couleur

    # Affiche l'image finale
    for ligne in output:
        print("".join(ligne))

if __name__ == '__main__':
    main()

"""
9 19
4
1 3 7 5 o
5 2 6 16 -
1 12 7 14 u
2 1 2 16 s
"""
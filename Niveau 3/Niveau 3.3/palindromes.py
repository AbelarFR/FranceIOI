#-------------------------------------------------------------------------------
# Name:        Titres palindromiques
# Purpose:     France-IOI niveau 3.3
#
# Author:      Sébastien
#
# Created:     12/09/2022
#-------------------------------------------------------------------------------

nbLivres = int(input())

for loop in range(nbLivres):
    titre = input()
    titre_maj = "".join(titre.upper().split()) # Ignore les espaces et la casse

    est_palindrome = True
    for i in range(len(titre_maj) // 2):
        if (titre_maj[i] != titre_maj[len(titre_maj) - i - 1]):
            est_palindrome = False
            break

    if est_palindrome:
        print(titre)

"""
3
Lieur a Rueil
Le chevalier delibere
Un roc si biscornu
"""
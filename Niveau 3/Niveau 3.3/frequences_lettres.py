#-------------------------------------------------------------------------------
# Name:        Fréquences d’apparition
# Purpose:     France-IOI niveau 3.3
#
# Author:      Sébastien
#
# Created:     13/09/2022
#-------------------------------------------------------------------------------

texte = input().upper()

compteurs = [0] * 26
nbLettres = 0
for lettre in texte:
    if lettre.isalpha():
        compteurs[ord(lettre) - ord('A')] += 1
        nbLettres += 1

for compteur in compteurs:
    print(compteur/nbLettres)
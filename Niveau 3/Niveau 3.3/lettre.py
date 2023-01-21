#-------------------------------------------------------------------------------
# Name:        Lettre la plus fréquente
# Purpose:     France-IOI niveau 3.3
#
# Author:      Sébastien
#
# Created:     12/09/2022
#-------------------------------------------------------------------------------

texte = input().upper()

compteurs = [0] * 26
for lettre in texte:
    if lettre != ' ':
        compteurs[ord(lettre) - ord('A')] += 1

maxi = max(compteurs)
for i, valeur in enumerate(compteurs):
    if valeur == maxi: break

print(chr(i + ord('A')))
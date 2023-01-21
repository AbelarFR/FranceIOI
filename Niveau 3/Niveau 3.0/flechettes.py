#-------------------------------------------------------------------------------
# Name:        Fléchettes
# Purpose:     France-IOI niveau 3.0
#
# Author:      Sébastien
#
# Created:     08/09/2022
#-------------------------------------------------------------------------------

nbLettres = int(input())
taille = 2*nbLettres-1
for ligne in range(taille):
    for colonne in range(taille):
        if ligne + colonne < taille:
            print(chr(ord('a') + min(ligne, colonne)), end='')
        else:
            print(chr(ord('a') + min(taille-ligne-1, taille-colonne-1)), end='')
    print()

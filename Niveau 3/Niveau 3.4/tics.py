#-------------------------------------------------------------------------------
# Name:        Conférence et tics de langage
# Purpose:     France-IOI niveau 3.4
#
# Author:      Sébastien
#
# Created:     14/09/2022
#-------------------------------------------------------------------------------

mot = input().lower()
discours = input().lower().split()
nombre = 0
for m in discours:
    if m == mot:
        nombre += 1
print(nombre)

"""
heu
Je pense heu que heu ce livre est heu le meilleur que j ai ecrit heu depuis heu cinq ans Heu vous avez des questions
"""
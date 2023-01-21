#-------------------------------------------------------------------------------
# Name:        Composition musicale
# Purpose:     France-IOI niveau 3.0
#
# Author:      Sébastien
#
# Created:     09/09/2022
#-------------------------------------------------------------------------------

"""
morceau = input()
suite = True

while(suite):
    suite = False
    for note in range(len(morceau)-1):
        if morceau[note] == morceau[note+1]:
            morceau = morceau[:note]+morceau[note+2:]
            suite = True
            break

print(morceau)
"""

entree = input()
sortie = ""

for note in range(len(entree)):
    if sortie != "" and sortie[-1] == entree[note]:
        sortie = sortie[:-1]
    else:
        sortie = sortie + entree[note]

print(sortie)


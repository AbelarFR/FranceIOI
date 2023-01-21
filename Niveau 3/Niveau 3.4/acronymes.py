#-------------------------------------------------------------------------------
# Name:        Acronymes
# Purpose:     France-IOI niveau 3.4
#
# Author:      Sébastien
#
# Created:     14/09/2022
#-------------------------------------------------------------------------------

acronyme = input()
nbLivres = int(input())

for _ in range(nbLivres):
    titre = [mot.capitalize() for mot in input().split()]
    initiales = []
    for mot in titre:
        initiales.append(mot[0])
    if "".join(initiales) == acronyme:
        print(" ".join(titre))

"""
PP
7
PEDro paramO
Poemes PALINDROMES
LA Condition HUMAINE
PERE et fils
petite
Promenade Au phare
peter pan
"""

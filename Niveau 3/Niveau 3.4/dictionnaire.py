#-------------------------------------------------------------------------------
# Name:        Inversion de dictionnaire
# Purpose:     France-IOI niveau 3.4
#
# Author:      Sébastien
#
# Created:     14/09/2022
#-------------------------------------------------------------------------------

nbMots = int(input())
dico = []
for loop in range(nbMots):
    mot1, mot2 = input().split()
    dico.append(mot2 + ' ' + mot1)

dico.sort()

for ligne in dico:
    print(ligne)

"""
2
travail work
verite truth
"""
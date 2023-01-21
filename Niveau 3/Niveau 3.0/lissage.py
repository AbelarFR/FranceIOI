#-------------------------------------------------------------------------------
# Name:        Lissage de signal
# Purpose:     France-IOI niveau 3.0
#
# Author:      Sébastien
#
# Created:     10/09/2022
#-------------------------------------------------------------------------------

def est_lisse(mesures):
    lisse = True
    for i in range(len(mesures)-1):
        if abs(mesures[i+1]-mesures[i]) > diffMax: lisse = False
    return lisse

# Lit les entrées
nbMesures = int(input())
diffMax = float(input())
mesures = []
for loop in range(nbMesures):
    mesures.append(float(input()))

n = 0
while not est_lisse(mesures):
    n = n + 1
    sortie = [mesures[0]]
    for i in range(1, nbMesures-1):
        sortie.append((mesures[i-1]+mesures[i+1])/2)
    sortie.append(mesures[-1])
    mesures = sortie

print(n)
"""
7
1.120
1.292
1.343
3.322
4.789
-0.782
7.313
4.212
"""
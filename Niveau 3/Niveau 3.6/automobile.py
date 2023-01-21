#-------------------------------------------------------------------------------
# Name:        Course automobile
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     19/09/2022
#-------------------------------------------------------------------------------

import sys

def main():
    nbAutomobiles = int(input())
    autos = list(map(int, sys.stdin.readline().split()))
    croisements = []

    for i in range(nbAutomobiles):
        # Cherche la voiture i+1 dans la liste
        j = i
        while j < nbAutomobiles and autos[j] != i+1:
            j += 1
        # Replace la voiture i+1 à sa position d'arrivée
        # en la décalant de proche en proche vers la gauche
        for k in range(j, i, -1):
            croisements.append((autos[k-1], autos[k]))
            autos[k], autos[k-1] = autos[k-1], autos[k]

    print(len(croisements))
    for c in croisements:
        print(c[0], c[1])

if __name__ == '__main__':
    main()

"""
4
2 1 4 3
"""
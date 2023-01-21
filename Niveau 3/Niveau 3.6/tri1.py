#-------------------------------------------------------------------------------
# Name:        Tri des données
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     20/09/2022
#-------------------------------------------------------------------------------

import sys

def tri_selection(valeurs):
    for nb_restant in range(len(valeurs), 0, -1):
        imax = 0
        for i in range(nb_restant):
            if valeurs[i] > valeurs[imax]:
                imax = i
        if imax < nb_restant-1:
            valeurs[imax], valeurs[nb_restant-1] = valeurs[nb_restant-1], valeurs[imax]


def tri_insertion(valeurs):
    for i in range(1, len(valeurs)):
        valeur = valeurs[i]
        j = i
        while j > 0 and valeur < valeurs[j-1]:
            valeurs[j] = valeurs[j-1]
            j -= 1
        valeurs[j] = valeur



def tri_bulle(valeurs):
    for _ in range(len(valeurs)):
        for i in range(len(valeurs)-1):
            if valeurs[i] > valeurs[i+1]:
                valeurs[i], valeurs[i+1] = valeurs[i+1], valeurs[i]


def main():
    n = int(input())
    polluants = list(map(int, sys.stdin.readline().split()))

    tri_insertion(polluants)

    print(" ".join(map(str, polluants)))

if __name__ == '__main__':
    main()

"""
6
3 2 17 0 10 3
"""
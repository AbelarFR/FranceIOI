#-------------------------------------------------------------------------------
# Name:        Densité la plus proche
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     24/09/2022
#-------------------------------------------------------------------------------

import sys

def rechercher(liste, valeur):
    debut = 0
    fin = len(liste) - 1
    while debut < fin:
        m1 = (debut + fin) // 2
        m2 = m1 + 1
        if valeur > liste[m2]:
            debut = m2
        elif valeur < liste[m1]:
            fin = m1
        elif valeur - liste[m1] <= liste[m2] - valeur :
            return liste[m1]
        else:
            return liste[m2]
    return liste[debut]

def main():
    n = int(input())
    densites = list(map(int, sys.stdin.readline().split()))
    densites.sort()

    q = int(input())
    for _ in range(q):
        densite = int(sys.stdin.readline())
        print(rechercher(densites, densite))

if __name__ == '__main__':
    main()

"""
7
41 32 11 17 24 8 16
4
9
20
28
11
"""

#-------------------------------------------------------------------------------
# Name:        Densité du plastique
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     22/09/2022
#-------------------------------------------------------------------------------

import sys

def rechercher(liste, valeur):
    debut = 0
    fin = len(liste) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if valeur > liste[milieu]:
            debut = milieu + 1
        elif valeur < liste[milieu]:
            fin = milieu - 1
        else:
            return 1
    return 0

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
1 3 6 7 9 11 20
9
0
1
2
3
10
11
12
20
21
"""
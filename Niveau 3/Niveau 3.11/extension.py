#-------------------------------------------------------------------------------
# Name:        Extension du centre
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     19/10/2022
#-------------------------------------------------------------------------------

import sys

def main():
    na = int(sys.stdin.readline())
    liste_a = list(map(int, sys.stdin.readline().split()))
    nb = int(sys.stdin.readline())
    liste_b = list(map(int, sys.stdin.readline().split()))

    a = 0
    b = 0

    while (a < na and b < nb):
        if liste_a[a] <= liste_b[b]:
            print(liste_a[a], end=' ')
            a += 1
        else:
            print(liste_b[b], end=' ')
            b += 1

    while (a < na):
        print(liste_a[a], end=' ')
        a += 1

    while (b < nb):
        print(liste_b[b], end=' ')
        b += 1

if __name__ == '__main__':
    main()

"""
6
0 2 3 3 10 17
4
2 16 17 22
---
4
1 2 3 4
4
1 2 3 4
"""

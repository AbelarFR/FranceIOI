#-------------------------------------------------------------------------------
# Name:        Tri des données (bibliothèque)
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     21/09/2022
#-------------------------------------------------------------------------------

import sys

def main():
    n = int(input())
    valeurs = list(map(int, sys.stdin.readline().split()))
    valeurs.sort()
    print(" ".join(map(str, valeurs)))

if __name__ == '__main__':
    main()

"""
6
-127 3 -8 7 25 18
"""
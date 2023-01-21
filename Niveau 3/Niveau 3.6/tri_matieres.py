#-------------------------------------------------------------------------------
# Name:        Matières recyclables
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     22/09/2022
#-------------------------------------------------------------------------------

import sys

def main():
    n = int(input())
    noms = [input() for _ in range(n)]
    noms.sort()
    for nom in noms:
        print(nom)


if __name__ == '__main__':
    main()

"""
6
papier
carton
verre
carton
plastique
fer
"""
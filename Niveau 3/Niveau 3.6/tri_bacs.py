#-------------------------------------------------------------------------------
# Name:        Identifier les bacs
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     21/09/2022
#-------------------------------------------------------------------------------

import sys

def main():
    nbBacs = int(input())
    bacs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(nbBacs)]
    bacs.sort(key = lambda b:(b[1], b[0]))
    for bac in bacs:
        print(*bac)

if __name__ == '__main__':
    main()

"""
6
1 6
2 3
4 12
3 7
5 25
7 18
"""
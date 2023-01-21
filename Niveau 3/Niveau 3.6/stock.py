#-------------------------------------------------------------------------------
# Name:        Préparation du stock
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     19/09/2022
#-------------------------------------------------------------------------------

import sys

def main():
    n, m = map(int, input().split())
    stock = list(map(int, sys.stdin.readline().split()))
    bacs = list(map(int, sys.stdin.readline().split()))

    for bac in bacs:
        i = 0
        while i < len(stock) and bac > stock[i]:
            i += 1
        print(i, end=' ')
        stock.insert(i, bac)
    print()

    print(" ".join(map(str, stock)))

if __name__ == '__main__':
    main()

"""
5 4
2 2 4 6 7
3 1 8 6
"""
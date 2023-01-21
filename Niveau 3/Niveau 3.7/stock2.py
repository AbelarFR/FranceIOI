#-------------------------------------------------------------------------------
# Name:        État du stock
# Purpose:     France-IOI niveau 3.7
#
# Author:      Sébastien
#
# Created:     24/09/2022
#-------------------------------------------------------------------------------

import sys

def main():
    n = int(input())
    stock = list(map(int, sys.stdin.readline().split()))
    o = int(input())
    for _ in range(o):
        produit, operation = map(int, sys.stdin.readline().split())
        stock[produit-1] += operation
    print(" ".join(map(str, stock)))

if __name__ == '__main__':
    main()

"""
4
5 10 0 4
8
1 1
2 -2
4 2
3 5
3 -2
3 -1
1 4
1 -5
"""
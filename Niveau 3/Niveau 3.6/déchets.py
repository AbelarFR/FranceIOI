#-------------------------------------------------------------------------------
# Name:        Déchets polluants
# Purpose:     France-IOI niveau 3.6
#
# Author:      Sébastien
#
# Created:     18/09/2022
#-------------------------------------------------------------------------------

import sys

def main():
    n, m = map(int, input().split())
    dechets = list(map(int, sys.stdin.readline().split()))

    for _ in range(m):
        imax = 0
        for i in range(n):
            if dechets[i] > dechets[imax]:
                imax = i
        print(dechets[imax], end=' ')
        dechets[imax] = dechets[n-1]
        n -= 1

if __name__ == '__main__':
    main()

"""
6 4
3 2 17 0 10 3
"""
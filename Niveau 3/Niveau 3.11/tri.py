#-------------------------------------------------------------------------------
# Name:        Tri automatique
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     20/10/2022
#-------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

def main():
    p = int(input())
    petits = sorted(map(int, input().split()))
    s = int(input())
    souples = sorted(map(int, input().split()))

    n = 0
    i = 0
    j = 0

    while i < p and j < s:
        if petits[i] < souples[j]:
            i += 1
        elif petits[i] > souples[j]:
            j += 1
        else:
            n += 1
            i += 1
            j += 1

    print(n)

if __name__ == '__main__':
    main()


"""
6
9 4 5 12 3 14
10
6 2 3 1 8 11 4 5 7 12
"""
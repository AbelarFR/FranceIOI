#-------------------------------------------------------------------------------
# Name:        Premier absent
# Purpose:     France-IOI niveau 3.9
#
# Author:      Sébastien
#
# Created:     12/10/2022
#-------------------------------------------------------------------------------

import sys

def main():
    n, p = map(int, sys.stdin.readline().split())
    eleves = [False] * (p+2)
    premier_absent = 1
    for _ in range(p):
        e = int(sys.stdin.readline())
        if e <= p:
            eleves[e] = True
        if e == premier_absent:
            while premier_absent < n+1 and eleves[premier_absent]:
                premier_absent += 1
        if premier_absent > n:
            premier_absent = -1
        print(premier_absent)

if __name__ == '__main__':
    main()

"""
6 5
1
2
3
4
5
"""
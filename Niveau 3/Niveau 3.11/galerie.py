#-------------------------------------------------------------------------------
# Name:        Galerie souterraine
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     21/10/2022
#-------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

def main():
    h, l, d = map(int, input().split())
    plan = [[(c == 0) for c in map(int, input().split())] for _ in range(h)]

    x = 0
    y = 0
    n = 1

    while x != l-1 or y != h-1:
        if n % (d+1) == 0:
            print(y, x)
        plan[y][x] = False
        if   x > 0   and plan[y][x-1]: x -= 1
        elif x < l-1 and plan[y][x+1]: x += 1
        elif y > 0   and plan[y-1][x]: y -= 1
        else:                          y += 1
        n += 1
    if n % (d+1) == 0:
        print(y, x)

if __name__ == '__main__':
    main()

"""
9 11 7
0 0 1 0 0 0 1 1 1 1 1
1 0 0 0 1 0 1 0 0 0 0
1 1 1 1 1 0 1 0 1 1 0
1 1 0 0 0 0 1 0 0 1 0
1 1 0 1 1 1 1 1 0 1 0
1 1 0 1 1 1 1 0 0 1 0
1 1 0 0 0 0 1 0 1 0 0
1 1 1 1 1 0 1 0 1 0 1
1 1 1 1 1 0 0 0 1 0 0
---
2 2 0
0 0
1 0
"""
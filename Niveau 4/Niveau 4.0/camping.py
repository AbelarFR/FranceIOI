#-------------------------------------------------------------------------------
# Name:        Installation du camping
# Purpose:     France-IOI niveau 4.0
#
# Author:      Sébastien
#
# Created:     11/11/2022
#-------------------------------------------------------------------------------

import time
import sys
input = sys.stdin.readline

def main():
    l, c = map(int, input().split())
    plan = [list(map(lambda v : v == "1", input().split())) for _ in range(l)]
    carres = [[0]*c for _ in range(l)]
    taille_max = 0
    for y in range(l):
        for x in range(c):
            if plan[y][x]:
                carres[y][x] = 0
            elif y == 0 or x == 0:
                carres[y][x] = 1
            else:
                carres[y][x] = 1 + min(carres[y-1][x], carres[y][x-1], carres[y-1][x-1])
            taille_max = max(taille_max, carres[y][x])
    print(taille_max)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Temps d'exécution :", end-start, "ms")


"""
6 7
1 0 0 1 0 0 1
0 0 0 0 0 0 0
1 0 0 0 0 0 0
0 0 0 0 0 0 0
0 1 0 0 0 0 1
1 0 0 0 1 0 1
---
5 7
0 0 0 1 1 1 1
0 0 0 1 1 1 1
0 0 0 1 1 1 1
1 1 1 1 1 0 0
1 1 1 1 1 0 0
---
4 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""
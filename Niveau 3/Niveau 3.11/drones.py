#-------------------------------------------------------------------------------
# Name:        Essaim de drones
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     06/11/2022
#-------------------------------------------------------------------------------

##import time
import sys
input = sys.stdin.readline

def main():
    l, c = map(int, input().split())
    points1 = [(y,x) for y in range(l) for x,v in enumerate(input().split()) if v == "1"]
    points2 = [(y,x) for y in range(l) for x,v in enumerate(input().split()) if v == "1"]
    translations = [[0]*(c*2) for _ in range(l*2)]

    n_max = 0
    dy_max, dx_max = (0, 0)
    for y1,x1 in points1:
        for y2,x2 in points2:
            dy = y2 - y1
            dx = x2 - x1
            translations[dy+l][dx+c] += 1
            if translations[dy+l][dx+c] > n_max:
                n_max = translations[dy+l][dx+c]
                dy_max, dx_max = (dy, dx)

    print(n_max)
    for y1,x1 in points1:
        for y2,x2 in points2:
            if y2 - y1 == dy_max and x2 - x1 == dx_max:
                print(y2+1, x2+1)

if __name__ == '__main__':
##    start = time.time()
    main()
##    end = time.time()
##    print("Temps d'exécution :", end-start, "ms")

"""
10 8
0 1 1 0 0 0 0 0
0 1 1 1 0 0 0 0
0 0 0 0 0 1 0 0
0 1 1 1 1 0 0 0
0 0 1 1 1 0 0 0
0 0 0 1 1 0 0 0
0 1 0 0 1 0 0 0
0 0 0 0 0 0 1 0
0 1 0 0 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1
1 1 0 1 1 1 1 0
1 1 0 0 1 1 1 0
1 0 0 0 0 1 1 0
0 0 0 1 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 1 0 0 1 0 0 0
0 0 0 0 0 0 0 0
"""

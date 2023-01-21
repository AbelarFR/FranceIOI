#-------------------------------------------------------------------------------
# Name:        Les bons milieux
# Purpose:     France-IOI niveau 3.9
#
# Author:      Sébastien
#
# Created:     10/10/2022
#-------------------------------------------------------------------------------

import sys

def main():
    taille = 100
    nbPoints = int(sys.stdin.readline())
    plan = [[False]*(taille+1) for _ in range(taille+1)]
    liste = []
    for _ in range(nbPoints):
        x, y = map(int, sys.stdin.readline().split())
        liste.append((x, y))
        plan[x][y] = True

    nbMilieux = 0
    for p in liste:
        for q in liste:
            if q != p:
                # On calcule les coordonnées du point S symétrique de Q par rapport à P
                xs = 2*p[0] - q[0]
                ys = 2*p[1] - q[1]
                # Si S est dans le plan, alors P est un milieu (milieu de [QS])
                if xs >= 0 and xs <= taille and ys >= 0 and ys <= taille and plan[xs][ys]:
                    nbMilieux += 1
                    break

    print(nbMilieux)

if __name__ == '__main__':
    main()

"""
7
0 4
2 4
4 4
4 0
1 2
2 2
3 2
---
3
50 60
52 60
52 58
"""
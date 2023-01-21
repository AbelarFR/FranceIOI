#-------------------------------------------------------------------------------
# Name:        Rallonges audio
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     28/10/2022
#-------------------------------------------------------------------------------

def main():
    n = int(input())
    longueur = 0
    femelles = []
    males = []
    for _ in range(n):
        c1, c2, l = map(int, input().split())
        if c1 != c2:
            longueur += l
        elif c1 == 0:
            femelles.append(l)
        else:
            males.append(l)

    femelles.sort(reverse=True)
    males.sort(reverse=True)

    if len(males) > 0:
        n = min(len(femelles), len(males)-1)
        longueur += sum(femelles[:n]) + sum(males[:n+1])
        print(longueur)
    else:
        print(-1)

if __name__ == '__main__':
    main()

"""
5
1 0 1000
1 1 500
0 0 2000
1 1 800
0 0 3000
---
7
0 0 500
1 1 1000
0 0 600
1 1 2000
0 0 300
0 0 400
0 0 200
"""
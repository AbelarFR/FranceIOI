#-------------------------------------------------------------------------------
# Name:        Amis d’amis
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     30/10/2022
#-------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

def main():
    i = int(input())
    n = int(input())
    relations = []
    distance = [-1]*65000 # degré d'amitié : 0 = soi-même, 1 = ami direct, 2 = ami d'ami, -1 = pas ami
    distance[i] = 0
    for _ in range(n):
        i1, i2 = map(int, input().split())
        if i1 == i:
            distance[i2] = 1
        elif i2 == i:
            distance[i1] = 1
        else:
            relations.append((i1, i2))
            relations.append((i2, i1))

    nbAmis = 0
    for i1, i2 in relations:
        if  distance[i1] == 1 and distance[i2] == -1:
##            print("ami", i2)
            nbAmis += 1
            distance[i2] = 2

    print(nbAmis)

if __name__ == '__main__':
    main()

"""
0
11
0 1
0 2
0 3
1 2
1 3
2 3
4 1
2 5
2 4
3 6
7 8
"""

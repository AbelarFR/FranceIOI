#-------------------------------------------------------------------------------
# Name:        Dates de péremption
# Purpose:     France-IOI niveau 3.7
#
# Author:      Sébastien
#
# Created:     25/09/2022
#-------------------------------------------------------------------------------

def main():
    pile = []
    o = int(input())

    for _ in range(o):
        n, date = map(int, input().split())
        if n > 0:
            for _ in range(n):
                pile.append(date)
        else:
            pile = pile[:n]

    print(min(pile))


if __name__ == '__main__':
    main()

"""
8
3 20040810
-1 0
-1 0
3 20040920
-1 0
4 20040916
-3 0
-2 0
"""

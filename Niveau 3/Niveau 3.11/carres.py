#-------------------------------------------------------------------------------
# Name:        Carrés concentriques
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     23/10/2022
#-------------------------------------------------------------------------------

def distance(n, x, y):
    return max(abs(n-x), abs(n-y))

def main():
    n = int(input())
    mot = input()

    for y in range(1, 2*n):
        ligne = [mot[distance(n, x, y)] for x in range(1, 2*n)]
        print("".join(ligne))

if __name__ == '__main__':
    main()

"""
5
carre
"""
#-------------------------------------------------------------------------------
# Name:        Lecture dans une base quelconque
# Purpose:     France-IOI niveau 3.10
#
# Author:      Sébastien
#
# Created:     16/10/2022
#-------------------------------------------------------------------------------

def main():
    base, nbChiffres = map(int, input().split())
    chiffres = list(map(int, input().split()))
    n = 0
    for c in chiffres:
        n = base*n + c
    print(n)

if __name__ == '__main__':
    main()

"""
12 2
3 11
"""

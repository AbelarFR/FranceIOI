#-------------------------------------------------------------------------------
# Name:        Entre deux
# Purpose:     France-IOI niveau 3.8
#
# Author:      Sébastien
#
# Created:     04/10/2022
#-------------------------------------------------------------------------------

def ecrire_entiers(n, m):
    if n <= m:
        print(n, end=' ')
        ecrire_entiers(n+1, m)

if __name__ == '__main__':
    n, m = map(int, input().split())
    ecrire_entiers(n, m)

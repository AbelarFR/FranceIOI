#-------------------------------------------------------------------------------
# Name:        Affichage binaire
# Purpose:     France-IOI niveau 3.10
#
# Author:      Sébastien
#
# Created:     16/10/2022
#-------------------------------------------------------------------------------

def binaire(n):
    if n > 1:
        binaire(n // 2)
    print(n % 2, end='')

if __name__ == '__main__':
    n = int(input())
    binaire(n)
    print()

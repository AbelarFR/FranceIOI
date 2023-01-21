#-------------------------------------------------------------------------------
# Name:        Tours de Hanoï
# Purpose:     France-IOI niveau 3.8
#
# Author:      Sébastien
#
# Created:     03/10/2022
#-------------------------------------------------------------------------------

def hanoi(n, origine, destination):
    if n > 0:
        intermediaire = 6 - origine - destination
        hanoi(n-1, origine, intermediaire)
        print(origine, "->", destination)
        hanoi(n-1, intermediaire, destination)

if __name__ == '__main__':
    n = int(input())
    hanoi(n, 1, 3)
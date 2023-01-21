#-------------------------------------------------------------------------------
# Name:        Table de multiplication binaire
# Purpose:     France-IOI niveau 3.10
#
# Author:      Sébastien
#
# Created:     16/10/2022
#-------------------------------------------------------------------------------

def binaire(n):
    valeur = ""
    if n > 1:
        valeur = binaire(n // 2)
    valeur += str(n % 2)
    return valeur


if __name__ == '__main__':
    t = int(input())
    table = [[binaire(i*j) for i in range(1, t+1)] for j in range(1, t+1)]
    for ligne in table:
        print("\t".join(ligne))

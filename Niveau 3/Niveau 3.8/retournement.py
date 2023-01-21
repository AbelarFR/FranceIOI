#-------------------------------------------------------------------------------
# Name:        Retournement de chaîne
# Purpose:     France-IOI niveau 3.8
#
# Author:      Sébastien
#
# Created:     04/10/2022
#-------------------------------------------------------------------------------

def retourner(chaine):
    if len(chaine) > 0:
        retourner(chaine[1:])
        print(chaine[0], end='')

if __name__ == '__main__':
    chaine = input()
    retourner(chaine)
    print()

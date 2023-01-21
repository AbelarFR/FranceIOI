#-------------------------------------------------------------------------------
# Name:        Collage d'affiches
# Purpose:     France-IOI niveau 3.9
#
# Author:      Sébastien
#
# Created:     09/10/2022
#-------------------------------------------------------------------------------

import sys

##def collerAffiche(affiches, nbAffiches, hauteur):
##    debut = 0
##    fin = nbAffiches
##    while debut < fin:
##        milieu = (debut + fin) // 2
##        if hauteur < affiches[milieu]:
##            debut = milieu + 1
##        elif hauteur > affiches[milieu]:
##            fin = milieu
##        else:
##            debut = milieu
##            break
##    affiches[debut] = hauteur
##    return debut + 1

def collerAffiche(affiches, nbAffiches, hauteur):
     while (nbAffiches > 0) and (affiches[nbAffiches-1] <= hauteur):
        nbAffiches -= 1
     affiches[nbAffiches] = hauteur
     return nbAffiches + 1


def main():
    nbRequetes = int(sys.stdin.readline())
    affiches = [0]*nbRequetes
    nbAffiches = 0
    for _ in range(nbRequetes):
        action = sys.stdin.read(1)
        if action == 'Q':
            print(nbAffiches)
            sys.stdin.readline() # Ignore le reste de la ligne
        else:
            hauteur = int(sys.stdin.readline())
            nbAffiches = collerAffiche(affiches, nbAffiches, hauteur)

if __name__ == '__main__':
    main()

"""
12
C 2
Q
C 4
C 2
Q
C 9
Q
C 9
C 2
Q
C 8
Q
---
10
Q
C 8
C 7
C 11
Q
C 2
C 4
C 3
Q
C 3
"""
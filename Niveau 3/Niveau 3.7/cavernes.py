#-------------------------------------------------------------------------------
# Name:        Carte des cavernes
# Purpose:     France-IOI niveau 3.7
#
# Author:      Sébastien
#
# Created:     26/09/2022
#-------------------------------------------------------------------------------

def valide(s):
    compteur = 0
    for c in s:
        if c == '(':
            compteur += 1
        elif c == ')':
            compteur -= 1
        if compteur < 0:
            return False
    return compteur == 0

def main():
    n = int(input())
    s = input()
    if valide(s):
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()

"""
18
( ( () (()) ) () )
----
2
)(
----
9
( () (( )
----
0

"""

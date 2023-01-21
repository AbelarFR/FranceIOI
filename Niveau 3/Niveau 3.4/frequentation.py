#-------------------------------------------------------------------------------
# Name:        Fréquentation de la bibliothèque
# Purpose:     France-IOI niveau 3.4
#
# Author:      Sébastien
#
# Created:     14/09/2022
#-------------------------------------------------------------------------------

fin = False
total = 0
while not fin:
    try:
        nombres = map(int, input().split())
        for n in nombres:
            total += n
    except EOFError:
        fin = True

print(total)

"""
5
2 2
4 4 4
6 6
3 3
"""
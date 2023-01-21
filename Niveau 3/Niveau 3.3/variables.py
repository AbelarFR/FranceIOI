#-------------------------------------------------------------------------------
# Name:        Validité des noms de variables
# Purpose:     France-IOI niveau 3.3
#
# Author:      Sébastien
#
# Created:     13/09/2022
#-------------------------------------------------------------------------------

nbNoms = int(input())

for loop in range(nbNoms):
    variable = input()
    valide = variable[0] == '_' or variable[0].isalpha()

    i = 1
    while valide and i < len(variable):
        valide = variable[i] == '_' or variable[i].isalpha() or variable[i].isdigit()
        i += 1

    if valide: print("YES")
    else: print("NO")

"""
5
Bonjour32
r~ussi
_toto_
passe-partout
2_fois
"""
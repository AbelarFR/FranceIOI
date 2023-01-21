#-------------------------------------------------------------------------------
# Name:        Bâtiment et allée
# Purpose:     France-IOI niveau 3.3
#
# Author:      Sébastien
#
# Created:     11/09/2022
#-------------------------------------------------------------------------------

nom_auteur = input()
age_fils = int(input())
print(ord(nom_auteur[0]) - ord('A') + 1, end='')
print(chr(ord('A') + age_fils - 1))

"""
Dopelgon
6
"""
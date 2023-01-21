#-------------------------------------------------------------------------------
# Name:        Déchiffrement de la première page
# Purpose:     France-IOI niveau 3.4
#
# Author:      Sébastien
#
# Created:     15/09/2022
#-------------------------------------------------------------------------------

def dechiffrer_lettre(c, cle):
    if c.islower():
        i = ord(c) - ord('a')
        return cle[i]
    else:
        i = ord(c.lower()) - ord('a')
        return cle[i].upper()

cle = input()
texte = input()

for c in texte:
    if c.isalpha():
        c = dechiffrer_lettre(c, cle)
    print(c, end='')

"""
qwertyuiopasdfghjklzxcvbnm
Xiyqigd !
"""

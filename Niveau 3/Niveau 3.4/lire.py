#-------------------------------------------------------------------------------
# Name:        Lire ou ne pas lire, telle est (à nouveau) la question
# Purpose:     France-IOI niveau 3.4
#
# Author:      Sébastien
#
# Created:     14/09/2022
#-------------------------------------------------------------------------------

nbLivres = int(input())
titre_precedent = " "
for i in range(nbLivres):
    titre = input()
    if titre > titre_precedent:
        print(titre)
        titre_precedent = titre

"""
8
ANNA KARENINE
JACQUES LE FATALISTE ET SON MAITRE
DIX PETITS NEGRES
CENT ANS DE SOLITUDE
LA PESTE
LA FERME DES ANIMAUX
SUR LA ROUTE
SA MAJESTE DES MOUCHES
"""
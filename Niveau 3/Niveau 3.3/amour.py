#-------------------------------------------------------------------------------
# Name:        Nombre d'amour
# Purpose:     France-IOI niveau 3.3
#
# Author:      Sébastien
#
# Created:     12/09/2022
#-------------------------------------------------------------------------------

def calculer_nombre_amour(nom):
    nombre = 0
    for lettre in nom:
        nombre += ord(lettre) - ord('A')

    while (nombre >= 10):
        nombre_txt = str(nombre)
        nombre = 0
        for lettre in nombre_txt:
            nombre += ord(lettre) - ord('0')

    return nombre

nom1, nom2 = input().split()
print(calculer_nombre_amour(nom1), calculer_nombre_amour(nom2))
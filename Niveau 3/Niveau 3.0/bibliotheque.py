#-------------------------------------------------------------------------------
# Name:        Emprunts de livres
# Purpose:     France-IOI niveau 3.0
#
# Author:      Sébastien
#
# Created:     07/09/2022
#-------------------------------------------------------------------------------

nbLivres, nbJours = map(int, input().split())
livres = [0] * nbLivres

for jour in range(nbJours):
    # print("=== Jour", jour, "===")
    nbClients = int(input())
    for client in range(nbClients):
        livre, duree = map(int, input().split())
        if jour >= livres[livre]:
            livres[livre] = jour + duree
            # print("Le client emprunte le livre", livre, "pour", duree, "jours.")
            print(1)
        else:
            # print("Le client ne peut pas emprunter le livre", livre)
            print(0)

"""
2 4
2
0 3
1 3
1
0 3
1
1 4
2
0 2
0 5
"""
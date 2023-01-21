#-------------------------------------------------------------------------------
# Name:        Choisir son manteau
# Purpose:     France-IOI niveau 4.0
#
# Author:      Sébastien
#
# Created:     19/11/2022
#-------------------------------------------------------------------------------

import time
import sys
input = sys.stdin.readline
from operator import attrgetter

class Manteau:
    def __init__(self, id, deb, fin):
        self.id = id
        self.deb = deb
        self.fin = fin

def main():
    nbManteaux = int(input())
    manteaux = []
    for id in range(nbManteaux):
        deb, fin = map(int, input().split())
        manteaux.append(Manteau(id, deb, fin))

    # Etape 1 : Classer mes manteaux selon temperature_mini
    manteaux_mini = sorted(manteaux, key=attrgetter("deb"))
    # Etape 2 : Calculer rang_temperature_mini pour chaque manteau, en gérant les ex-aequo (0 pour le(s) manteau(x) qui a la température mini la plus basse)
    rang = 0
    rang_mini = [0]*nbManteaux
    for i in range(1, nbManteaux):
        if manteaux_mini[i].deb > manteaux_mini[i-1].deb:
            rang = i
        rang_mini[manteaux_mini[i].id] = rang

    # Etape 3 : Classer mes manteaux selon temperature_maxi
    manteaux_maxi = sorted(manteaux, key=attrgetter("fin"), reverse=True)
    # Etape 4 : Calculer rang_temperature_maxi pour chaque manteau, en gérant les ex-aequo (0 pour le(s) manteau(x) qui a la température maxi la plus haute)
    rang = 0
    rang_maxi = [0]*nbManteaux
    for i in range(1, nbManteaux):
        if manteaux_maxi[i].fin < manteaux_maxi[i-1].fin:
            rang = i
        rang_maxi[manteaux_maxi[i].id] = rang

    # Etape 5 : Calculer amplitude pour chaque manteau. amplitude = nbre_manteaux - rang_temperature_mini - rang_temperature_maxi
    amplitudes = [nbManteaux - 1 - rang_mini[i] - rang_maxi[i] for i in range(nbManteaux)]
    # Etape 6 : Le manteau avec l'amplitude la plus grande est le manteau voulu, et pour ce manteau, amplitude est l'indicateur demandé.
    print(max(amplitudes))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Temps d'exécution :", end-start, "ms")

"""
8
1 3
2 5
5 8
3 6
2 5
3 8
3 6
3 8
---
1
0 1
0 1
"""

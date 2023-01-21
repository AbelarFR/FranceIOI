#-------------------------------------------------------------------------------
# Name:        Gomoku
# Purpose:     France-IOI niveau 3.5
#
# Author:      Sébastien
#
# Created:     17/09/2022
#-------------------------------------------------------------------------------

def alignement(plateau, joueur, i, j, direction):
    n = len(plateau)
    for _ in range(4):
        i += direction[0]
        j += direction[1]
        if i < 0 or i >= n or j < 0 or j >= n or plateau[i][j] != joueur:
            return False
##  print("Joueur", joueur, "a 5 pions alignés dans la direction", direction, "à partir de la position", i, j)
    return True

def main():
    n = int(input())
    plateau = [list(map(int, input().split())) for _ in range(n)]

    directions = [(0,1), (1,0), (1,1), (1,-1)]
    for i in range(n):
        for j in range(n):
            joueur = plateau[i][j]
            if joueur != 0:
##              print("Pion du joueur", joueur, "à la position", i, j)
                for direction in directions:
                    if alignement(plateau, joueur, i, j, direction):
                        return joueur
    return 0


if __name__ == '__main__':
    print(main())

"""
6
0 0 2 0 1 0
0 1 2 2 2 1
0 0 2 0 1 0
0 0 2 1 0 0
0 0 1 0 0 0
0 1 0 0 0 0
"""
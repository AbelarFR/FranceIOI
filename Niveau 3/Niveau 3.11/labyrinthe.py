#-------------------------------------------------------------------------------
# Name:        Labyrinthe à billes
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     31/10/2022
#-------------------------------------------------------------------------------

from operator import itemgetter

mur   = '#'
vide  = '.'
trou  = 'O'
bille = 'x'
deplacements = {'N': (-1,0), 'S': (+1,0), 'O': (0,-1), 'E': (0,+1)}

def deplacer(labyrinthe, position, direction):
    deplacement = deplacements.get(direction)
    if deplacement == None: return position
    labyrinthe[position[0]][position[1]] = '.'

    while True:
        j, i = position[0] + deplacement[0], position[1] + deplacement[1]
        if labyrinthe[j][i] == trou:
            return None
        elif labyrinthe[j][i] == mur or labyrinthe[j][i] == bille:
            labyrinthe[position[0]][position[1]] = bille
            return position
        else:
            position = (j, i)

def main():
    l, c = map(int, input().split())
    labyrinthe = [[c for c in input()] for _ in range(l)]
    billes = []
    for j in range(l):
        for i in range(c):
            if labyrinthe[j][i] == bille:
                billes.append((j, i))

    _ = int(input())
    deplacements = input()
    for d in deplacements:
        if   d == 'N': billes.sort(key = itemgetter(0))
        elif d == 'S': billes.sort(key = itemgetter(0), reverse=True)
        elif d == 'O': billes.sort(key = itemgetter(1))
        elif d == 'E': billes.sort(key = itemgetter(1), reverse=True)
##        print("Avant déplacement :", billes)
        billes = [b for b in map(lambda x: deplacer(labyrinthe, x, d), billes) if b != None]
##        print("Après déplacement :", billes)

    print(len(billes))

if __name__ == '__main__':
    main()

"""
7 8
########
#x.....#
#....O.#
#....#.#
####.#.#
#x...#.#
########
4
SENE
---
7 8
########
#x...x.#
#....O.#
#....#.#
#O##.#.#
#x...#.#
########
4
SE NE
"""
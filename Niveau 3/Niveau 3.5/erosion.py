#-------------------------------------------------------------------------------
# Name:        Érosion
# Purpose:     France-IOI niveau 3.5
#
# Author:      Sébastien
#
# Created:     18/09/2022
#-------------------------------------------------------------------------------

import sys

def quatre_voisins(image, h, l, i, j):
    return not (i == 0 or i == h-1 or
                j == 0 or j == l-1 or
                image[i-1][j] == '.' or
                image[i+1][j] == '.' or
                image[i][j-1] == '.' or
                image[i][j+1] == '.')

def main():
    n = int(sys.stdin.readline())
    h, l = map(int, sys.stdin.readline().split())
    image = [list(sys.stdin.readline()) for _ in range(h)]

    for _ in range(n):
        new_image = [[] for _ in range(h)]
        for i in range(h):
            for j in range(l):
                if image[i][j] == '.' or not quatre_voisins(image, h, l, i, j):
                    new_image[i].append('.')
                else:
                    new_image[i].append('#')
        image = new_image

    for ligne in image:
        print("".join(ligne))


if __name__ == '__main__':
    main()

"""
2
12 16
...########.....
..#########.....
.##########.....
################
################
######..#######.
.######.#######.
..############..
...###########..
....#########...
......#######...
........####....
"""
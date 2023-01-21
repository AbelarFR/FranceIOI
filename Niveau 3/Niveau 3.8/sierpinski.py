#-------------------------------------------------------------------------------
# Name:        Fractale : triangle de Sierpinski
# Purpose:     France-IOI niveau 3.8
#
# Author:      Sébastien
#
# Created:     02/10/2022
#-------------------------------------------------------------------------------

def sierpinski(fractale, n, i, j):
    if n == 1:
        fractale[i][j] = True
    else:
        sierpinski(fractale, n//2, i, j)
        sierpinski(fractale, n//2, i+n//2, j)
        sierpinski(fractale, n//2, i, j+n//2)

def main():
    n = int(input())
    fractale = [[False]*n for _ in range(n)]
    sierpinski(fractale, n, 0, 0)

    for ligne in fractale:
        for c in ligne:
            if c: print("#", end='')
            else: print(" ", end='')
        print()

if __name__ == '__main__':
    main()

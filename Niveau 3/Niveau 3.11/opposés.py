#-------------------------------------------------------------------------------
# Name:        Nombres opposés
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     29/10/2022
#-------------------------------------------------------------------------------

def main():
    _ = int(input())
    nombres = list(map(int, input().split()))
    positifs = sorted([ n for n in nombres if n > 0])
    negatifs = sorted([-n for n in nombres if n < 0])

    n = 0
    i = 0
    j = 0
    valeur_precedente = 0
    while i < len(positifs) and j < len(negatifs):
        if positifs[i] == negatifs[j]:
            if positifs[i] != valeur_precedente:
                n += 1
                valeur_precedente = positifs[i]
            i += 1
            j += 1
        elif positifs[i] < negatifs[j]:
            i += 1
        else:
            j += 1

    print(n)

if __name__ == '__main__':
    main()

"""
15
-3 4 2 8 9 1 -3 -8 -4 2 8 2 -8 1 3
"""
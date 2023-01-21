#-------------------------------------------------------------------------------
# Name:        Hydroélectricité
# Purpose:     France-IOI niveau 3.7
#
# Author:      Sébastien
#
# Created:     01/10/2022
#-------------------------------------------------------------------------------

def main():
    k, n = map(int, input().split())
    forces = list(map(int, input().split()))

    somme = sum(forces[0:k])
    maxi = somme
    for i in range(n-k):
        somme += forces[i+k] - forces[i]
        if somme > maxi:
            maxi = somme

    print(maxi)

if __name__ == '__main__':
    main()

"""
3 9
3 2 5 7 4 2 3 8 4
"""
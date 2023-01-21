#-------------------------------------------------------------------------------
# Name:        Boîtes factorielles
# Purpose:     France-IOI niveau 4.0
#
# Author:      Sébastien
#
# Created:     13/11/2022
#-------------------------------------------------------------------------------

MAX_NB_COEF = 13

def main():
    n = int(input())

    factorielle = [1]*MAX_NB_COEF
    for i in range(1, MAX_NB_COEF):
        factorielle[i] = i * factorielle[i-1]

    resultat = [0]*MAX_NB_COEF
    p = 0
    for i in range(MAX_NB_COEF-1, 0, -1):
        if n >= factorielle[i]:
            resultat[i] = n // factorielle[i]
            n %= factorielle[i]
            if p == 0: p = i

    print(p)
    print(" ".join(map(str, resultat[1:p+1])))

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------
# Name:        Carte de cinéma
# Purpose:     France-IOI niveau 3.7
#
# Author:      Sébastien
#
# Created:     27/09/2022
#-------------------------------------------------------------------------------

##def main():
##    nombre = int(input())
##    numeros = list(map(int, input().split()))
##    numeros_tries = [-1]*nombre
##    for i in range(nombre):
##        j = i
##        n = numeros[i]
##        while j > 0 and n <= numeros_tries[j-1]:
##            numeros_tries[j] = numeros_tries[j-1]
##            j -= 1
##        if n == numeros_tries[j]:
##            return n
##        else:
##            numeros_tries[j] = n
##    print(numeros_tries)
##    return -1

def main():
    nombre = int(input())
    cartes = list(map(int, input().split()))
    numeros = [False]*1000001
    for n in cartes:
        if numeros[n]:
            return n
        else:
            numeros[n] = True
    return -1

if __name__ == '__main__':
    print(main())

"""
4
1 2 2 1
----
4
10 2 3 2
----
5
11 3 17 13 19
----
5
11 3 17 11 3
"""

#-------------------------------------------------------------------------------
# Name:        Moyenne hexadécimale
# Purpose:     France-IOI niveau 3.10
#
# Author:      Sébastien
#
# Created:     16/10/2022
#-------------------------------------------------------------------------------

def main():
    n = int(input(), 16)
    somme = 0
    for _ in range(n):
        somme += int(input(), 16)
    moyenne = somme // n
    print(hex(moyenne)[2:].upper())

if __name__ == '__main__':
    main()

"""
C
0
2
4
6
8
A
C
E
10
12
14
16
"""
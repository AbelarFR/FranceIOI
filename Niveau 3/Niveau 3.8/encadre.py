#-------------------------------------------------------------------------------
# Name:        Nombre encadré
# Purpose:     France-IOI niveau 3.8
#
# Author:      Sébastien
#
# Created:     01/10/2022
#-------------------------------------------------------------------------------

def ecrire_crochets(n, e):
    if e == 0:
        print(n, end='')
    else:
        print('[', end='')
        ecrire_crochets(n, e-1)
        print(']', end='')

def main():
    n, e = map(int, input().split())
    ecrire_crochets(n, e)

if __name__ == '__main__':
    main()

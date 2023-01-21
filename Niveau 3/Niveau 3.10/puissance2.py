#-------------------------------------------------------------------------------
# Name:        Puissance de 2
# Purpose:     France-IOI niveau 3.10
#
# Author:      Sébastien
#
# Created:     16/10/2022
#-------------------------------------------------------------------------------

def main():
    n = int(input())
    p = 1
    while n > 1:
        n //= 2
        p *= 2
    print(p)

if __name__ == '__main__':
    main()

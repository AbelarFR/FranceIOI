#-------------------------------------------------------------------------------
# Name:        Lecture binaire
# Purpose:     France-IOI niveau 3.10
#
# Author:      Sébastien
#
# Created:     16/10/2022
#-------------------------------------------------------------------------------

def main():
    s = input()
    n = 0
    for c in s:
        n = 2*n + int(c)
    print(n)

if __name__ == '__main__':
    main()

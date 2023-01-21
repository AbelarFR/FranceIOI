#-------------------------------------------------------------------------------
# Name:        Cartes perforées
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     21/10/2022
#-------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        ligne = input()
        for i in range(26):
            if ligne[i] == 'O':
                print(chr(ord('A')+i), end='')
    print()

if __name__ == '__main__':
    main()

"""
5
###########O##############
####O##############O######
###################O######
#################O########
####O#############O#######
---
1
OOOOOOOOOOOOOOOOOOOOOOOOOO
"""
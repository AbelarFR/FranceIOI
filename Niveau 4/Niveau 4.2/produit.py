#-------------------------------------------------------------------------------
# Name:        Retrouver un produit
# Purpose:     France-IOI niveau 4.2
#
# Author:      Sébastien
#
# Created:     21/01/2023
#-------------------------------------------------------------------------------

import time

def main():
    _ = int(input())
    codes = list(map(int, input().split()))

    _ = int(input())
    for code in map(int, input().split()):
        path = [code]
        while code > 0:
            code = codes[code-1]
            if code > 0: path.insert(0, code)
        print(" ".join(map(str, path)))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
##  print("Temps d'exécution :", end-start, "ms")

"""
8
3 3 7 3 6 7 0 0
3
1 5 8
"""
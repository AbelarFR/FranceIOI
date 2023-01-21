#-------------------------------------------------------------------------------
# Name:        Introduction à la complexité en temps des algorithmes
# Purpose:     France-IOI niveau 3.9
#
# Author:      Sébastien
#
# Created:     07/10/2022
#-------------------------------------------------------------------------------

import time

def ne_fait_rien(n):
    for _ in range(n):
        pass

def additions(n):
    total = 0
    for i in range(n):
        total += i
        total += i
        total += i
        total += i
        total += i

        total += i
        total += i
        total += i
        total += i
        total += i

def multiplications(n):
    total = 1
    for i in range(1, n+1):
        total *= i
        total *= i
        total *= i
        total *= i
        total *= i

        total *= i
        total *= i
        total *= i
        total *= i
        total *= i

def divisions(n):
    total = n*1.0
    for i in range(1, n+1):
        total = n / i
        total = n / i
        total = n / i
        total = n / i
        total = n / i

        total = n / i
        total = n / i
        total = n / i
        total = n / i
        total = n / i

def modulos(n):
    total = n
    for i in range(1, n+1):
        total %= i
        total %= i
        total %= i
        total %= i
        total %= i

        total %= i
        total %= i
        total %= i
        total %= i
        total %= i

if __name__ == '__main__':
    n = int(input().replace(' ', ''))
    t1 = time.time()
    ne_fait_rien(n)
    t2 = time.time()
    print("rien :", t2-t1)
    t1 = time.time()
    additions(n)
    t2 = time.time()
    print("additions :", t2-t1)
    t1 = time.time()
    multiplications(n)
    t2 = time.time()
    print("multiplications :", t2-t1)
    t1 = time.time()
    divisions(n)
    t2 = time.time()
    print("divisions :", t2-t1)
    t1 = time.time()
    modulos(n)
    t2 = time.time()
    print("modulos :", t2-t1)

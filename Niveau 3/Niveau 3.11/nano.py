#-------------------------------------------------------------------------------
# Name:        iPhone Nano
# Purpose:     France-IOI niveau 3.11
#
# Author:      Sébastien
#
# Created:     31/10/2022
#-------------------------------------------------------------------------------

def main():
    d = int(input())
    mots = [[] for _ in range(20)]
    for _ in range(d):
        mot = input()
        mots[len(mot)-1].append(mot)

    n = int(input())
    mots = mots[n-1]
    for i in range(n):
        lettres = input()
        for j, mot in enumerate(mots):
            if mot != None and not mot[i] in lettres:
                mots[j] = None

##    print(mots)
    for mot in mots:
        if mot != None:
            print(mot)
            break

if __name__ == '__main__':
    main()

"""
9
franceioi
nano
apple
ipod
iphone
ocaml
debian
print
scanf
5
apoh
rcpi
piua
mnod
dlte
---
9
print
franceioi
nano
apple
ipod
iphone
ocaml
debian
scanf
5
apoh
rcpi
piua
mnod
dlte
"""
#-------------------------------------------------------------------------------
# Name:        Attaque du cavalier
# Purpose:     France-IOI niveau 3.5
#
# Author:      Sébastien
#
# Created:     17/09/2022
#-------------------------------------------------------------------------------

def piece_noire(echiquier, i, j):
    return (i >= 0 and i < 8 and
            j >= 0 and j < 8 and
            echiquier[i][j].islower())

def main():
    echiquier = [input() for _ in range(8)]
    mouvements = [(+1,+2),(+1,-2),(-1,+2),(-1,-2),(+2,+1),(+2,-1),(-2,+1),(-2,-1)]

    for i in range(8):
        for j in range(8):
            if echiquier[i][j] == 'C':
##              print("Cavalier trouvé à la position", i, j)
                for (di, dj) in mouvements:
                    if (piece_noire(echiquier, i+di, j+dj)):
                        return True

    return False


if __name__ == '__main__':
    reponse = main()
    if reponse:
        print("yes")
    else:
        print("no")

"""
tc.drf.t
ppp.pppp
...p...c
.....f..
..C..P..
..P.D.P.
PP.....P
T.F.RFCT
"""
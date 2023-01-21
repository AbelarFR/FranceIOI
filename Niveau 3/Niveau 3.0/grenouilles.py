#-------------------------------------------------------------------------------
# Name:        Course de grenouilles
# Purpose:     France-IOI niveau 3.0
#
# Author:      Sébastien
#
# Created:     10/09/2022
#-------------------------------------------------------------------------------

nbGrenouilles = int(input())
nbTours = int(input())

points = [0] * nbGrenouilles
positions = [0] * nbGrenouilles
pos_max = 0
leader = 0

for tour in range(nbTours):
    # On détermine la grenouille en tête au début du tour
    if leader > 0:
        # print("Grenouille", leader, "en tête")
        points[leader-1] += 1
    # else:
    #   print("Egalité")

    # Une grenouille saute
    numGrenouille, saut = map(int, input().split())
    positions[numGrenouille-1] += saut

    # La grenouille dépasse le leader
    if positions[numGrenouille-1] > pos_max:
        leader = numGrenouille
        pos_max = positions[leader-1]
    # La grenouille est au même niveau que le leader
    elif positions[numGrenouille-1] == pos_max:
        leader = 0

meilleur_score = max(points)
for i in range(nbGrenouilles):
    if points[i] == meilleur_score:
        print(i+1)
        break

"""
4
6
2 2
1 2
3 3
4 1
2 2
3 1
"""
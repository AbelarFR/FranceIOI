#-------------------------------------------------------------------------------
# Name:        Plus long palindrome
# Purpose:     France-IOI niveau 3.9
#
# Author:      Sébastien
#
# Created:     09/10/2022
#-------------------------------------------------------------------------------

def chercherPalindrome(texte, gauche, droite):
    while gauche >= 0 and droite < len(texte) and texte[gauche] == texte[droite]:
        gauche -= 1
        droite += 1
##    print("[" + texte[gauche+1:droite] + "]", end=' ')
    return droite - gauche - 1

def chercherPalindromeMaximum(texte):
    maxi = 1
    for i in range(len(texte)):
##        print(i, texte[i], ":", end=' ')
        if i + maxi//2 >= len(texte): break
        maxi = max(maxi, chercherPalindrome(texte, i-1, i+1))
        maxi = max(maxi, chercherPalindrome(texte, i, i+1))
##        print()
    return maxi

if __name__ == '__main__':
    texte = input()
    print(chercherPalindromeMaximum(texte))

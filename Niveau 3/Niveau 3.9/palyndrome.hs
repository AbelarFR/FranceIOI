--------------------------------------------------------------------------------
-- Name:        Plus long palindrome
-- Purpose:     France-IOI niveau 3.9
--
-- Author:      Sébastien
--
-- Created:     09/10/2022
--------------------------------------------------------------------------------

main :: IO()
main = do  
    texte <- getLine
    print $ maximum (map (chercherPalindromeMax texte) [0..length texte -1])
    
chercherPalindromeMax :: String -> Int -> Int
chercherPalindromeMax [] _ = 0
chercherPalindromeMax texte position = let gauche = reverse $ take position texte
                                           droite = drop position texte
                                           droite' = drop (position+1) texte
        in max (chercherPalindrome gauche droite) (1 + chercherPalindrome gauche droite')

chercherPalindrome :: String -> String -> Int
chercherPalindrome [] _ = 0
chercherPalindrome _ [] = 0
chercherPalindrome (g:gs) (d:ds) = if g == d then 2 + chercherPalindrome gs ds else 0



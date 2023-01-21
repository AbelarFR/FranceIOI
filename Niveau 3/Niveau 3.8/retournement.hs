--------------------------------------------------------------------------------
-- Name:        Retournement de chaîne
-- Purpose:     France-IOI niveau 3.8
--
-- Author:      Sébastien
--
-- Created:     04/10/2022
--------------------------------------------------------------------------------

main :: IO()
main = do  
    chaine <- getLine
    putStrLn $ retourner' chaine
    
retourner :: String -> String
retourner [] = []
retourner (x:xs) = (retourner xs)++[x]

retourner' :: String -> String
retourner' chaine = foldl (\x y -> y:x) [] chaine

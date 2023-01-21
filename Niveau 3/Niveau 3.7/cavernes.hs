--------------------------------------------------------------------------------
-- Name:        Carte des cavernes
-- Purpose:     France-IOI niveau 3.7
--
-- Author:      Sébastien
--
-- Created:     26/09/2022
--------------------------------------------------------------------------------

valide :: String -> Int -> Bool
valide "" c = (c == 0) -- Fin de chaîne
valide ('(':xs) c = valide xs (c+1)
valide (')':xs) c = if c > 0 then valide xs (c-1) else False
valide (_:xs) c = valide xs c -- Ignore les caractères autres que ( ou )

main :: IO()
main = do  
    _ <- getLine
    s <- getLine
    putStrLn $ if valide s 0 then "1" else "0"
    

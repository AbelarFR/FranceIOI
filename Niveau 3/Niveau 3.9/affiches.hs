--------------------------------------------------------------------------------
-- Name:        Collage d'affiches
-- Purpose:     France-IOI niveau 3.9
--
-- Author:      Sébastien
--
-- Created:     09/10/2022
--------------------------------------------------------------------------------

collerAffiche :: Int -> [Int] -> [Int]
collerAffiche h [] = [h]
collerAffiche h (x:xs) = if h < x then h:x:xs
                         else collerAffiche h xs

traiterRequete :: Int -> [Int] -> IO()
traiterRequete 0 _ = return ()
traiterRequete nbRequetes affiches = do
    action <- getChar
    if action == 'Q' then do
        _ <- getLine
        print $ length affiches
        traiterRequete (nbRequetes-1) affiches
    else do
        hauteur <- readLn :: IO Int
        traiterRequete (nbRequetes-1) (collerAffiche hauteur affiches)
        
main :: IO()
main = do  
    nbRequetes <- readLn :: IO Int
    traiterRequete nbRequetes []    

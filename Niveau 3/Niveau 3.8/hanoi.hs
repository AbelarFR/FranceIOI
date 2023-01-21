--------------------------------------------------------------------------------
-- Name:        Tours de Hanoï
-- Purpose:     France-IOI niveau 3.8
--
-- Author:      Sébastien
--
-- Created:     03/10/2022
--------------------------------------------------------------------------------

main :: IO()
main = do  
    n <- readLn :: IO Int
    hanoi n 1 3
    
hanoi :: Int -> Int -> Int -> IO()
hanoi 0 _ _ = return ()
hanoi n origine destination = let intermediaire = 6 - origine - destination
    in do
        hanoi (n-1) origine intermediaire
        putStrLn $ show origine ++ " -> " ++ show destination
        hanoi (n-1) intermediaire destination

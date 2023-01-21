--------------------------------------------------------------------------------
-- Name:        Puissance de 2
-- Purpose:     France-IOI niveau 3.10
--
-- Author:      Sébastien
--
-- Created:     16/10/2022
--------------------------------------------------------------------------------

main :: IO()
main = do
    n <- readLn :: IO Int
    print $ puissance2 n
    
puissance2 :: Int -> Int
puissance2 1 = 1
puissance2 n = 2 * (puissance2 (n `div` 2))

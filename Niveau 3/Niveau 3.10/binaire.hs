--------------------------------------------------------------------------------
-- Name:        Affichage binaire
-- Purpose:     France-IOI niveau 3.10
--
-- Author:      Sébastien
--
-- Created:     16/10/2022
--------------------------------------------------------------------------------

main :: IO()
main = do
    n <- readLn :: IO Int
    putStrLn $ binaire n
    
binaire :: Int -> String
binaire n
    | n <= 1 = show n
    | otherwise = binaire (n `div` 2) ++ show (n `mod` 2)


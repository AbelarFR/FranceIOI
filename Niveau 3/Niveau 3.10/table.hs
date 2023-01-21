--------------------------------------------------------------------------------
-- Name:        Table de multiplication binaire
-- Purpose:     France-IOI niveau 3.10
--
-- Author:      Sébastien
--
-- Created:     16/10/2022
--------------------------------------------------------------------------------

import Data.List

main :: IO()
main = do
    t <- readLn :: IO Int
    let table = [[binaire (i*j) | i <- [1..t]] | j <-[1..t]]
    putStrLn $ unlines (map (intercalate "\t") table)

binaire :: Int -> String
binaire n
    | n <= 1 = show n
    | otherwise = binaire (n `div` 2) ++ show (n `mod` 2)

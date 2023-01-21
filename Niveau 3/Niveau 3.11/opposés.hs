--------------------------------------------------------------------------------
-- Name:        Nombres opposés
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     29/10/2022
--------------------------------------------------------------------------------

import Data.Containers.ListUtils
import Data.List

main :: IO ()
main = do
    _ <- readLn :: IO Int
    nombres <- fmap (map read . words) getLine :: IO [Int]
    let positifs = sort [ n | n <- nombres, n > 0]
        negatifs = sort [-n | n <- nombres, n < 0]
    -- print $ length (nubInt (intersect positifs negatifs))
    print $ nbCommuns 0 positifs negatifs
    
    
nbCommuns :: Int -> [Int] -> [Int] -> Int
nbCommuns _ [] _ = 0
nbCommuns _ _ [] = 0
nbCommuns précédent (x:xs) (y:ys)
    | x < y = nbCommuns précédent xs (y:ys)
    | x > y = nbCommuns précédent (x:xs) ys
    | x == y && x == précédent = nbCommuns précédent xs ys
    | otherwise = 1 + nbCommuns x xs ys

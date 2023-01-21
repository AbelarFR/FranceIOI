--------------------------------------------------------------------------------
-- Name:        Écriture dans une base quelconque
-- Purpose:     France-IOI niveau 3.10
--
-- Author:      Sébastien
--
-- Created:     16/10/2022
--------------------------------------------------------------------------------

import Data.List

main :: IO()
main = do
    (n:base:_) <- fmap (map read . words) getLine :: IO [Int]
    let chiffres = convertir n base
    print $ length chiffres
    putStrLn $ intercalate " " (map show chiffres)
    
convertir :: Int -> Int -> [Int]
convertir n base
    | n < base = [n]
    | otherwise = convertir (n `div` base) base ++ [n `mod` base]


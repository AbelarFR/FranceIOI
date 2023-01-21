--------------------------------------------------------------------------------
-- Name:        Changement de base
-- Purpose:     France-IOI niveau 3.10
--
-- Author:      Sébastien
--
-- Created:     16/10/2022
--------------------------------------------------------------------------------

import Data.List

main :: IO()
main = do
    (b1:b2:_) <- fmap (map read . words) getLine :: IO [Int]
    chiffres <- fmap (map read . words) getLine :: IO [Int]
    let n = foldl (\n c -> b1*n + c) 0 chiffres
    let chiffres' = convertir n b2
    putStrLn $ intercalate " " (map show chiffres')
    
convertir :: Int -> Int -> [Int]
convertir n base
    | n < base = [n]
    | otherwise = convertir (n `div` base) base ++ [n `mod` base]


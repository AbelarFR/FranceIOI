--------------------------------------------------------------------------------
-- Name:        Tri automatique
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     20/10/2022
--------------------------------------------------------------------------------

import Data.List

main :: IO ()
main = do
    _ <- readLn :: IO Int
    petits <- fmap (sort . map read . words) getLine :: IO [Int]
    _ <- readLn :: IO Int
    souples <- fmap (sort . map read . words) getLine :: IO [Int]
    print $ nbCommun petits souples

nbCommun :: [Int] -> [Int] -> Int
nbCommun [] _ = 0
nbCommun _ [] = 0
nbCommun (x:xs) (y:ys)
    | x < y = nbCommun xs (y:ys)
    | x > y = nbCommun (x:xs) ys
    | otherwise = 1 + nbCommun xs ys
    
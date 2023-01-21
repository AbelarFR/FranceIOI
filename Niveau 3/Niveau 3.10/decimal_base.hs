--------------------------------------------------------------------------------
-- Name:        Lecture dans une base quelconque
-- Purpose:     France-IOI niveau 3.10
--
-- Author:      Sébastien
--
-- Created:     16/10/2022
--------------------------------------------------------------------------------

main :: IO()
main = do
    (base:_) <- fmap (map read . words) getLine :: IO [Int]
    chiffres <- fmap (map read . words) getLine :: IO [Int]
    print $ foldl (\n c -> base*n + c) 0 chiffres

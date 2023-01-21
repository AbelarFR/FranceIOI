--------------------------------------------------------------------------------
-- Name:        Extension du centre
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     19/10/2022
--------------------------------------------------------------------------------

import Data.List

reunir :: [Int] -> [Int] -> [Int]
reunir [] [] = []
reunir xs [] = xs
reunir [] ys = ys
reunir (x:xs) (y:ys) = if x <= y then x:reunir xs (y:ys) else y:reunir (x:xs) ys

main :: IO()
main = do
    _ <- readLn :: IO Int
    xs <- fmap (map read . words) getLine :: IO [Int]
    _ <- readLn :: IO Int
    ys <- fmap (map read . words) getLine :: IO [Int]
    let liste_u = reunir xs ys
    putStrLn $ intercalate " " (map show liste_u)
    
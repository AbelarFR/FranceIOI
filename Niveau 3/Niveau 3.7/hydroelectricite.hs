--------------------------------------------------------------------------------
-- Name:        Hydroélectricité
-- Purpose:     France-IOI niveau 3.7
--
-- Author:      Sébastien
--
-- Created:     01/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List

main :: IO()
main = do  
    k:n:_ <- fmap (map read . words) getLine :: IO [Int]
    forces <- fmap (map read . words) getLine :: IO [Int]
    let sommes = calculerSommes' forces
        sommes' = zipWith (\a b -> a-b) (take (n+1-k) sommes) (drop k sommes)
    print $ maximum sommes'
    
calculerSommes :: [Int] -> [Int]
calculerSommes [] = [0]
calculerSommes (x:xs) = let s:sommes = calculerSommes xs
                        in (x+s):s:sommes

calculerSommes' :: [Int] -> [Int]
calculerSommes' liste = foldr (\y (x:xs) -> (x+y):x:xs) [0] liste

calculerSommes'' :: [Int] -> [Int]
calculerSommes'' liste = reverse $ foldl (\(x:xs) y -> (x+y):x:xs) [0] liste
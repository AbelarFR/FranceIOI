--------------------------------------------------------------------------------
-- Name:        Longueur des descriptions
-- Purpose:     France-IOI niveau 4.2
--
-- Author:      Sébastien
--
-- Created:     22/01/2023
--------------------------------------------------------------------------------

import Control.Monad
import Data.List
import Data.Array
import System.TimeIt

main :: IO ()
main = timeIt $ do
    n <- readLn :: IO Int
    liste <- fmap (zip [1..n] . map read . words) getLine :: IO [(Int, Int)]
    let arbre0 = array (0, n) [(i, [] ) | i <- [0..n]]
        arbre = foldr (mettreDansBoite) arbre0 liste
    print $ calculerProfondeur arbre (arbre!0)
    
mettreDansBoite :: (Int, Int) -> Array Int [Int] -> Array Int [Int]
mettreDansBoite (contenu, i) arbre =
    arbre // [(i, contenu:(arbre!i))]

calculerProfondeur :: Array Int [Int] -> [Int] -> Int
calculerProfondeur _ [] = 0
calculerProfondeur arbre contenu =
    (maximum (map (calculerProfondeur arbre . (!) arbre) contenu)) + 1
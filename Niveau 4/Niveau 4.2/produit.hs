--------------------------------------------------------------------------------
-- Name:        Retrouver un produit
-- Purpose:     France-IOI niveau 4.2
--
-- Author:      Sébastien
--
-- Created:     22/01/2023
--------------------------------------------------------------------------------

import Control.Monad
import Data.List
import Data.Array.Unboxed

main :: IO ()
main = do
    nbObjets <- readLn :: IO Int
    objets <- fmap (array (1, nbObjets) . zip [1..nbObjets] . map read . words) getLine :: IO (Array Int Int)
    
    _  <- readLn :: IO Int
    listeRecherches <- fmap (map read . words) getLine :: IO [Int]
    putStr $ unlines (map (afficherChemin . rechercherChemin objets) listeRecherches)
    
rechercherChemin :: Array Int Int -> Int -> [Int]
rechercherChemin _ 0 = []
rechercherChemin objets n = n : (rechercherChemin objets (objets ! n))

afficherChemin :: [Int] -> String
afficherChemin chemin = intercalate " " (map show (reverse chemin))

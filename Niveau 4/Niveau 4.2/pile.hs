--------------------------------------------------------------------------------
-- Name:        Pile de cartons
-- Purpose:     France-IOI niveau 4.2
--
-- Author:      Sébastien
--
-- Created:     27/01/2023
--------------------------------------------------------------------------------

import Data.Array
import Data.Array.IO
import System.TimeIt

main :: IO ()
-- main = timeIt $ do
main = do
    nbNoeuds <- readLn :: IO Int
    -- Crée l'arbre
    arbreM <- newArray (0, nbNoeuds) [] :: IO (IOArray Int [Int])
    sequence (map (initialiser arbreM) [0..nbNoeuds])
    -- Transforme l'arbre en immutable array
    arbre <- freeze arbreM :: IO (Array Int [Int])
    sequence_ (map (afficherChemin arbre) (arbre!0))

-- Lit et ajoute la liste des fils du noeud n° i de l'arbre.    
initialiser :: IOArray Int [Int] -> Int -> IO ()
initialiser arbre i = do
    _:fils <- fmap (map read . words) getLine :: IO [Int]
    writeArray arbre i fils

afficherChemin :: Array Int [Int] -> Int -> IO ()
afficherChemin arbre noeud = do
    putStrLn $ "A " ++ show noeud
    sequence (map (afficherChemin arbre) (arbre!noeud))
    putStrLn $ "R " ++ show noeud

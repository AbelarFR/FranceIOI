--------------------------------------------------------------------------------
-- Name:        Longueur des descriptions
-- Purpose:     France-IOI niveau 4.2
--
-- Author:      Sébastien
--
-- Created:     22/01/2023
--------------------------------------------------------------------------------

import Data.Array
import Data.Array.IO
import System.TimeIt

main :: IO ()
main = timeIt $ do
    -- Nombre d'objets = nombre de noeuds de l'arbre
    n <- readLn :: IO Int
    -- Liste de couples n° contenu (= fils), n° contenant (= père)
    liste <- fmap (zip [1..n] . map read . words) getLine :: IO [(Int, Int)]
    -- Crée l'arbre
    arbreM <- newArray (0, n) [] :: IO (IOArray Int [Int])
    sequence (map (initialiser arbreM) liste)
    -- Transforme l'arbre en immutable array
    arbre <- freeze arbreM :: IO (Array Int [Int])
    print $ calculerProfondeur arbre (arbre!0)

-- Ajoute contenu dans la liste des fils du noeud n° i de l'arbre.    
initialiser :: IOArray Int [Int] -> (Int, Int) -> IO ()
initialiser arbre (contenu, i) = do
    fils <- readArray arbre i
    writeArray arbre i (contenu:fils)

-- Calcule la profondeur sous un noeud avec l'ensemble de ces fils.
calculerProfondeur :: Array Int [Int] -> [Int] -> Int
calculerProfondeur _ [] = 0
calculerProfondeur arbre fils =
    (maximum (map (calculerProfondeur arbre . (!) arbre) fils)) + 1
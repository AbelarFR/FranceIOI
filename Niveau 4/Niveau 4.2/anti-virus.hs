--------------------------------------------------------------------------------
-- Name:        Anti-virus
-- Purpose:     France-IOI niveau 4.2
--
-- Author:      Sébastien
--
-- Created:     28/01/2023
--------------------------------------------------------------------------------

import Data.Array
import Data.Array.IO
import System.TimeIt

type Arbre = Array Int [Int]
type ArbreM = IOArray Int [Int]

main :: IO ()
main = timeIt $ do
    n <- readLn :: IO Int
    -- Liste de couples n° contenu (= fils), n° contenant (= père)
    liste <- fmap (zip [1..n] . map read . words) getLine :: IO [(Int, Int)]
    -- Crée l'arbre
    arbreM <- newArray (0, n) [] :: IO ArbreM
    sequence (map (initialiser arbreM) liste)
    -- Transforme l'arbre en immutable array
    arbre <- freeze arbreM :: IO Arbre
    masque <- getLine
    
    -- Affiche les fils niveau par niveau à partir de la racine
    afficher arbre [0] masque
    putStrLn ""

-- Ajoute contenu dans la liste des fils du noeud n° i de l'arbre.    
initialiser :: ArbreM -> (Int, Int) -> IO ()
initialiser arbre (contenu, i) = do
    fils <- readArray arbre i
    writeArray arbre i (contenu:fils)

-- Affiche les fils niveau par niveau
afficher :: Arbre -> [Int] -> String -> IO ()
afficher _ [] _ = return ()
afficher arbre peres masque = do
    let fils = foldr (\n f -> f ++ arbre!n) [] peres
    filtrer fils masque
    afficher arbre fils masque

-- Affiche uniquement les numéros de noeuds compatibles avec le masque
filtrer :: [Int] -> String -> IO ()
filtrer [] _ = return ()
filtrer (n:ns) masque = do
    let chaine = show n
    if length chaine == length masque && and (zipWith (\c1 c2 -> c1 == '?' || c1 == c2) masque chaine)
    then putStr $ chaine ++ " "
    else return ()
    filtrer ns masque
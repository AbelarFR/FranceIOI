--------------------------------------------------------------------------------
-- Name:        Densité du plastique
-- Purpose:     France-IOI niveau 3.6
--
-- Author:      Sébastien
--
-- Created:     24/09/2022
--------------------------------------------------------------------------------
import Data.List
import Control.Monad

-- Retourne la valeur la plus proche
proche :: (Ord a, Num a) => a -> a -> a -> a
proche v v1 v2 = if (v - v1) <= (v2 - v) then v1 else v2

-- Recherche une valeur dans une liste par dichotomie
-- Retourne la valeur la plus proche trouvée
rechercher :: (Ord a, Num a) => a -> [a] -> Int -> Int -> a
rechercher x xs debut fin
    | debut == fin     = xs !! debut
    | debut + 1 == fin = proche x (xs !! debut) (xs !! fin)
    | otherwise =
            let moitie = (fin + debut) `div` 2
                milieu = xs !! moitie
            in if x < milieu then rechercher x xs debut moitie
                else rechercher x xs moitie fin

-- Récupère une valeur sur l'entrée standard et regarde si présente dans une liste        
traiter :: (Read a, Ord a, Num a, Show a) => [a] -> IO()
traiter xs = do
    x <- readLn
    print $ rechercher x xs 0 (length xs - 1)

main :: IO()
main = do
    n <- readLn :: IO Int
    ligne <- getLine
    let densites = sort (map read (words ligne)) :: [Int]
    q <- readLn :: IO Int
    replicateM_ q $ traiter densites
    
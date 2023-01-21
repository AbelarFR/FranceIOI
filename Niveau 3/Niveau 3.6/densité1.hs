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

-- Recherche une valeur dans une liste par dichotomie
-- Retourne 1 si la valeur est présente dans la liste, 0 sinon
rechercher :: Ord a => a -> [a] -> Int -> Int -> Int
rechercher x xs debut fin =
    let moitie = (fin + debut) `div` 2
        milieu = xs !! moitie
     in if x == milieu then 1
        else if x < milieu && debut < moitie then rechercher x xs debut (moitie-1)
        else if x > milieu &&   fin > moitie then rechercher x xs (moitie+1) fin
        else 0

-- Récupère une valeur sur l'entrée standard et regarde si présente dans une liste        
traiter :: (Read a, Ord a) => [a] -> IO()
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
    
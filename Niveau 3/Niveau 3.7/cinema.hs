--------------------------------------------------------------------------------
-- Name:        Carte de cinéma
-- Purpose:     France-IOI niveau 3.7
--
-- Author:      Sébastien
--
-- Created:     29/09/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List
import qualified Data.Set as Set

main :: IO()
main = do  
    n <- readLn :: IO Int
    cartes <- fmap (map read . words) getLine :: IO [Int]
    print $ rechercherTricheur cartes Set.empty
    
-- Recherche des numéros de carte dans une liste
-- Retourne le numéro de la carte en double, -1 sinon
rechercherTricheur :: [Int] -> Set.Set Int -> Int
rechercherTricheur [] _ = -1
rechercherTricheur (x:xs) cartes = if Set.member x cartes then x
                                 else rechercherTricheur xs (Set.insert x cartes)
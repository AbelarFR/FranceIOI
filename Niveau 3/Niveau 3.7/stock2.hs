--------------------------------------------------------------------------------
-- Name:        État du stock
-- Purpose:     France-IOI niveau 3.7
--
-- Author:      Sébastien
--
-- Created:     24/09/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List

-- Applique une opération sur la ième valeur de la liste
modifier :: [Int] -> Int -> Int -> [Int]
modifier liste indice operation = 
    (take indice liste) ++ [liste!!indice + operation] ++ (drop (indice+1) liste)

traiter :: Int -> [Int] -> IO [Int]
traiter 0 stock = return stock
traiter q stock = do
    stock' <- traiter (q-1) stock
    (produit:operation:_) <- fmap (map read . words) getLine :: IO [Int]
    -- putStrLn $ "Opération #" ++ show q ++ ": produit " ++ show produit ++ " -> " ++ show operation
    return $ modifier stock' (produit-1) operation

main :: IO()
main = do
    -- Lit le stock initial
    n <- readLn :: IO Int
    stock <- fmap (map read . words) getLine :: IO [Int]
    
    -- Réalise les opérations sur le stock
    q <- readLn :: IO Int
    newStock <- traiter q stock
    
    -- Affiche le stock final
    putStrLn $ intercalate " " (map show newStock)
    
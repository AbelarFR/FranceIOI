--------------------------------------------------------------------------------
-- Name:        Galerie souterraine
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     22/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.Array

type Coord = (Int, Int) -- (y: ligne, x: colonne)

main :: IO ()
main = do
    (h:l:d:_) <- fmap (map read . words) getLine :: IO [Int]
    plan <- fmap (listArray ((0,0), (h-1,l-1)) . map read . words) getContents :: IO (Array Coord Int)
    afficher plan (-1, -1) (0, 0) (h, l) 1 (d+1)
    
afficher :: Array Coord Int -- Plan
         -> Coord           -- La position précédente (pour tester si on revient en arrière)
         -> Coord           -- La position courante
         -> Coord           -- La taille du plan
         -> Int             -- Le nombre de cases visitées
         -> Int             -- La distance entre deux conduits d'aération
         -> IO ()
afficher plan prec position taille n d = do
    if n `mod` d == 0 
    then putStrLn $ show (fst position) ++ " " ++ show (snd position)
    else return ()
    case avancer plan prec position taille of
        Just a -> afficher plan position a taille (n+1) d
        Nothing -> return ()
    
avancer :: Array Coord Int -- Plan
        -> Coord           -- La position précédente (pour tester si on revient en arrière)
        -> Coord           -- La position courante
        -> Coord           -- La taille du tableau
        -> Maybe Coord     -- La position suivante
avancer plan prec (y, x) (h, l)
    | y == h-1 && x == l-1                              = Nothing
    | x < l-1 && plan!(y, x+1) == 0 && (y, x+1) /= prec = Just (y, x+1)
    | x > 0   && plan!(y, x-1) == 0 && (y, x-1) /= prec = Just (y, x-1)
    | y < h-1 && plan!(y+1, x) == 0 && (y+1, x) /= prec = Just (y+1, x)
    | otherwise                                         = Just (y-1, x)

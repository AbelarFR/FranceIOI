--------------------------------------------------------------------------------
-- Name:        Les bons milieux
-- Purpose:     France-IOI niveau 3.9
--
-- Author:      Sébastien
--
-- Created:     11/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.Array

type Point = (Int,Int)
taille = 100

main :: IO()
main = do
    nbPoints <- readLn :: IO Int
    liste <- replicateM nbPoints lirePoint
    let plan = listArray ((0,0), (taille,taille)) (repeat False)
    let plan' = plan // [(point, True) | point <- liste]
    let nbMilieux = foldr (\p n -> n + (estMilieu p liste plan')) 0 liste
    print nbMilieux
    
lirePoint :: IO Point
lirePoint = do (x:y:_) <- fmap (map read . words) getLine :: IO [Int]
               return (x,y)

estMilieu :: Point -> [Point] -> Array Point Bool -> Int -- Retourne 1 si le point est milieu, 0 sinon
estMilieu _ [] _ = 0
estMilieu p (q:qs) plan
    | p == q = estMilieu p qs plan
    | otherwise = let xs = 2 * fst p - fst q
                      ys = 2 * snd p - snd q
                  in if xs >= 0 && xs <= taille && ys >= 0 && ys <= taille && plan ! (xs,ys)
                     then 1
                     else estMilieu p qs plan                  
    
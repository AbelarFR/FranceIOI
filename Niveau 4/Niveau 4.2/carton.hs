--------------------------------------------------------------------------------
-- Name:        Retrouver un produit
-- Purpose:     France-IOI niveau 4.2
--
-- Author:      Sébastien
--
-- Created:     27/01/2023
--------------------------------------------------------------------------------

import Control.Monad
import Data.List
import Data.Array.Unboxed

main :: IO ()
main = do
    nbObjets <- readLn :: IO Int
    contenants <- fmap (listArray (1, nbObjets) . map read . words) getLine :: IO (Array Int Int)
    
    nbRecherches <- readLn :: IO Int
    replicateM_ nbRecherches
        (do
            objet1:objet2:_ <- fmap (map read . words) getLine :: IO [Int]
            let peres = zip (listerPeres contenants objet1) (listerPeres contenants objet2)
                communs = takeWhile (\(x,y) -> x == y) peres
            print $ snd (last communs)
        )
    

listerPeres :: Array Int Int -> Int -> [Int]
listerPeres _ 0 = [0]
listerPeres contenants n = (listerPeres contenants (contenants!n)) ++ [n]
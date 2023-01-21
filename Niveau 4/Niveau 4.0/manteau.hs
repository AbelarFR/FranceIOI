--------------------------------------------------------------------------------
-- Name:        Choisir son manteau
-- Purpose:     France-IOI niveau 4.0
--
-- Author:      Sébastien
--
-- Created:     20/11/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List
import Data.Array.Unboxed

main :: IO ()
main = do
    nbManteaux <- readLn :: IO Int
    manteaux <- fmap (zip [1..nbManteaux]) $ replicateM nbManteaux $ fmap (map read . words) $ getLine :: IO [(Int,[Int])]
  
    let manteauxMini = sortBy (\(_,deb1) (_,deb2) -> compare deb1 deb2) $ map (\(n,(deb:_)) -> (n,deb)) manteaux
        rangMini = array (1,nbManteaux) (rang 0 (0,0) manteauxMini) :: Array Int Int
    
        manteauxMaxi = sortBy (\(_,fin1) (_,fin2) -> compare fin2 fin1) $ map (\(n,(_:fin:_)) -> (n,fin)) manteaux
        rangMaxi = array (1,nbManteaux) (rang 0 (0,0) manteauxMaxi) :: Array Int Int
    
        amplitudes = [nbManteaux - 1 - rangMini!i - rangMaxi!i | i <- [1..nbManteaux]]
    print $ maximum amplitudes
    

rang :: Int -> (Int, Int) -> [(Int, Int)] -> [(Int, Int)]
rang _ _ [] = []
rang i (rPrec, valPrec) ((n,val):xs) = (n, r):rang (i+1) (r,val) xs
    where r = if val == valPrec then rPrec else i
--------------------------------------------------------------------------------
-- Name:        Hydroélectricité
-- Purpose:     France-IOI niveau 3.8
--
-- Author:      Sébastien
--
-- Created:     01/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List

main :: IO()
main = do  
    n:e:_ <- fmap (map read . words) getLine :: IO [Int]
    ecrire_crochets n e
    
ecrire_crochets :: Int -> Int -> IO()
ecrire_crochets n 0 = putStr $ show n
ecrire_crochets n e = do
       putStr "["
       ecrire_crochets n (e-1)
       putStr "]"


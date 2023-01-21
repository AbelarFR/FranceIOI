--------------------------------------------------------------------------------
-- Name:        Entre deux
-- Purpose:     France-IOI niveau 3.8
--
-- Author:      Sébastien
--
-- Created:     04/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List

main :: IO()
main = do  
    n:m:_ <- fmap (map read . words) getLine :: IO [Int]
    ecrireEntiers n m
    
ecrireEntiers :: Int -> Int -> IO()
ecrireEntiers n m
    | n <= m = do
               putStr $ show n ++ " "
               ecrireEntiers (n+1) m
    | otherwise = return ()

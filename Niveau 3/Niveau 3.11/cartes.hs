--------------------------------------------------------------------------------
-- Name:        Cartes perforées
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     21/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.Char

main :: IO ()
main = do
    n <- readLn :: IO Int
    replicateM_ n traiterLigne
    putStrLn ""
    
traiterLigne :: IO ()
traiterLigne = do
    ligne <- getLine
    putStr $ traiterColonne ligne 0
    
traiterColonne :: String -> Int -> String
traiterColonne [] _ = []
traiterColonne (x:xs) i
    | x == 'O'  = chr(ord 'A' + i):(traiterColonne xs (i+1))
    | otherwise = traiterColonne xs (i+1)

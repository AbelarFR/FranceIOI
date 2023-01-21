--------------------------------------------------------------------------------
-- Name:        Dates de péremption
-- Purpose:     France-IOI niveau 3.7
--
-- Author:      Sébastien
--
-- Created:     25/09/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List

traiter :: Int -> [Int] -> IO [Int]
traiter 0 pile = return pile
traiter o pile = do
    pile' <- traiter (o-1) pile
    (n:date:_) <- fmap (map read . words) getLine :: IO [Int]
    -- putStrLn $ "Opération #" ++ show o ++ ": nombre = " ++ show n ++ ", date = " ++ show date
    return $ if n > 0 then (replicate n date) ++ pile' else drop (-n) pile'

main :: IO()
main = do  
    -- Réalise les opérations sur la pile
    o <- readLn :: IO Int
    pile <- traiter o []
    
    -- Affiche le stock final
    print $ minimum pile

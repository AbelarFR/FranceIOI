--------------------------------------------------------------------------------
-- Name:        Distributeur automatique
-- Purpose:     France-IOI niveau 3.7
--
-- Author:      Sébastien
--
-- Created:     25/09/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List

traiter :: Int -> [Int] -> IO [Int]
traiter 0 file = return file
traiter o file = do
    file' <- traiter (o-1) file
    (n:date:_) <- fmap (map read . words) getLine :: IO [Int]
    -- putStrLn $ "Opération #" ++ show o ++ ": nombre = " ++ show n ++ ", date = " ++ show date
    return $ if n > 0 then (replicate n date) ++ file' else take ((length file') - (-n)) file'

main :: IO()
main = do  
    -- Réalise les opérations sur la file
    o <- readLn :: IO Int
    file <- traiter o []
    
    -- Affiche le stock final
    print $ minimum file

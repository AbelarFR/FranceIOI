--------------------------------------------------------------------------------
-- Name:        Boîtes factorielles
-- Purpose:     France-IOI niveau 4.0
--
-- Author:      Sébastien
--
-- Created:     13/11/2022
--------------------------------------------------------------------------------

import Data.Array.Unboxed
import Data.List

maxNbCoeff = 12
factorielles :: Array Int Int
factorielles = a where a = array (1, maxNbCoeff) ((1, 1):[(i, i*a!(i-1)) | i <- [2..maxNbCoeff]])

main :: IO ()
main = do
    n <- readLn :: IO Int
    let decomposition = reverse . dropWhile (== 0) $ decompose n maxNbCoeff
    print $ length decomposition
    putStrLn $ intercalate " " . map show $ decomposition
    
decompose :: Int -> Int -> [Int]
decompose _ 0 = []
decompose n p =
    (n `div` factorielles!p):decompose (n `mod` factorielles!p) (p-1)
    
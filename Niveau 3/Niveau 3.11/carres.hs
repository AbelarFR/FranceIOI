--------------------------------------------------------------------------------
-- Name:        Carrés concentriques
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     23/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.Array

main :: IO ()
main = do
    n <- readLn :: IO Int
    mot <- fmap (listArray (0, n-1)) getLine
    let carre = foldr (\y ys -> foldr (afficherCaractere mot y) "" [(1-n)..(n-1)]:ys) [] [(1-n)..(n-1)]
    putStr $ unlines carre
    
afficherCaractere :: Array Int Char -> Int -> Int -> String -> String
afficherCaractere mot y x xs = (mot!(max (abs x) (abs y))):xs
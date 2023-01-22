--------------------------------------------------------------------------------
-- Name:        Retrouver un produit
-- Purpose:     France-IOI niveau 4.2
--
-- Author:      Sébastien
--
-- Created:     22/01/2023
--------------------------------------------------------------------------------

import Control.Monad
import Data.List
import Data.Array.Unboxed

main :: IO ()
main = do
    nbObjets <- readLn :: IO Int
    listeObjets <- fmap (map read . words) $ getLine :: IO [Int]
    let objets = array (1, nbObjets) (zip [1..nbObjets] listeObjets) :: Array Int Int
    print objets
    
    
--------------------------------------------------------------------------------
-- Name:        Installation du camping
-- Purpose:     France-IOI niveau 4.0
--
-- Author:      Sébastien
--
-- Created:     11/11/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List
import Data.Array.Unboxed
import System.TimeIt

type Coord = (Int, Int)
type Plan = Array Coord Int

main :: IO ()
main = timeIt (do
    (l:c:_) <- fmap (map read . words) getLine :: IO [Int]
    plan <- fmap (listArray ((1,1), (l,c)) . map read . words) getContents :: IO Plan
    print $ maximum (carres plan))

carres :: Plan -> Array Coord Int
carres plan =
    let (_, (l,c)) = bounds plan
        a = array ((1,1), (l,c))
                ([((1,x), 1-plan!(1,x)) | x <- [1..c]] ++
                 [((y,1), 1-plan!(y,1)) | y <- [2..l]] ++
                 [((y,x), if plan!(y,x) == 1 
                          then 0
                          else 1 + (minimum [a!(y,x-1), a!(y-1,x-1), a!(y-1,x)]))
                                        | y <- [2..l], x <- [2..c]])
    in a

--------------------------------------------------------------------------------
-- Name:        Rallonges audio
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     29/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List

main :: IO ()
main = do
    _ <- readLn :: IO Int
    lignes <- fmap lines getContents
    let (longueur, femelles, males) = foldr lireLigne (0, [], []) lignes
        femelles' = sort femelles
        males' = sort males
        f = length femelles'
        m = length males'
        n = min f (m - 1)
    if n > -1 then
        print $ longueur + sum (drop (m - 1 - n) males') + sum (drop (f - n) femelles')
    else print (-1)
    
    
lireLigne :: String -> (Int, [Int], [Int]) -> (Int, [Int], [Int])
lireLigne ligne (longueur, femelles, males) =
    let (c1:c2:l:_) = map read (words ligne) :: [Int] in
    if c1 /= c2 then (longueur+l, femelles, males)
    else if c1 == 0 then (longueur, l:femelles, males)
    else (longueur, femelles, l:males)
    
  
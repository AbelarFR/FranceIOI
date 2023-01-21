--------------------------------------------------------------------------------
-- Name:        Lecture binaire
-- Purpose:     France-IOI niveau 3.10
--
-- Author:      Sébastien
--
-- Created:     16/10/2022
--------------------------------------------------------------------------------

main :: IO()
main = do
    s <- getLine   
    print $ foldl (\n c -> 2*n + (if c == '1' then 1 else 0)) 0 s

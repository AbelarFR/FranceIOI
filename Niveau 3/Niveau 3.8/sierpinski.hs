--------------------------------------------------------------------------------
-- Name:        Fractale : triangle de Sierpinski
-- Purpose:     France-IOI niveau 3.8
--
-- Author:      Sébastien
--
-- Created:     03/10/2022
--------------------------------------------------------------------------------

sierpinski :: Int -> [String]
sierpinski 1 = ["#"]
sierpinski n = let n' = n `div` 2
                   triangle = sierpinski n' 
                   vide = replicate n' (replicate n' ' ')
               in (zipWith (++) triangle triangle) ++ (zipWith (++) triangle vide)

main :: IO()
main = do  
    n <- readLn :: IO Int
    let fractale = sierpinski n
    putStr $ unlines fractale
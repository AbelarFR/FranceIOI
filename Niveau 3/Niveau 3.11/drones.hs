--------------------------------------------------------------------------------
-- Name:        Essaim de drones
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     06/11/2022
--------------------------------------------------------------------------------

import Control.Monad
import Data.List
type Point = (Int, Int)
type Translation = (Int, Int)
type Max = (Int, Point)

main :: IO ()
main = do
    (l:c:_) <- fmap (map read . words) getLine :: IO [Int]
    image1 <- replicateM l $ fmap words getLine
    image2 <- replicateM l $ fmap words getLine
    let points1 = lirePoints image1 1
        points2 = lirePoints image2 1
        translations = [(y2-y1, x2-x1) | (y1, x1) <- points1, (y2, x2) <- points2]
        translations_sorted = sort translations
        maxi = rechercherMax translations_sorted (0, (0, 0))  (0, (0, 0))
    print $ fst maxi
    afficherPoints points1 points2 (snd maxi)

lirePoints :: [[String]] -> Int -> [Point]
lirePoints [] _ = []
lirePoints (l:ls) y = (lirePoints' l y 1)++ lirePoints ls (y+1)

lirePoints' :: [String] -> Int -> Int -> [Point]
lirePoints' [] _ _ = []
lirePoints' (c:cs) y x = if c == "1" then (y,x):lirePoints' cs y (x+1) else lirePoints' cs y (x+1)

rechercherMax :: [Translation] -> Max -> Max -> Max
rechercherMax [] _ m = m
rechercherMax (t:ts) precedent m =
    let n = if t == snd precedent then (fst precedent) + 1 else 1
    in if n > fst m
       then rechercherMax ts (n, t) (n, t)
       else rechercherMax ts (n, t) m

afficherPoints :: [Point] -> [Point] -> Translation -> IO ()
afficherPoints [] _ _ = return ()
afficherPoints (p:ps) points2 translation = do
    afficherPoints' p points2 translation
    afficherPoints ps points2 translation

afficherPoints' :: Point -> [Point] -> Translation -> IO ()
afficherPoints' _ [] _ = return ()
afficherPoints' (y1,x1) ((y2,x2):ps) (dy,dx) =
    if y2-y1 == dy && x2-x1 == dx
    then putStrLn $ show y2 ++ " " ++ show x2
    else afficherPoints'(y1,x1) ps (dy,dx)
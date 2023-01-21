--------------------------------------------------------------------------------
-- Name:        Moyenne hexadécimale
-- Purpose:     France-IOI niveau 3.10
--
-- Author:      Sébastien
--
-- Created:     16/10/2022
--------------------------------------------------------------------------------

import Data.Char

main :: IO()
main = do
    n <- fmap lireHexa getLine
    valeurs <- fmap (map lireHexa . lines) getContents :: IO [Int]
    putStrLn $ ecrireHexa ((sum valeurs) `div` n)

lireHexa :: String -> Int
lireHexa s = foldl (\n c -> 16*n + valHexa(c)) 0 s
    
valHexa :: Char -> Int
valHexa c
    | c `elem` "0123456789" = ord(c) - ord('0')
    | c `elem` "ABCDEF" = ord(c) - ord('A') + 10
    
ecrireHexa :: Int -> String
ecrireHexa n
    | n < 16 = [carHexa n]
    | otherwise = ecrireHexa (n `div` 16) ++ [carHexa (n `mod` 16)]

carHexa :: Int -> Char
carHexa n
    | n < 10 = chr (n + (ord '0'))
    | otherwise = chr ((n-10) + (ord 'A'))
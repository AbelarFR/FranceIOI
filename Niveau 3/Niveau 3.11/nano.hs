--------------------------------------------------------------------------------
-- Name:        iPhone Nano
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     31/10/2022
--------------------------------------------------------------------------------

main :: IO ()
main = do
    d <- readLn :: IO Int
    lignes <- fmap lines getContents
    let dico = take d lignes
        -- Ignore la ligne avec le nombre de groupes de lettres
        lettres = drop (d+1) lignes
    putStrLn . head . dropWhile (not . tester lettres) $ dico
    
tester :: [String] -> String -> Bool
tester [] [] = True
tester _ [] = False
tester [] _ = False
tester (l:lettres) (m:mot) 
    | m `elem` l = tester lettres mot
    | otherwise = False
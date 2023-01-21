--------------------------------------------------------------------------------
-- Name:        Baguenaudier
-- Purpose:     France-IOI niveau 4.0
--
-- Author:      Sébastien
--
-- Created:     19/11/2022
--------------------------------------------------------------------------------

main :: IO ()
main = do
    n <- readLn :: IO Int
    vider n
   
-- Vide les k premières cases   
vider :: Int -> IO ()
vider k
    | k > 0 = do
        vider (k-2)
        print k -- Enlève la pierre de la case n° k
        remplir (k-2)
        vider (k-1)
    | otherwise = return ()

-- Remplit les k premières cases
remplir :: Int -> IO ()
remplir k
    | k > 0 = do
        remplir (k-1)
        vider (k-2)
        print k -- Pose la pierre de la case n° k
        remplir (k-2)
    | otherwise = return ()

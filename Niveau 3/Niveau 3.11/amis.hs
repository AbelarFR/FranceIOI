--------------------------------------------------------------------------------
-- Name:        Amis d’amis
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     31/10/2022
--------------------------------------------------------------------------------

import Data.Set (insert, empty, member, notMember)

main :: IO ()
main = do
    i <- readLn :: IO Int
    _ <- readLn :: IO Int
    lignes <- fmap lines getContents
    let relations = foldr (\l r -> let (i1:i2:_) = map read . words $ l :: [Int]
                                   in (i1,i2):(i2,i1):r) [] lignes
        amis = foldr (\(i1, i2) s -> if i1 == i then insert i2 s else s) empty relations
        amis2 = foldr (\(i1, i2) s -> if i2 /= i && i1 `member` amis && i2 `notMember` amis then insert i2 s else s) empty relations
    print $ length amis2
    
    
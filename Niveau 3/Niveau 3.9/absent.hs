--------------------------------------------------------------------------------
-- Name:        Premier absent
-- Purpose:     France-IOI niveau 3.9
--
-- Author:      Sébastien
--
-- Created:     11/10/2022
--------------------------------------------------------------------------------

import Control.Monad
import qualified Data.Vector.Unboxed as V
import           Data.Vector.Unboxed ((!), (//))
import qualified Data.Vector.Unboxed.Mutable as M
import System.TimeIt

main :: IO()
main = timeIt $ do
    (n:p:_) <- fmap (map read . words) getLine :: IO [Int]
    -- let eleves = V.replicate (p+1) False
    eleves <- M.replicate (p+1) False
    noterEleve' n p eleves 1

noterEleve :: Int -> Int -> V.Vector Bool -> Int -> IO()
noterEleve _ 0 _ _ = return ()
noterEleve n p eleves absent = do
    e <- readLn :: IO Int
    let eleves' = if e <= (V.length eleves) then eleves // [(e -1, True)] else eleves
    let absent' = chercherAbsent absent eleves'
    print $ if absent' > n then -1 else absent'
    noterEleve n (p-1) eleves' absent'
    
chercherAbsent :: Int -> V.Vector Bool -> Int
chercherAbsent n eleves = if not (eleves ! (n-1)) then n else chercherAbsent (n+1) eleves
    

noterEleve' :: Int -> Int -> M.MVector (M.PrimState IO) Bool -> Int -> IO()
noterEleve' _ 0 _ _ = return ()
noterEleve' n p eleves absent = do
    e <- readLn :: IO Int
    if e <= (M.length eleves) then M.write eleves (e-1) True else return () :: IO ()
    absent' <- chercherAbsent' absent eleves
    print $ if absent' > n then -1 else absent'
    noterEleve' n (p-1) eleves absent'
    
chercherAbsent' :: Int -> M.MVector (M.PrimState IO) Bool -> IO Int
chercherAbsent' n eleves = do
                eleve <- M.read eleves (n-1)
                if not eleve then return n else chercherAbsent' (n+1) eleves
 
--------------------------------------------------------------------------------
-- Name:        Fibre optique
-- Purpose:     France-IOI niveau 4.2
--
-- Author:      Sébastien
--
-- Created:     29/01/2023
--------------------------------------------------------------------------------

import Data.Array
import Data.Array.IO
import Control.Monad
import System.TimeIt
import Debug.Trace

type Arbre = Array Int [Int]
type ArbreM = IOArray Int [Int]

main :: IO ()
main = timeIt $ do
    nbNoeuds <- readLn :: IO Int
    arbreM <- newArray (0, nbNoeuds-1) [] :: IO ArbreM
    liste <- replicateM (nbNoeuds-1) (fmap (map read . words) getLine) :: IO [[Int]]
    sequence (map (initialiser arbreM) liste)
    arbre <- freeze arbreM :: IO Arbre
--  print arbre
    let (_, resultat) = compter arbre (-1) 0 nbNoeuds
    print resultat

-- Ajoute dans l'arbre la relation entre deux noeuds
initialiser :: ArbreM -> [Int] -> IO ()
initialiser arbre (noeud1:noeud2:_) = do
    voisins1 <- readArray arbre noeud1
    writeArray arbre noeud1 (noeud2:voisins1)
    voisins2 <- readArray arbre noeud2
    writeArray arbre noeud2 (noeud1:voisins2)
    
-- Compte le nombre de PC dans chaque branche qui part de 'noeud'
-- et retient le maximum (tailleMax).
-- Retourne le nombre de PC dans la branche dont 'noeud' est la racine et le minimum des "tailleMax".
compter :: Arbre -> Int -> Int -> Int -> (Int, Int)
-- compter arbre pere noeud resultatIn | trace ("IN  compter " ++ show pere ++ " " ++ show noeud ++ " " ++ show resultatIn) False = undefined
compter arbre pere noeud resultatIn =
    let voisins = arbre!noeud
        (tailleTotale, tailleMax, resultat') = foldr 
            (\voisin (compteur, maxi, result) -> 
                if voisin /= pere 
                then let (tailleBranche, result') = compter arbre noeud voisin result
                     in (compteur + tailleBranche, max tailleBranche maxi, result')
                else (compteur, maxi, result))
            (1, 0, resultatIn)
            voisins
        tailleArbre = (snd (bounds arbre)) + 1
        tailleMax' = max tailleMax (tailleArbre - tailleTotale)
        resultatOut = min tailleMax' resultat'
    in -- trace ("OUT compter " ++ show tailleTotale ++ " " ++ show resultatOut) -- 
    (tailleTotale, resultatOut)
    
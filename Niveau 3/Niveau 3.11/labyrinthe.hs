--------------------------------------------------------------------------------
-- Name:        Labyrinthe à billes
-- Purpose:     France-IOI niveau 3.11
--
-- Author:      Sébastien
--
-- Created:     01/11/2022
--------------------------------------------------------------------------------

import Data.Array.Unboxed
import Data.List
import Control.Monad
import qualified Data.Map as M

type Coord = (Int, Int)
type Plan = Array Coord Char

mur   = '#'
vide  = '.'
trou  = 'O'
bille = 'x'
deplacements = M.fromList[('N', (-1,0)), ('S', (1,0)), ('O', (0,-1)), ('E', (0,1))   ]

main :: IO ()
main = do
    (l:c:_) <- fmap (map read . words) getLine :: IO [Int]
    contenu <- fmap (filter (flip elem [mur, vide, trou, bille]) . unlines) $ replicateM l getLine
    let labyrinthe = listArray ((1,1), (l,c)) contenu :: Plan
        is = indices labyrinthe
        billes = foldr (\i bs -> if labyrinthe!i == bille then i:bs else bs) [] is
        labyrinthe' = labyrinthe // zip billes (repeat vide)
    putStrLn $ show billes
    _ <- readLn :: IO Int
    directions <- getLine
    billes' <- deplacerBilles labyrinthe directions billes
    print $ length billes'

-- Enchaîne une série de déplacement
deplacerBilles :: Plan -> String -> [Coord] -> IO [Coord]
deplacerBilles _ [] billes = return billes
deplacerBilles labyrinthe (direction:ds) billes = do
    let billes' = deplacerBilles' labyrinthe direction billes
    putStrLn $ show billes ++ " -> " ++ direction:"" ++ " -> " ++ show billes'
    deplacerBilles labyrinthe ds billes'

-- Déplace toutes les billes dans une direction
deplacerBilles' :: Plan -> Char -> [Coord] -> [Coord]
deplacerBilles' labyrinthe direction billes =
    case M.lookup direction deplacements of
        -- Just deplacement -> map (deplacerBille labyrinthe deplacement billes) billes
        Just deplacement -> let billes' = trierBilles direction billes
                            in foldr (\b bs -> case deplacerBille labyrinthe deplacement bs b of
                                                    Just bi -> bi:bs
                                                    Nothing -> bs)
                                     []
                                     billes
        Nothing -> billes

-- Trie la liste des billes en mettant à droite les billes qui vont se déplacer devant
trierBilles :: Char -> [Coord] -> [Coord]
trierBilles 'N' billes = sortBy (\(y1,_) (y2,_) -> compare y2 y1) billes
trierBilles 'S' billes = sortBy (\(y1,_) (y2,_) -> compare y1 y2) billes
trierBilles 'E' billes = sortBy (\(_,x1) (_,x2) -> compare x2 x1) billes
trierBilles 'O' billes = sortBy (\(_,x1) (_,x2) -> compare x1 x2) billes

-- Déplace une bille dans une direction
deplacerBille :: Plan -> Coord -> [Coord] -> Coord -> Maybe Coord
deplacerBille labyrinthe deplacement billes position = do
    let suivant = (fst position + fst deplacement, snd position + snd deplacement)
    if labyrinthe!suivant == trou
        then Nothing
    else if labyrinthe!suivant == vide && not (suivant `elem` billes)
        then deplacerBille labyrinthe deplacement billes suivant
        else Just position
                                  

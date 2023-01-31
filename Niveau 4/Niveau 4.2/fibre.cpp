//------------------------------------------------------------------------------
// Name:        Fibre optique
// Purpose:     France-IOI niveau 4.2
//
// Author:      Sébastien
//
// Created:     29/01/2023
//------------------------------------------------------------------------------

#include <iostream>
#include <vector>
using namespace std;

const int MAX_TAILLE = 100*1000;

vector<int> arbre[MAX_TAILLE];
int nbNoeuds = 0;
int resultat = 0;

// Compte le nombre de PC dans chaque branche qui part de 'noeud'
// et retient le maximum.
// Retourne le nombre de PC dans la branche dont 'noeud' est la racine.
int compter(int pere, int noeud)
{
    int compteur = 1;
    int tailleBrancheMax = 0;
    for (int voisin : arbre[noeud])
    {
        if (voisin != pere)
        {
            int tailleBranche = compter(noeud, voisin);
            if (tailleBrancheMax < tailleBranche) tailleBrancheMax = tailleBranche;
            compteur += tailleBranche;
        }
    }
    if (tailleBrancheMax < nbNoeuds - compteur) tailleBrancheMax = nbNoeuds - compteur;
    if (resultat > tailleBrancheMax) resultat = tailleBrancheMax;
    return compteur;
}

int main()
{
    // Crée l'arbre.
    cin >> nbNoeuds;
    for (int i = 0; i < nbNoeuds-1; i++)
    {
        int noeud1, noeud2;
        cin >> noeud1 >> noeud2;
        arbre[noeud1].push_back(noeud2);
        arbre[noeud2].push_back(noeud1);
    }
    
    resultat = nbNoeuds;
    compter(-1, 0);
    cout << resultat << endl;
}

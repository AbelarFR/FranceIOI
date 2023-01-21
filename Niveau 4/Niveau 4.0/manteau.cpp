#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_TAILLE = 20000;

struct Manteau {
    int inf;
    int sup;
};
bool operator<(const Manteau& m1, const Manteau& m2)
{
    return m1.inf < m2.inf || (m1.inf == m2.inf && m1.sup > m2.sup);
}

Manteau manteaux[MAX_TAILLE];

int main()
{
    int nbManteaux;
    cin >> nbManteaux;
    for (int i = 0; i < nbManteaux; i++)
    {
        cin >> manteaux[i].inf >> manteaux[i].sup;
    }
    sort(manteaux, manteaux + nbManteaux);

    int nmax = 0;
    for (int i = 0; i < nbManteaux; )
    {
        int niveau = 0;
        int suivant = -1;
        
        int j = i+1;
        for (; j < nbManteaux && manteaux[j].inf <= manteaux[i].sup; j++)
        {
            if (manteaux[j].sup <= manteaux[i].sup)
            {
                niveau++;
            } else if (suivant == -1)
            {
                suivant = j;
            }
        }
        // cout << i << " " << manteaux[i].inf << " " << manteaux[i].sup << " " << niveau << endl;
        i = (suivant == -1) ? j : suivant;
        if (niveau > nmax) nmax = niveau;
    }
    cout << nmax << endl;

    
    return 0;
}
import pandas as pd
# Importation de la librairie pandas
from typing import List, Tuple, Dict # Importation des types de données
# Création des variables de travail
data = 'dataBruteForce.csv'
# Nom du fichier csv à traiter
Wallet =  500
# Création d'une variable Wallet qui contient la valeur de départ de notre portefeuille

# def read_data(data):
#     """Fonction qui lit le fichier csv et retourne un dataframe"""
#     df = pd.read_csv((data), sep=";")
#     df["Bénéfice_en_Euro"] = df["Coût_par_action"] * df["Bénéfice"] / 100
#     return df



df = pd.read_csv((data), sep=";")
df["Bénéfice_en_Euro"] = df["Coût_par_action"] * df["Bénéfice"] / 100


def tri_actions(df: List[Dict]) -> List[Dict]:
    """ Tri la liste de dictionnaires selon les rapports Coût_par_action/Bénéfice_en_Euro. """

    def recupere_rapports(df):
        return df['Bénéfice_en_Euro'] / df['Coût_par_action']

    action_trie = sorted(df, key=recupere_rapports)

    return action_trie

def algo_glouton(action_trie: List[Dict],
                          Wallet: float) -> Tuple[List[str], int, int]:
    """
    Construction du sac à dos à partir d'une stratégie gloultonne.
    HYPOTHÈSE : la liste de dictionnaires est triée par ordre croissant des rapports
    valeurs/masses.

    Retourne un tuple constitué d'une liste contenant les noms des df sélectionnés,
    de la valeur du sac à dos et de la masse du sac à dos.
    """
    Coût_par_action = 0
    bénéfice_euros = 0
    liste_action = []

    i = len(action_trie) - 1  # Compteur
    while i >= 0:
        df = action_trie[i]  # objet est un dictionnaire
        if (Coût_par_action + df["Coût_par_action"]) <= Wallet:
            bénéfice_euros += df["Bénéfice_en_Euro"]
            Coût_par_action += df["Coût_par_action"]
            liste_action.append(df['Nom'])

        i -= 1  # Décrémentation du compteur

    return (liste_action, bénéfice_euros, Coût_par_action)

def Coût_par_action(df: List[Dict[str, str]], liste_action: List[int]) -> int:
    """
    Calcule la masse du sac pour la liste d'df retenus.
    """
    cout = 0
    for i in range(len(df)):
        cout += df[i]['Coût_par_action'] * liste_action[i]

    return cout


def calcul_valeur_sac(df: List[Dict[str, str]],
                      liste_action: List[int]) -> int:
    """
    Calcule la masse du sac pour la liste d'df retenus.
    """
    valeur = 0
    for i in range(len(df)):
        valeur += df[i]['Bénéfice_en_Euro'] * liste_action[i]
    return valeur



def recherche_recursive(df: List[Dict[str, str]], Wallet: isinstance,
                        liste_action: List[int], i: int) -> List[int]:
    """
    Détermine le chemin de l'arbre de décision correspondant à la valeur optimale
    pour une masse du sac déterminée.
    """
    if i == len(df):
        return liste_action[:]

    val1 = -1  # Initialisation à une valeur impossible du poids
    if df[i]['Coût_par_action'] <= Wallet - Coût_par_action(
            df, liste_action):  # Ajoute objet si m_sac - m_inter > 0
        liste_action[i] = 1
        sol1 = recherche_recursive(df, Wallet, liste_action, i + 1)
        val1 = calcul_valeur_sac(df, sol1)

    liste_action[i] = 0  # On n'ajoute pas l'objet
    sol2 = recherche_recursive(df, Wallet, liste_action, i + 1)
    val2 = calcul_valeur_sac(df, sol2)

    if val1 > val2:
        return sol1[:]
    else:
        return sol2[:]

    df = tri_actions(df)
    print("Objets utilisables : {}".format(df), end='\n')


    # construction du sac à dos par stratégie gloutonne
    sac_a_dos, bénéfice_euros, Coût_par_action = algo_glouton(df, Wallet)



    # Conclusion de la mise en œuvre de la stratégie gloutonne
    print("Stratégie gloutonne")
    print("-------------------")
    print("Constitution du sac à dos : {}".format(sac_a_dos))
    print("Masse du sac à dos : {}".format(Coût_par_action))
    print("Valeur du sac à dos : {}".format(bénéfice_euros))
    print()


import pandas as pd
# Importation de la librairie pandas

# Création des variables de travail
data = 'dataBruteForce.csv'
# Nom du fichier csv à traiter
Wallet =  500
# Création d'une variable Wallet qui contient la valeur de départ de notre portefeuille

def read_data(data):
    df = pd.read_csv((data), sep=";")
    df["Bénéfice_en_Euro"] = df["Coût_par_action"] * df["Bénéfice"] / 100
    return df

print(read_data(data))


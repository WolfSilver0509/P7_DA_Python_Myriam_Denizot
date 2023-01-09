import csv

# Ouvrir le fichier CSV en mode lecture
with open('dataset1_Python+P7.csv', 'r') as f:
    # Créer un objet lecteur CSV
    reader = csv.reader(f)

    # Créer une liste vide pour accueillir les dictionnaires
    dict_list = []

    # Récupérer les en-têtes du fichier CSV
    headers = next(reader)

    # Boucle sur les lignes du fichier CSV
    for row in reader:
        # Créer un dictionnaire en utilisant les en-têtes comme clés et les valeurs de la ligne comme valeurs associées
        dict_list.append(dict(zip(headers, row)))

    # Fermer le fichier
    # print(dict_list)
    # print(headers)
    # f.close()

    # Condition pour que les prix inférieurs à zero soit supprimer
    for i in dict_list:
        if float(i['price']) <= 0:
            dict_list.remove(i)
            #print(dict_list)

    # crée une nouvelle entrée dans le dictionnaire pour le profit en euros
    for i in dict_list:
        i['profit_total'] = (float(i['price']) * float(i['profit'])) / 100
        print(dict_list)

    # ranger cette liste de dictionnaire par ordre décroissant de profit_total
    dict_list.sort_values(by=['profit_total'], ascending=False)



import csv

# Ouvrir le fichier CSV en mode lecture
with open('dataset1_Python+P7.csv', 'r') as f:
    # Créer un objet lecteur CSV
    reader = csv.reader(f)

    # Créer une liste vide pour accueillir les dictionnaires
    dict_list = []
    dict_list_v2 = []
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
        if float(i['price']) <= 0 and float(i['profit']) <= 0:
            dict_list.remove(i)
            dict_list_v2.append(dict_list)
            #print(dict_list)

    # crée une nouvelle entrée dans le dictionnaire pour le profit en euros
    for i in dict_list:
        i['profit_total'] = (float(i['price']) * float(i['profit'])) / 100
        print(dict_list)

    # ranger cette liste de dictionnaire par ordre décroissant de profit_total
    # dict_list.sort_values(by=['profit_total'], ascending=False)


    # enregistrer la liste dict dans un fichier csv

    data = [dict_list]

    #nom du fichier
    filename = "newCsv.csv"

    # le clé du dict comme nom de colonne
    fieldnames = dict_list_v2[0].keys()

    # ecriture dans le fichier csv
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in dict_list_v2:
            writer.writerow(row)

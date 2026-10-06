import csv

def main():
    print("1 - Listes")
    print("2 - Dictionnaires")
    print("3 - Fichiers")
    print("4 - Projet")
    print("0 - Quitter")
    choix = int(input("Votre choix : "))
    match choix:
        case 1:
            Listes()
            main()
        case 2:
            Dictionnaire()
            main()
        case 3:
            FichierExcel()
            main()
        case 4:
            Projet()
            main()
        case 0:
            print("Fin du programme")
            exit()
        case _:
            main()

def Listes():
    # Stats : moyenne, max, min, ...
    notes = [12, 15, 8, 17, 10]
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne : {moyenne}")
    print(f"Note maximale : {max(notes)}")
    print(f"Note minimale : {min(notes)}")
    
    # Parcourir
    for i,note in enumerate(notes):
        print(f"Note n° {i+1} : {note}")
        
    print("-" * 20)
    
    for i in range(5):
        print(f"Note n° {i+1} : {notes[i]}")
    
    print("-" * 20)
    
    for note in notes:
        print(note)
        
    
    # Divers
    print(f"Nb éléments : {len(notes)}")
    print(f"Nombre d'occurences du nombre 17 : {notes.count(17)}")
    print(f"Ajouter la note 7 : OK")
    notes.append(7)
    print(f"Valeur de l'indice en fonction de la valeur 17 : {notes.index(17)}")
    notes.remove(15)
    for note in notes:
        print(note)
    
    nbEtudiantsAdmis = sum(1 for note in notes if note >=10)
    print(f"Nombre d'étudiants admis : {nbEtudiantsAdmis}")
    nbBonsEtudiants = sum(1 for note in notes if ((note >=15) and (note <=20)))
    print(f"Nombre de bons étudiants : {nbBonsEtudiants}")
    
def Dictionnaire():
    # Création du dictionnaire
    dico = {}
    # Ajouter un élément
    dico["nom"] = "Martin"
    # Afficher l'élément
    print(f"Nom : {dico["nom"]}")
    
    employes = {"nom":"Martin","age":"28","salaire":"2693.67"}
    
    # parcourir les clés
    for cle in employes.keys():
        print(cle)
    
    # parcourir les valeurs
    for valeur in employes.values():
        print(valeur)
    
    # parcourir les deux : clés + valeur
    for cle,valeur in employes.items():
        print(f"{cle} : {valeur}")
    
    # Récupérer la valeur en fonction de la clé
    print(f"Valeur : {employes.get("age")}")

def FichierExcel():
    # Afficher toutes les lignes du fichier
    with open("TP1-Ressources/Ventes.csv", "r", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            print("-" * 20)
            print(f"Date : {ligne["date"]}")
            print(f"Produit : {ligne["produit"]}")
            print(f"Catégorie : {ligne["categorie"]}")
            print(f"Quantité : {int(ligne["quantite"])}")
            print(f"Prix : {float(ligne["prix_unitaire"])}")
    
    print("=" * 20)
    # Ajouter une ligne
    date = input("Date : ")
    produit = input("Produit : ")
    categorie = input("Catégorie : ")
    quantite = input("Quantite : ")
    prix = input("Prix : ")
    print("=" * 20)
    print()
    nouvelleLigne = date+","+produit+","+categorie+","+quantite+","+prix
    
    with open("Ventes.csv", "a", encoding="utf-8") as fichier:
        fichier.write(nouvelleLigne+"\n")
        
    # Afficher toutes les lignes du fichier
    with open("TP1-Ressources/Ventes.csv", "r", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            print(f"Date : {ligne["date"]}")
            print(f"Produit : {ligne["produit"]}")
            print(f"Catégorie : {ligne["categorie"]}")
            print(f"Quantité : {int(ligne["quantite"])}")
            print(f"Prix : {float(ligne["prix_unitaire"])}")
            print("-" * 20)
    

def Projet():
    print("1 - Exercice 1")
    print("2 - Exercice 2")
    print("3 - Exercice 3")
    print("4 - Exercice 4")
    print("0 - Quitter projet")
    choix = int(input("Votre choix : "))
    match choix:
        case 1:
            Exercice1()
            Projet()
        case 2:
            Exercice2()
            Projet()
        case 3:
            Exercice3()
            Projet()
        case 4:
            Exercice4()
            Projet()
        case 0:
            print("Fin du projet")
            main()
        case _:
            Projet()

def Exercice1():
    cours = [150.5, 152.3, 148.7, 151.2, 155.8, 154.3, 157.9, 156.1, 159.4, 162.0]
    
    # 1. Prix moyen
    prixMoyen = sum(cours) / len(cours)
    print(f"Prix moyen : {prixMoyen:.2f}€")

    # 2. Min et Max
    prixMin = min(cours)
    prixMax = max(cours)
    print(f"Prix minimum : {prixMin}€")
    print(f"Prix maximum : {prixMax}€")

    # 3. Variation totale    
    variationTotale = cours[len(cours)-1] - cours[0]
    print(f"Variation totale : {variationTotale:.2f}€")

    # 4. Rendement total
    rendementTotal = (variationTotale / cours[0]) * 100
    print(f"Rendement total : {rendementTotal:.2f}%")

    # 5. Nombre de jours de hausse
    # joursHausse = 0
    # for i in range(1, len(cours)):
    #     if cours[i] > cours[i-1]:
    #         joursHausse += 1
    
    joursHausse = sum(1 for i in range(1, len(cours)) if cours[i] > cours[i - 1])
    print(f"Nombre de jours de hausse : {joursHausse}")
    
def Exercice2():
    categories = ["Loyer", "Alimentation", "Transport", "Loisirs", "Épargne", "Factures"]
    montants = [800, 350, 120, 200, 300, 150]

    # 1. Total des dépenses
    totalDepenses = sum(montants)
    print(f"Total dépenses : {totalDepenses}€")

    # 2. Proportion de chaque catégorie
    print("Proportions :")
    for i in range(len(categories)):
        proportion = (montants[i] / totalDepenses) * 100
        print(f"{categories[i]} : {proportion:.1f}%")

    # 3. Catégorie avec la plus grosse dépense
    maxDepense = max(montants)
    indexMax = montants.index(maxDepense)
    print(f"Plus grosse dépense : {categories[indexMax]} ({maxDepense}€)")

    # 4. Ce qui reste avec un salaire de 2500€
    salaire = 2500
    reste = salaire - totalDepenses
    print(f"Reste après dépenses : {reste}€")

    # 5. Catégories dépassant 10%
    print("Catégories > 10% du budget :")
    for i in range(len(categories)):
        proportion = (montants[i] / totalDepenses) * 100
        if proportion > 10:
            print(f"- {categories[i]} : {proportion:.1f}%")

def Exercice3():
    jeux = ChargerDonnees()  
    while True:
        print("\n" + "=" * 45)
        print("   Gestionnaire de location de jeux vidéo")
        print("=" * 45)
        print("1. Afficher les données")
        print("2. Rechercher un jeu")
        print("3. Emprunter un jeu")
        print("4. Sauvegarder")
        print("0. Quitter projet")
        choix = int(input("Votre choix : "))
        match choix:
            case 1:
                AfficherDonnees(jeux)
            case 2:
                RechercherJeu(jeux)
            case 3:
                EmprunterJeu(jeux)
            case 4:
                Sauvegarder(jeux)
            case 0:
                print("Fin du projet")
                main()
            case _:
                Exercice3()

def ChargerDonnees():
    jeux = []
    with open("Jeux.txt", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                champs = ligne.split("|")
                jeu = {
                    "Titre": champs[0].strip(),
                    "Genre": champs[1].strip(),
                    "Plateforme": champs[2].strip(),
                    "Prix": champs[3].strip(),
                    "Annee": champs[4].strip(),
                    "Emprunteur": champs[5].strip(),
                }
                jeux.append(jeu)
    return jeux

def AfficherDonnees(datas):
    for item in datas:
        print("-" * 20)
        print(f"Titre : {item["Titre"]}")
        print(f"Genre : {item["Genre"]}")
        print(f"Plateforme : {item["Plateforme"]}")
        print(f"Prix : {item["Prix"]}")
        print(f"Annee : {item["Annee"]}")
        print(f"Emprunteur : {item["Emprunteur"]}")

def RechercherJeu(datas):
    genre = input("Quel genre : ").strip().lower()
    resultats = []
    
    for jeu in datas:
        if jeu["Genre"].lower() == genre:
            resultats.append(jeu)
    
    if len(resultats) == 0:
        print("Aucun jeu trouvé")
    else:
        for item in resultats:
            print("-" * 20)
            print(f"Titre : {item["Titre"]}")
            print(f"Genre : {item["Genre"]}")
            print(f"Plateforme : {item["Plateforme"]}")
            print(f"Prix : {item["Prix"]}")
            print(f"Annee : {item["Annee"]}")
            print(f"Emprunteur : {item["Emprunteur"]}")

def EmprunterJeu(datas):
    titre = input("Titre du jeu à emprunter : ").strip().lower()
    # On recherche le jeu par son titre
    trouve = False
    for jeu in datas:
        if jeu["Titre"].lower() == titre:
            trouve = True
            break
    if not trouve:
        print("Aucun jeu ne correspond avec ce titre")
    else:
        if "par" in jeu["Emprunteur"]:
            print("Ce jeu est déjà emprunté")
            return
        else:
            emprunteur = input("Nom de l'emprunteur : ").strip()
            jeu["Emprunteur"] = "Emprunté par "+ emprunteur

def Sauvegarder(datas):
    with open("Jeux.txt", "w", encoding="utf-8") as fichier:
        for jeu in datas:
            ligne = jeu["Titre"] +" | " + jeu["Genre"] +" | " + jeu["Plateforme"] +" | " + jeu["Prix"] +" | " + jeu["Annee"] +" | " + jeu["Emprunteur"]
            fichier.write(ligne+"\n")

def Exercice4():
    nombre_transactions = 0
    quantite_totale = 0
    ca_total = 0

    ca_min = None
    ca_max = 0

    produit_max = ""
    quantite_max = 0

    categories = {}

    with open("TP1-Ressources/Ventes.csv", "r", encoding="utf-8") as fichier:

        lecteur = csv.DictReader(fichier)

        for ligne in lecteur:

            nombre_transactions += 1

            produit = ligne["produit"]
            categorie = ligne["categorie"]

            quantite = int(ligne["quantite"])
            prix = float(ligne["prix_unitaire"])

            ca = quantite * prix

            # Quantité totale
            quantite_totale += quantite

            # Chiffre d'affaires
            ca_total += ca

            # Minimum
            if ca_min is None or ca < ca_min:
                ca_min = ca

            # Maximum
            if ca > ca_max:
                ca_max = ca

            # Produit le plus vendu
            if quantite > quantite_max:
                quantite_max = quantite
                produit_max = produit

            # Catégories
            if categorie not in categories:
                categories[categorie] = 0

            categories[categorie] += ca


    ca_moyen = ca_total / nombre_transactions


    print("=" * 50)
    print("           ANALYSE DES VENTES")
    print("=" * 50)

    print()

    print(f"NOMBRE DE TRANSACTIONS : {nombre_transactions}")
    print(f"QUANTITE TOTALE : {quantite_totale}")

    print()

    print("CHIFFRE D'AFFAIRES")
    print("-" * 34)
    print(f"Total       : {round(ca_total, 2)} €")
    print(f"Moyenne     : {round(ca_moyen, 2)} €")
    print(f"Minimum     : {round(ca_min, 2)} €")
    print(f"Maximum     : {round(ca_max, 2)} €")

    print()

    print("PRODUIT LE PLUS VENDU")
    print("-" * 34)
    print(f"Produit     : {produit_max}")
    print(f"Quantité    : {quantite_max}")

    print()

    print("CATEGORIES")
    print("-" * 34)

    for categorie, ca in categories.items():
        print(f"{categorie} : {round(ca, 2)} €")

    print()
    print("=" * 50)

if __name__ == "__main__":
    main()
import numpy

def main():
    print("1 - Tableaux")
    print("2 - Matrices")
    print("3 - Projet")
    print("0 - Quitter")
    choix = int(input("Votre choix : "))
    match choix:
        case 1:
            Tableaux()
            main()
        case 2:
            Matrices()
            main()
        case 3:
            Projet()
            main()
        case 0:
            print("Fin du programme")
            exit()
        case _:
            main()

def Tableaux():
    # Création d'un tableau
    notes = numpy.array([12, 15, 8, 17, 10])
    print(notes)
    print(f"Notes + 1 : {notes + 1}")
    print(f"Notes - 2 : {notes - 2}")
    print(f"Notes * 2 : {notes * 2}")
    print(f"Notes / 2 : {notes / 2}")
    
    # Stats diverses
    print(f"Moyenne : {numpy.mean(notes)}")
    print(notes.mean())
    print(f"Médiane : {numpy.median(notes)}")
    
    print(f"Minimum : {numpy.min(notes)}")
    print(notes.min())
    print(f"Maximum : {numpy.max(notes)}")
    print(notes.max())
    print(f"Somme : {numpy.sum(notes)}")
    print(notes.sum())
    print(f"Écart-type : {numpy.std(notes)}")
    print(notes.std())
    print(f"Variance : {numpy.var(notes)}")
    print(notes.var())
    
    # Filtrer
    print("Filtrer sur une condition")
    selection = notes >= 10
    print(selection)
    print(notes[selection])
    
    # Ou directement
    print(notes[notes >= 10])
    
    # Plusieurs conditions
    print("Filtrer sur plusieurs conditions")
    selection = notes[(notes >= 10) & (notes <= 15)]
    print(selection)
    
    # Compter
    print("Compter")
    print(f"Nombre d'admis :  {numpy.sum(notes >= 10)}")
    print(f"Notes >= 15 : {numpy.sum(notes >= 15)}")
    print(f"Notes < 10 : {numpy.sum(notes < 10)}")
    
    # Générer des valeurs
    print("Générer des valeurs")
    print(numpy.arange(1,11))
    print(numpy.arange(0,21,2))
    print(numpy.linspace(0,100,10))
    
    # Parcourir
    for i,note in enumerate(notes):
        print(f"Note n° {i+1} : {note}")
        
    print("-" * 20)
    
    for i in range(len(notes)):
        print(f"Note n° {i+1} : {notes[i]}")
    
    print("-" * 20)
    
    for note in notes:
        print(note)

def Matrices():
    # Tableaux de notes pour 5 étudiants avec les matières Python, SQL et réseau
    notes = numpy.array([
        [15, 12, 14],
        [9, 14, 11],
        [17, 16, 15],
        [12, 10, 13],
        [18, 15, 17]
    ])
    print(notes)
    # Afficher la note de l'étudiant 3 en SQL
    print("Note de l'étudiant 3 en SQL")
    print(notes[2][1])
    # Ou
    print(notes[2,1])
    
    # Moyenne par matière
    moyennes = numpy.mean(notes, axis=0)
    print("Moyenne Python :", moyennes[0])
    print("Moyenne SQL :", moyennes[1])
    print("Moyenne Réseau :", moyennes[2])
    
    # Moyenne par étudiant
    moyennes = numpy.mean(notes, axis=1)
    for i, moyenne in enumerate(moyennes):
        print(f"Etudiant n°{i + 1} : {round(moyenne,2)}")
    
    # Numéros des étudiants ayant eu la moyenne en python
    indicesEtudiants = numpy.where(notes[:,0] >=10)[0]
    print(indicesEtudiants + 1)

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
    # Création d'un tableau de 10 valeurs allant de 0 à 9
    tab = numpy.arange(10)
    print(tab)
    # Afficher que les valeurs impaires
    print(tab[tab % 2 == 1])
    # Remplacer les valeurs impaires par des -1
    #out = numpy.where(tab % 2 == 1,-1,tab)
    print(numpy.where(tab % 2 == 1,-1,tab))
    # Autre solution mais ça modifie le tableau initial
    # tab[tab % 2 == 1] = -1
    # print(tab)

def Exercice2():
    tab = numpy.random.randint(0, 2, 10)
    print(f"Tableau initial : {tab}")

    compresse = []
    compteur = 1

    for i in range(1, len(tab)):
        if tab[i] == tab[i - 1]:
            compteur += 1
        else:
            compresse.append(compteur)
            compteur = 1

    compresse.append(compteur)
    print(f"Tableau compressé : {compresse}")

def Exercice3():
    jours = numpy.array(["Lundi", "Mardi", "Mercredi","Jeudi", "Vendredi", "Samedi", "Dimanche"])
    ventes = numpy.array([120, 85, 150, 95, 180, 220, 140])
    # Afficher les ventes du vendredi.
    print("1. Ventes du vendredi :")
    indice_vendredi = numpy.where(jours == "Vendredi")[0][0]
    
    print(ventes[indice_vendredi])
    
    # Afficher les jours où les ventes dépassent 150 livres.
    print("2. Jours avec plus de 150 ventes :")
    print(jours[ventes > 150])
    
    # Statistiques
    # Calculer le nombre total de ventes.
    print(f"3. Total des ventes : {numpy.sum(ventes)}")
    #Calculer la moyenne des ventes.
    print(f"4. Moyenne : {numpy.mean(ventes)}")
    # Déterminer la vente minimale et maximale.
    print(f"5. Minimum : {numpy.min(ventes)}")
    print(f"5. Maximum : {numpy.max(ventes)}")

    # Trier les ventes par ordre croissant.
    indices = numpy.argsort(ventes)
    print("6. Ventes triées :")
    print(ventes[indices])

    # Afficher le classement des jours du plus vendeur au moins vendeur.
    print("7. Classement du meilleur au moins bon :")
    indices_desc = numpy.argsort(ventes)[::-1]
    print(jours[indices_desc])
    
    # Afficher les trois meilleures journées.
    print("8. Top 3 des journées :")
    print(jours[indices_desc[:3]])
    
    # Combien de jours ont dépassé la moyenne ?
    moyenne = numpy.mean(ventes)
    print("9. Nombre de jours au-dessus de la moyenne :")
    print(numpy.sum(ventes > moyenne))
    
    # Quel est l'écart entre la meilleure et la moins bonne journée ?
    print("10. Ecart entre le maximum et le minimum :")
    print(numpy.max(ventes) - numpy.min(ventes))
    
    # Quel pourcentage des jours ont dépassé 100 ventes ?
    pourcentage = numpy.sum(ventes > 100) / len(ventes) * 100
    print("11. Pourcentage de jours avec plus de 100 ventes :")
    print(f"Pourcentage : {pourcentage:.2f}%")
    print(f"Pourcentage : {round(pourcentage,2)}%")
    
def Exercice4():
    # Matrice des ventes
    ventes = numpy.array([
        [45, 30, 80],   # Paris
        [35, 25, 70],   # Lyon
        [50, 40, 90]    # Marseille
    ])

    # Matrice des prix
    prix = numpy.array([
        [800, 300, 500],
        [800, 300, 500],
        [800, 300, 500]
    ])
    # Noms des magasins
    magasins = numpy.array(["Paris", "Lyon", "Marseille"])
    # Noms des produits
    produits = numpy.array(["Ordinateurs", "Tablettes", "Smartphones"])

    print("1. Smartphones vendus à Lyon :")
    print(ventes[1, 2])

    print("2. Magasin ayant vendu le plus d'ordinateurs :")
    indice = numpy.argmax(ventes[:, 0])
    print(magasins[indice])

    print("3. Nombre total de tablettes vendues :")
    print(numpy.sum(ventes[:, 1]))

    print("4. Produit le plus vendu à Marseille :")
    indice = numpy.argmax(ventes[2])
    print(produits[indice])

    print("5. Total des articles vendus :")
    print(numpy.sum(ventes))

    print("6. Moyenne des ventes par magasin :")
    print(numpy.mean(ventes, axis=1))

    print("7. Moyenne des ventes par produit :")
    print(numpy.mean(ventes, axis=0))

    ca = ventes * prix

    print("8. Matrice du chiffre d'affaires :")
    print(ca)

    print("9. Chiffre d'affaires total :")
    print(numpy.sum(ca), "€")

    print("10. Magasin générant le plus de CA :")
    ca_magasin = numpy.sum(ca, axis=1)
    indice = numpy.argmax(ca_magasin)
    print(magasins[indice])

    print("11. Produit générant le plus de CA :")
    ca_produit = numpy.sum(ca, axis=0)
    indice = numpy.argmax(ca_produit)
    print(produits[indice])

    print("12. Produit représentant la plus grande part du CA :")
    indice = numpy.argmax(ca_produit)
    part = ca_produit[indice] / numpy.sum(ca) * 100
    print(f"{produits[indice]} représentant {round(part,2)} % du CA total")

if __name__ == "__main__":
    main()
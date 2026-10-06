# TP2.py

#J'importe numpy
import numpy

#Je fais un menu pour choisir entre plusieurs options, tableaux, matrices et projet
def main():
    print("1. Tableaux")
    print("2. Matrices")
    print("3. Projet")
    print("0. Quitter")
    choix = int(input("Entrez votre choix : ")) #Attend l'entree de l'utilisateur
    match choix: #Utilisation de match case pour choisir l'option
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
            print("Quitter le programme")
            exit()
        case _:
            main()

#Je crée une fonction pour afficher un tableau numpy avec des valeurs prédéfinies
def Tableaux():
    tab = numpy.array([12,15,8,17,10,])
    print(tab)
    print(tab + 1)
    print(tab - 2)
    print(tab * 2)
    print(tab / 2)
    print(f"La moyenne des éléments du tableau est : {numpy.mean(tab)}")
    print(f"La médiane des éléments du tableau est : {numpy.median(tab)}")
    print(f"La valeur maximale du tableau est : {numpy.max(tab)} et la valeur minimale est : {numpy.min(tab)}")
    print(f"La somme des éléments du tableau est : {numpy.sum(tab)}")
    print(f"L'écart type des éléments du tableau est : {numpy.std(tab)}")
    print(f"La variance des éléments du tableau est : {numpy.var(tab)}")
    print(f"Les éléments du tableau supérieurs à 10 sont : {tab[tab >= 10]}")
    print(f"Les éléments du tableau supérieurs à 10 et inférieurs à 15 sont : {tab[(tab >= 10) & (tab <= 15)]}")
    print(f"Nombre d'admis : {numpy.sum(tab >= 10)}")
    print(f"Nombre : {numpy.sum(tab >= 15)}")
    print(f"Nombre : {numpy.sum(tab < 10)}")

    #numpy.

def Matrices():
    mat = numpy.matrix([[1,15,12,14],[2,9,14,11],[3,17,16,15],[4,12,10,13],[5,18,15,17]])
    print(mat)

def Projet():
    pass

if __name__ == "__main__":
    main()
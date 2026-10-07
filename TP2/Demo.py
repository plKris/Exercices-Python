import numpy
def main():
    # tab = numpy.arange(10)
    # print(tab)
    
    # print(tab[tab % 2 == 1])
    # print(numpy.where(tab % 2 == 1,-1,tab))
    
    # tab = numpy.random.randint(0,2,10)
    # print(tab)
    
    # compteur = 1
    # tabCompresse = []
    # for i in range(len(tab)-1):
    #     if tab[i] == tab[i+1]:
    #         compteur+=1
    #     else:
    #         tabCompresse.append(compteur)
    #         compteur = 1
    # tabCompresse.append(compteur)
    # print(tabCompresse)

    jours = numpy.array(["Lundi", "Mardi", "Mercredi","Jeudi", "Vendredi", "Samedi", "Dimanche"])
    ventes = numpy.array([120, 85, 150, 95, 180, 220, 140])
    # print(numpy.where(jours == "Vendredi"))
    # print(ventes[numpy.where(jours == "Vendredi")[0][0]])
    indice = numpy.where(jours == "Vendredi")
    print(f"Indice : {indice}")
    print(ventes[indice][0])
    
    print(jours[numpy.where(ventes > 150)])
    
    print(sum(ventes))
    print(numpy.mean(ventes))
    print(numpy.min(ventes))
    print(numpy.max(ventes))
    
    indices = numpy.argsort(ventes)
    print (ventes[indices])
    print(numpy.sort(ventes))
    print(numpy.sort(ventes)[::-1])
    print(jours[numpy.argsort(ventes)[::-1]][:3])
    

if __name__ == "__main__":
    main()
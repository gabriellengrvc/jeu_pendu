from random import randrange

def mot_hasard():
    """Pioche au hasard un mot dans un des fichiers de n lettres et retourne ce mot"""
    # Choisir au hasard un fichier de lettres dont le nom
    # est sous la forme "mots_de_n_lettres.txt" avec n entre 1 et 25.

    n = randrange(5,7)
    adresse_relative = "pendu/base_de_mots/"
    fichier = adresse_relative+"mots_de_"+str(n)+"_lettres.txt"

    with open(fichier,"r") as mon_fichier:
        ma_liste = mon_fichier.readlines() # Créer une liste de tous les mots du fichier
    #print(ma_liste,len(ma_liste),len(ma_liste[0]))

    mot =  ma_liste[randrange(len(ma_liste))] # En choisir un au hasard
    return mot.rstrip() # Enlever le retour à la ligne enlever lespace a la fin de la ligne

solution = mot_hasard()
"""print(solution)"""
tentatives = 7
lettres_trouvees = ""
lettres_valides = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
blanks = '_' * len(solution)
print(blanks, "\n")

while tentatives > 0:
    reponse = input("Deviner une lettre:")[0:1].lower()

    blanks = '_' * len(solution)

    if reponse not in lettres_valides:
        reponse = input("Ce symbole ou ce mot n'est pas acceptable, faites un autre choix : ").lower() 
        
    if reponse in solution:
        lettres_trouvees += reponse
        print("Oui!")
        for i in range(len(solution)):
            if solution[i] in lettres_trouvees:
                blanks = blanks[:i] + solution[i] + blanks[i+1:]
        print(blanks, "\n")
    
    else:
        tentatives -= 1
        print("Try again")
        if tentatives==0:
            print(" ==========Y= ")
        if tentatives<=1:
            print(" ||/       |  ")
        if tentatives<=2:
            print(" ||        0  ")
        if tentatives<=3:
            print(" ||       /|\ ")
        if tentatives<=4:
            print(" ||       / \ ")
        if tentatives<=5:                    
            print("/||           ")
        if tentatives<=6:
            print("==============\n")

    affichage = ""
    for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

    if "_" not in affichage:
      print(">>> Gagné! <<<")
      break

print("\n    * Fin de la partie *    ")









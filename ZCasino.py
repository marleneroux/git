#!/usr/local/bin/python3.9

#Casino
#jeu de roulette simplifié, on peut miser une somme et gagner ou perdre
#de l'argent. quand on n'a plus d'argent on a perdu

#importation de la fonction randrange
#math.ceil(x) : retourne l'entier supérieur à x

from random import randrange
import math

#code principal
#variable mise0 = mise de départ
mise0 = int(input("vous vous installez à la table de casino avec ? : "))

#tant que la mise est supérieure à 0 on fait une boucle
while (mise0 != 0):
    if (mise0 <= 0):
        print("Vous avez tout perdu!")
        break

#définition des variables 1-nombre choisi par le joueur, 2-sa mise et 3-le résultat de la roulette       
    nombre = int(input("choisir un numéro entre 0 et 49 :"))
    while nombre < 0 or nombre > 49:
        nombre = int(input("choisir un numéro entre 0 et 49 :"))
               
    mise = int(input("choisir votre mise : "))
    aleatoire = int(randrange(50))
    print("la roulette s'arrête sur : ", aleatoire)

# comparaison du résultat de la roulette avec le nombre choisi par le joueur
    if (aleatoire % 2 == 0 and nombre % 2 == 0) or (aleatoire % 2 != 0 and nombre % 2 != 0):
        mise0= mise0 + math.ceil(50/100 * mise)
        print("vous avez misé sur la bonne couleur. Vous gagnez", mise*50/100)
        print("vous avez à présent", mise0)
    elif aleatoire == nombre:
        mise0= mise0 + 3*mise
        print("vous avez misé sur le bon numéro. Vous gagnez", mise*3)
        print("vous avez à présent", mise0)
    else:
        mise0 = mise0 - mise
        print("vous avez perdu la somme misée")
        print("vous avez à présent", mise0)

# question pour continuer ou arrêter le jeu
    choix = input("Voulez-vous continuer ? (o/n)")
    if choix == "o":
        continue
    if choix == "n":
        print("vous repartez avec", mise0)
        break
        

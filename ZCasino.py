#! /usr/local/bin/python3.9

#importation de la fonction randrange

from random import randrange
import math

#code principal

mise0 = int(input("vous vous installez à la table de casino avec ? : "))
nombre = int(input("choisir un numéro entre 0 et 49 :"))     
mise = int(input("choisir votre mise : "))
aleatoire = int(randrange(50))
print("la roulette s'arrête sur : ", aleatoire)

if (aleatoire % 2 == 0 and nombre % 2 == 0) or (aleatoire % 2 != 0 and nombre % 2 != 0):
    mise0= mise0 + 50/100 * mise
    print("vous avez misé sur la bonne couleur. Vous gagnez", mise*50/100)
    print("vous avez à présent", mise0)
elif aleatoire == nombre:
    mise0= mise0 + 3*mise
    print("vous avez misé sur le bon numéro. Vous gagnez", mise*3)
    print("vous avez à présent", mise0)
else:
    print("vous avez perdu la somme misée")
    print("vous avez à présent", mise0 - mise)















#!/usr/local/bin/python3.9
# -*- coding: utf-8 -*-

#exercices sur les chaines
# fonction avec parametres un mot et une chaine de caractère
#renvoie false si élt pas dans la chaine, sinon sa position
def searchC(mot, chaine):
    chaine = chaine.find(mot)
    if chaine != -1:
        return chaine
    else:
        return False
                
#test de la fonction searchC
searchC("test", "je test le code")
searchC("mot", "je test le code")



#méthode replace("caractère à remplacer", "caractere de remplacement")

chaine = "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 a r3soudr3.Gandh1"
chaine = chaine.replace("1", "i")
chaine = chaine.replace("3", "e")
print(chaine)


#fonction paramètres lettre et chain qui renvoie le nombre d'apparition de la
#lettre dans la chaine
def compteur(lettre, chaine):
    j = 0   
    for i in chaine:
        if i == lettre:
            j = j + 1 
    return(j)

#test de la fonction compteur
compteur("l", "lettre")
compteur("a", "aleatoire")


#fonction qui prend une chaine de caractere et renvoie son inverse
def inverse(chaine):
    chaine = "".join(reversed(chaine))
    return (chaine)


#pour tester
inverse("mot")
inverse("liste")


#exercices sur les fichiers

#fonction nbre ligne

def Nbrligne(fichier):
    f = open(fichier,"r") # on ouvre le fichier en mode lecture
    text = f.readlines() #renvoie une liste contenant toutes les lignes du fichier
    nbre_ligne = len (text) #longueur de la liste text
    return (nbre_ligne)
    fichier.close()
    

#test de la fonction nbre ligne
Nbrligne("Demi.txt")


#ecrivez le contenu d'un fichier à la suite d'un autre
fichier_ajout = open("La_mesure_de_lhomme.txt", "a")# on ouvre le fichier en mode ajout
fichier_aajouter = open ("Demi.txt", "r")
t = fichier_aajouter.read()
fichier_ajout.write(t)

fichier_ajout.close()
fichier_aajouter.close()



#afficher le contenu du fichier
fichier_ajout = open("La_mesure_de_lhomme.txt", "r")
t = fichier_ajout.read()
print (t)
fichier_ajout.close()







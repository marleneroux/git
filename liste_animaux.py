#!/usr/local/bin/python3.9
# -*- coding: utf-8 -*-

#initialisation de la liste
liste_animaux = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
for animal in liste_animaux:
        print(animal)
        
#liste de manière inversée
liste_animaux.reverse()
print (liste_animaux)
        
#liste de manière triée
liste_animaux.sort()
print (liste_animaux)
        
#ajouter troll dans la liste
liste_animaux.append("troll")
print(liste_animaux)
        
#supprimer l'ensemble des animaux domestiques
domestiques = ["lapin","chat","chien","chiot"]
for anim in domestiques:
        liste_animaux.remove(anim)
print(liste_animaux)

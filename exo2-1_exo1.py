#!/usr/local/bin/python3.9
# -*- coding: utf-8 -*-

# write program to convert temperatures to and from celsius,fahrenheit

#temperature = int(input("saisir une temperature :")
#degre = str(input("indiquer si la temperature rentrée est en C (celsius) ou F (fahrenheit)"))


#définition des fonctions de conversion

def cel_far():
    temperatureC = int(input("saisir une temperature :"))
    conversionF = int(9 * temperatureC / 5 + 32)
    print(temperatureC,"°C is", conversionF, "in Fahrenheit")

#test
#cel_far(60)


def far_cel():
    temperatureF = int(input("saisir une temperature :"))
    conversionC = int((temperatureF - 32) / 9 *5)
    print(temperatureF,"°F is", conversionC, "in Celsius")

#test
#far_cel(45)


#main program
while True:
    choix = input("\n1: °C to °F\n2: °F to °C\nq : quit\n> ")
    if choix == "q":
        quit()
    elif choix == "1":
        cel_far()
    elif choix == "2":
        far_cel()
    else:
        print("Input error")
            
    

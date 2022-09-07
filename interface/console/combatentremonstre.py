#! /usr/bin/env python3
# coding: utf-8

#------------------
#simulateur de combat autour du JdR l'oeil noir
#auteur : silanoc
#début sur téléphone portable : juillet 2019
#amélioration : avril 2021
#version 1
#--------------------

from random import *
import json
	
from domaine.lanceur_de import d6, d20 
from domaine.entite import Entite as Entite
from domaine.combat import Combat as Combat


#------
# fonctions pour le programme
#------

def bannieredebutprogramme() -> None:
    """Simple message à afficher au lancement du programme.
    Print dans la console
    """
    
    print("""__________________________________________________________________
Bienvenue dans mon programme de simulation de combat de l'oeil noir
par Silanoc, avril 2021, version 1
""")

    print("""
@@@###### =  =  =  =  =  = *******+++++++::::::::::::::::::::::+++++++******* =  =  =  =  =  = ######@@
@@@@###### =  =  =  =  =  = *******+++++++::::::::::::::::::::+++++++******* =  =  =  =  =  = ######@@@
@@@@@###### =  =  =  =  =  = *******+++++* = @WWWWWWWWWWWWWW@#*+++++++******* =  =  =  =  =  = ######@@@@
@@@@@####### =  =  =  =  =  = *******#WWWWWWWWWWWWWWWWWWWWWWWWWW@ = ******** =  =  =  =  =  = #######@@@@
@@@@@@####### =  =  =  =  =  =  = * = @WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#*** =  =  =  =  =  =  = #######@@@@@
W@@@@@@####### =  =  =  =  = @WWWWWWWWWWW# = +:---------:*#WWWWWWWWWWWW# =  =  =  =  =  = #######@@@@@@
WW@@@@@@######## = @WWWWWWWWW = +++::::----...----:::+*#WWWWWWWWW@ =  = ########@@@@@@W
WWW@@@@@@@#####@WWWWWWWW#***++++::::---------::::++++*#WWWWWWWW@######@@@@@@@WW
WWWW@@@@@@@###WWWWWWWW =  =  = ****++++:::::----::::::++++**** = @WWWWWWW###@@@@@@@@WWW
WWWWW@@@@@@@@WWWWWWW## =  =  =  = ****+++++::::::::::++++++**** =  =  =  = @WWWWWW@@@@@@@@@WWWW
WWWWWWW@@@@@WWWWWW@#### =  =  =  = *****++++++++++++++++***** =  =  =  =  = ###@WWWWW@@@@@@WWWWWW
WWWWWWWWW@@WWWWWW@@@#### =  =  =  =  = *******++++++++******* =  =  =  =  = ####@@@WWWWWWW@WWWWWWWW
WWWWWWWWWWWWWWWWWW@@@@#### =  =  =  =  =  =  = *************** =  =  =  =  =  = #####@@@WWWWWWWWWWWWWWWWW
WWWWWWWWWWWWW@WWWWWW@@@@##### =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  =  = ######@@@WWWWWWWWWWW@@WWWWWW
WWWWWWWWWWW#---:+@WWWW@@@@######### =  =  =  =  =  =  =  =  =  =  = ########@@@WWW@+::::::::+@WWWWWWW
WWWWWWWWWWWW@:-----*W@WWW@@@@@####################@@@@@W#@*-----: = #WWWWWWWWWWWW
WWWWWWWWWWWWWW#------:#@#@WW@@@@@@@@@@@@@@@@@@@@@@@@W# = @:----:@WWWWWWWWWWWWWWW
nWWWWWWWWWWWWWWWW = -------+@W@@WWWW@@@@@@@@@@@@@@@WW@ = # = -----+@WWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWW@:-------:#WWWWWWWWWWWWWWWWWWW@@*------*WWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWW = ---------: = @WWWWWWWWWWW#+-------:#WWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWW@+-.........------.........:#WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWW@ = :...............-+#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@@@@@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
(c) 2021 topster.de############################################################""")


def genererlesmonstres() -> None:
    global monstre
    monstre = []
    for tous_les_monstres in json.load(open("interface/json/data_monstre.json")):
        monstre.append(Entite(**tous_les_monstres))
    print(monstre)
    for i in range(len(monstre)):
        print(monstre[i].classe)
        print(monstre[i].pvmax)


def combatsimple():
    #choisir les deux participants
    dicomonstre: dict = {}
    dicomonstrelisible: dict = {}
    for i in range(len(monstre)):
        dicomonstre[i]  =  monstre[i]
        dicomonstrelisible[i]  =  monstre[i].classe
    choix1 = "a" 
    choix2 = "a"
    listint = range(len(monstre))
    while choix1 not in listint or choix2 not in listint: 
        print("Entrez le chiffre correspondant au 1er monstre")
        choix1 = input(dicomonstrelisible)
        choix1 = int(choix1)
        print("Entrez le chiffre correspondant au 2ème monstre")
        choix2 = input(dicomonstrelisible)
        choix2 = int(choix2)
    participant1 = dicomonstre[int(choix1)]
    participant2 = dicomonstre[int(choix2)]
    #combat en lui même
    combatencours = Combat(participant1,participant2)
    quiestvainqueur = combatencours.effectue_combat()
    #affiche le résultat
    print("le vainqueur est : " + quiestvainqueur.classe + "\n")


def menu_principal():
    user_answer: int = "a"
    user_answer = input("""Que voulez vous faire :
                        un combat entre 2 monstre à choisir (tapez 1)
                        un tournois (tapez 2)
                        ou quitter (tapez Q ou q)""")
    while user_answer !=  "Q":
        menu = {"1":combatsimple,"2":tournoisentremonstre, "q":fin, "Q":fin}
        menu.get(user_answer,passer)()
        user_answer = input("""Que voulez vous faire :
                            un combat entre 2 monstre à choisir (tapez 1)
                            un tournois (tapez 2)
                            ou quitter (taper Q ou q) \n""")


def tournoisentremonstre():
    #initialisation des participants et des scores
        participants = monstre
        resultats  =  [[0] * (len(participants)) for _ in range(len(participants))]
        nbround = int(input("Combien de combats souhaitez-vous ?"))
        #combat
        for nmbredecombat in range(nbround):
            for i in range(0, len(participants)):
                for j in range (i+1,len(participants)):
                    #print (participants[i],participants[j])
                    combatencours = Combat(participants[i],participants[j])
                    quiestvainqueur = combatencours.effectue_combat()
                    if quiestvainqueur == participants[i]:
                        resultats[i][j]+= 1
                    else:
                        resultats[j][i]+= 1
        #affiche les resultats
        for k in range (len(participants)):
            print(str(participants[k].classe) +"\t"+ str(resultats[k]))


def passer() -> None:
    pass


def fin() -> None:
    print("Merci d'avoir utilisé mon programme. A une prochaine fois.")
    exit()


def main() -> None:
    genererlesmonstres()
    bannieredebutprogramme()
    menu_principal()
    
    
    
#-----------
# déroulement du programme
#--------     

if __name__ == "__main__":
    main()
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
#import json
	
#from domaine.lanceur_de import d6, d20 
#from domaine.entite import Entite as Entite
from domaine.combat import Combat as Combat

from domaine.port_console import recupere_la_liste_des_monstre

#------
# fonctions pour le programme
#------

def bannieredebutprogramme() -> None:
    """Simple .
    Print dans la console :
    * message à afficher au lancement du programme
    * le logo en pixel art, stocké dans un fichier externe
    """
    
    print("""__________________________________________________________________
Bienvenue dans mon programme de simulation de combat de l'oeil noir
par Silanoc, avril 2021, version 1
""")

    logo = open("images/pixel_art_logo_oeil_noir.txt", 'r')
    tout_le_logo = logo.readlines()
    for i in tout_le_logo:
        print(i, end = "" )
    
    print("\n")


def genererlesmonstres() -> None:
    """Via port_console, récupére dans une lsite toutes les instances de monstres possible à avoir"""
    global monstre
    monstre = recupere_la_liste_des_monstre()


def afficher_les_monstres_disponibles() -> None:
    """Simple affichage dans la console"""
    for i in range(len(monstre)):
        print(f" - {monstre[i].classe} avec {monstre[i].pvmax} points d'énergie vitale.")


def menu_principal() -> None:
    """Menu principal du propgramme, demande à l'utilisateur de faire un choix 
    et de le rentrer en écrivant dans la console
    """
    text_choix_possibles: int = """Que voulez vous faire :
                        afficher les montres disponibles (tapez 0)
                        un combat entre 2 monstre à choisir (tapez 1)
                        un tournois (tapez 2)
                        ou quitter (tapez Q ou q)"""
    user_answer = input(text_choix_possibles)
    while user_answer !=  "Q":
        menu = {"0": afficher_les_monstres_disponibles,
                "1" : combatsimple,
                "2" : tournoisentremonstre, 
                "q":fin, "Q":fin}
        menu.get(user_answer,passer)()
        user_answer = input(text_choix_possibles)


def choisir_deux_combattants() -> tuple():
    """Affiche la liste des monstres disponible, avec un numéro de lié.
    Demande à l'utilisateur de rentrer un nombre pour chacun des monstres devant combattre
    """
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
    participants: tuple = (dicomonstre[int(choix1)], dicomonstre[int(choix2)])
    return participants
    
    
def combatsimple():
    # défini les combattants
    qui_combat = choisir_deux_combattants()
    #combat en lui même
    combatencours = Combat(qui_combat[0],qui_combat[1])
    quiestvainqueur = combatencours.effectue_combat()
    #affiche le résultat
    print("le vainqueur est : " + quiestvainqueur.classe + "\n")


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
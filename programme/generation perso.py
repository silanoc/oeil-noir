#! /usr/bin/env python3
# coding: utf-8

from random import *
from lanceur_de import d6, d20

#def d6():
#    a  = randint(1, 6)
 #   return a

class heros:
    def __init__(self):
        self.courage = 0
        self.intelligence = 0
        self.charisme = 0
        self.adresse = 0
        self.force = 0

    def valeur_aleatoire_comp(self):
        self.courage = d6() + 7
        self.intelligence = d6() + 7
        self.charisme = d6() + 7
        self.adresse = d6() + 7
        self.force = d6() + 7

    def chercher_les_choix_possibles(self):
        self.liste_choix = ["aventurier"]
        if self.courage >= 12 and self.force >=  12:
            self.liste_choix.append("guerrier")
        if self.force >= 12 and self.adresse >=  12:
            self.liste_choix.append("nain")
        if self.intelligence >= 12 and self.adresse >=  12:
            self.liste_choix.append("elfe")
        if self.intelligence >= 12 and self.charisme >=  12:
            self.liste_choix.append("magicien")


for i in range(10):
    print("Co, Int, Cha, adre, Fo")
    perso1 = heros()
    #print(perso1.courage, perso1.intelligence, perso1.charisme, perso1.adresse, perso1.force)
    perso1.valeur_aleatoire_comp()
    print(perso1.courage, perso1.intelligence, perso1.charisme, perso1.adresse, perso1.force)
    perso1.chercher_les_choix_possibles()
    print(perso1.liste_choix)
    

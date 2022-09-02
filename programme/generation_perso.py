#! /usr/bin/env python3
# coding: utf-8

from random import *
from programme.lanceur_de import d6

class Heros:
    def __init__(self) -> None:
        """initialise les valeurs d'un hèros"""
        self.courage: int = 0
        self.intelligence: int = 0
        self.charisme: int = 0
        self.adresse: int = 0
        self.force: int = 0

    def valeur_aleatoire_comp(self) -> None:
        """Selon les régles du jeu, chaque caractèritique vaut 1d6+7 """
        self.courage = d6() + 7
        self.intelligence = d6() + 7
        self.charisme = d6() + 7
        self.adresse = d6() + 7
        self.force = d6() + 7

    def chercher_les_choix_possibles(self) -> list[str]:
        """Le choix de la classe d'aventurier, se fait en fonction de valeurs minimal.
        Mettre tous les possible dans une liste."""
        liste_choix: list[str] = ["aventurier"]
        if self.courage >= 12 and self.force >=  12:
            liste_choix.append("guerrier")
        if self.force >= 12 and self.adresse >=  12:
            liste_choix.append("nain")
        if self.intelligence >= 12 and self.adresse >=  12:
            liste_choix.append("elfe")
        if self.intelligence >= 12 and self.charisme >=  12:
            liste_choix.append("magicien")
        return liste_choix


def generer_10_perso():
    for i in range(10):
        print("Co, Int, Cha, adre, Fo")
        perso1: Heros = Heros()
        perso1.valeur_aleatoire_comp()
        print(perso1.courage, perso1.intelligence, perso1.charisme, perso1.adresse, perso1.force)
        classes_possible = perso1.chercher_les_choix_possibles()
        print(f"C'est donc un {classes_possible}")
        
if __name__ == "__main__":
    generer_10_perso()
    

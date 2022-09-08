#! /usr/bin/env python3
# coding: utf-8

"""Création des héros"""

from random import *
from domaine.lanceur_de import d6


class Heros:
    """initialise les valeurs d'un héros"""

    def __init__(self) -> None:
        self.courage: int = 0
        self.intelligence: int = 0
        self.charisme: int = 0
        self.adresse: int = 0
        self.force: int = 0

    def valeur_aleatoire_comp(self) -> None:
        """Selon les régles du jeu, chaque caractéristique vaut 1d6+7 """
        self.courage = d6() + 7
        self.intelligence = d6() + 7
        self.charisme = d6() + 7
        self.adresse = d6() + 7
        self.force = d6() + 7

    def chercher_les_choix_possibles(self) -> list[str]:
        """Le choix de la classe d'aventurier, se fait en fonction de valeurs minimal.
        Mettre tous les possible dans une liste."""
        liste_choix: list[str] = ["aventurier"]
        if self.courage >= 12 and self.force >= 12:
            liste_choix.append("guerrier")
        if self.force >= 12 and self.adresse >= 12:
            liste_choix.append("nain")
        if self.intelligence >= 12 and self.adresse >= 12:
            liste_choix.append("elfe")
        if self.intelligence >= 12 and self.charisme >= 12:
            liste_choix.append("magicien")
        return liste_choix

    def defini_au_hasard_la_classe(self, liste) -> None:
        """choisi au hasard dans la liste des metiers possible celui retenu.
        L'écrit dans self.classe_metier 

        :param list[str] liste : liste de métier possible"""
        self.classe_metier = liste[randint(0, len(liste) - 1)]


def generer_10_perso() -> None:
    for i in range(10):
        print("Co, Int, Cha, adre, Fo")
        perso1: Heros = Heros()
        perso1.valeur_aleatoire_comp()
        print(perso1.courage, perso1.intelligence,
              perso1.charisme, perso1.adresse, perso1.force)
        classes_possible = perso1.chercher_les_choix_possibles()
        print(f"C'est potentiellement un {classes_possible}")
        perso1.defini_au_hasard_la_classe(classes_possible)
        print(f"C'est plus précisement un {perso1.classe_metier}")


if __name__ == "__main__":
    generer_10_perso()

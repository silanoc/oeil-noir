#! /usr/bin/env python3
# coding: utf-8

import domaine.generation_perso as generation_perso

"""Test la génération de perso"""


class Test_generateur_perso():

    def test_constructeur(self):
        """simple vérification que le constructeur existe"""
        perso = generation_perso.Heros()
        assert perso.force == 0

    def test_valeur_aleatoire_comp(self):
        """ vérifier que les caractèristiques sont entre 8 et 13, soit 1d6+7"""
        perso = generation_perso.Heros()
        perso.valeur_aleatoire_comp()
        lst_poss: list[int] = [8, 9, 10, 11, 12, 13]
        assert (perso.force in lst_poss and perso.adresse in lst_poss and
                perso.charisme in lst_poss and perso.courage in lst_poss and
                perso.intelligence in lst_poss)

    def test_chercher_les_choix_possibles(self):
        """Test les 2 cas limite, aventurier ou toutes les classes"""
        perso1 = generation_perso.Heros()
        perso1.adresse = perso1.charisme = perso1.courage = perso1.force = perso1.intelligence = 8
        possible = perso1.chercher_les_choix_possibles()
        assert possible == ["aventurier"]

        perso2 = generation_perso.Heros()
        perso2.adresse = perso2.charisme = perso2.courage = perso2.force = perso2.intelligence = 12
        possible: list[str] = perso2.chercher_les_choix_possibles()
        possible.sort()
        assert possible == ["aventurier", "elfe",
                            "guerrier", "magicien", "nain"]

    def test_defini_au_hasard_la_classe(self):
        perso1 = generation_perso.Heros()
        perso1.defini_au_hasard_la_classe(["aventurier"])
        assert perso1.classe_metier == "aventurier"

        perso2 = generation_perso.Heros()
        perso2.defini_au_hasard_la_classe(["aventurier", "guerrier"])
        assert perso2.classe_metier in ["aventurier", "guerrier"]

        perso3 = generation_perso.Heros()
        perso3.defini_au_hasard_la_classe(
            ["aventurier", "elfe", "guerrier", "magicien", "nain"])
        assert perso3.classe_metier in [
            "aventurier", "elfe", "guerrier", "magicien", "nain"]

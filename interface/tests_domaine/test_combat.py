#! /usr/bin/env python3
# coding: utf-8

from domaine.combat import Combat, effectuer_un_tournois
from domaine.entite import Entite


class Test_combat():
    """Tests sur le domaine.Combat.
    Protagoniste : Dieu, qui à des caratèriqtique très élevé et monstre en bois très faible.
    Dieu gagne à tous les coups
    """

    def test_existance_intance_combat(self):
        petit_combat = Combat("Dieu", "Monstre en bois")
        assert petit_combat.attaquant == "Dieu" and petit_combat.defenseur == "Monstre en bois"

    def test_determine_degat(self):
        petit_combat = Combat("Dieu", "Monstre en bois")
        for i in range(100):
            assert 1 <= petit_combat.determine_degat(1, 1, 1) <= 6

    def test_effectue_combat(self):
        dieu = Entite(classe="Dieu", pvmax=999, attaque=20, parade=20,
                      nb_de_degat=5, degat_bonus=10, valeur_protection=10)
        monstreenbois = Entite(classe="Monstre en bois", pvmax=1, attaque=1,
                               parade=1, nb_de_degat=1, degat_bonus=1, valeur_protection=1)
        petit_combat = Combat(dieu, monstreenbois)
        resultat = petit_combat.effectue_combat()
        assert resultat == dieu

    def test_effectuer_un_tournois(self):
        dieu = Entite(classe="Dieu", pvmax=999, attaque=20, parade=20,
                      nb_de_degat=5, degat_bonus=10, valeur_protection=10)
        monstreenbois = Entite(classe="Monstre en bois", pvmax=1, attaque=1,
                               parade=1, nb_de_degat=1, degat_bonus=1, valeur_protection=1)
        qui = [dieu, monstreenbois]
        resultat = effectuer_un_tournois(qui, 100)
        assert resultat == [[0, 100], [0, 0]]
#! /usr/bin/env python3
# coding: utf-8

from domaine.entite import Entite as Entite


class Test_entite():

    def test_existance_instance_d_ork(self):
        """simplement pour tester l'existance de la classe Entite, 
        avec un ork comme exemple.
        """
        instance_d_ork = Entite(pvmax=10, classe="ork")
        assert (type(instance_d_ork.pvencours) is int
                and instance_d_ork.classe == "ork")

    def test_est_vivant(self):
        """Pour tester Entite.est_vivant()"""
        instance_d_ork = Entite(pvmax=10)
        instance_d_ork.pvencours = 0
        assert instance_d_ork.est_vivant() == False
        instance_d_ork.pvencours = 10
        assert instance_d_ork.est_vivant() == True

    def test_jet_attaque(self):
        instance_d_ork = Entite(pvmax=10, attaque=10)
        assert instance_d_ork.jet_attaque(5) == True
        assert instance_d_ork.jet_attaque(15) == False

    def test_jet_parade(self):
        instance_d_ork = Entite(pvmax=10, parade=10)
        assert instance_d_ork.jet_parade(5) == True
        assert instance_d_ork.jet_parade(15) == False
#! /usr/bin/env python3
# coding: utf-8

#import pytest
#import os

# Ligne nécessaire pour certaines configurations
#pytest.main(args=['-s', os.path.abspath('test_combatentremonstre.py')])

#import programme.combatentremonstre as combatentremonstre
import programme.combatentremonstre as combatentremonstre

"""Test combat entre monstre"""

class Test_combatentremonstre():
    
    def test_existance_monstre(self):
        """simplement pour tester l'existance de la classe Perso"""
        monstre = combatentremonstre.Perso(pvmax = 10, classe = "ork")
        assert type(monstre.pvencours) is int and monstre.classe == "ork"
        
    def test_est_vivant(self):
        """Pour tester Perso.est_vivant()"""
        monstre1 = combatentremonstre.Perso(pvmax = 10)
        monstre1.pvencours = 0
        assert monstre1.est_vivant() == False 
        monstre2 = combatentremonstre.Perso(pvmax = 10)
        monstre2.pvencours = 10
        assert monstre2.est_vivant() == True 
    
    def test_jet_attaque(self):
        monstre1 = combatentremonstre.Perso(pvmax = 10, attaque = 10)
        assert monstre1.jet_attaque(5) == True 
        assert monstre1.jet_attaque(15) == False 
        
    def test_jet_parade(self):
        monstre1 = combatentremonstre.Perso(pvmax = 10, parade = 10)
        assert monstre1.jet_parade(5) == True 
        assert monstre1.jet_parade(15) == False 
        

        
        
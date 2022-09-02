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
        monstre = combatentremonstre.Perso(pvmax = 10, classe = "ork")
        assert type(monstre.pvencours) is int and monstre.classe == "ork"
        
    def test_est_vivant(self):
        monstre1 = combatentremonstre.Perso(pvmax = 10, classe = "ork")
        monstre1.pvencours = 0
        assert monstre1.est_vivant() == False 
        monstre2 = combatentremonstre.Perso(pvmax = 10, classe = "ork")
        monstre2.pvencours = 0
        assert monstre2.est_vivant() == True 

        
        
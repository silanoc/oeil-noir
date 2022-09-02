#! /usr/bin/env python3
# coding: utf-8

import pytest
import os

# Ligne nécessaire pour certaines configurations
pytest.main(args=['-s', os.path.abspath('test_combatentremonstre.py')])

import programme.combatentremonstre as combatentremonstre

"""Test combat entre monstre"""

class Test_combatentremonstre():
    
    def test_existance_monstre(self):
        #monstre = combatentremonstre.Perso()
        #assert type(monstre.pvencours) is int 
        pass
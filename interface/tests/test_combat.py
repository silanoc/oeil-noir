#! /usr/bin/env python3
# coding: utf-8

from domaine.combat import Combat

class Test_combat():
    
    def test_existance_intance_combat(self):
        petit_combat = Combat("Dieu", "Monstre en bois")
        assert petit_combat.attaquant == "Dieu" and petit_combat.defenseur == "Monstre en bois"
    
    def test_determine_degat(self):
        petit_combat = Combat("Dieu", "Monstre en bois")
        for i in range (100):
            assert 1 <= petit_combat.determine_degat(1,1,1) <= 6
        
        
        
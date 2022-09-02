#! /usr/bin/env python3
# coding: utf-8

import domaine.lanceur_de as lanceur_de

"""Test les lanceurs de dé"""

def test_d20():
    """Vérifie que le résultat est compris entre 1 et 20 (bornes incluses"""
    chiffre = lanceur_de.d20()
    for i in range(100):
        assert 0 < chiffre < 21
    
def test_d6():
    """Vérifie que le résultat est compris entre 1 et 6 (bornes incluses"""
    for i in range(100):
        assert 0 < lanceur_de.d6() < 7
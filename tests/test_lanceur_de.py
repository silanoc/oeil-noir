#! /usr/bin/env python3
# coding: utf-8

import programme.lanceur_de as lanceur_de

"""Test les lanceurs de dé"""

def test_d20():
    """Vérifie que le résultat est compris entre 1 et 20 (bornes incluses"""
    chiffre = lanceur_de.d20()
    assert 0 < chiffre < 21
    
def test_d6():
    """Vérifie que le résultat est compris entre 1 et 6 (bornes incluses"""
    assert 0 < lanceur_de.d6() < 21
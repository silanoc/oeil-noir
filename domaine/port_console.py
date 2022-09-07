#! /usr/bin/env python3
# coding: utf-8

from domaine.entite import generer_des_monstre

def recupere_la_liste_des_monstre() -> list:
    liste_a_retourner = generer_des_monstre()
    return liste_a_retourner
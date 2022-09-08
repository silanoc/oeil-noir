#! /usr/bin/env python3
# coding: utf-8

from domaine.entite import Entite, generer_des_monstre
from domaine.combat import Combat, effectuer_un_tournois


def recupere_la_liste_des_monstre() -> list:
    liste_a_retourner: list = generer_des_monstre()
    return liste_a_retourner


def détermine_le_vainceur_d_un_combat_simple(combattant1, combattant2) -> Entite:
    combatencours: Combat = Combat(combattant1, combattant2)
    quiestvainqueur: Entite = combatencours.effectue_combat()
    return quiestvainqueur


def determine_le_resultat_du_tournois(qui, nbcombat):
    resultat = effectuer_un_tournois(qui, nbcombat)
    return resultat
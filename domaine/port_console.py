#! /usr/bin/env python3
# coding: utf-8

"""port faisant l'interface entre domaine et interface.console.combatentremonstre"""

from typing import List
from domaine.entite import Entite, generer_des_monstre
from domaine.combat import Combat, effectuer_un_tournois


def recupere_la_liste_des_monstre() -> list:
    liste_a_retourner: list = generer_des_monstre()
    return liste_a_retourner


def détermine_le_vainceur_d_un_combat_simple(combattant1: Entite, combattant2: Entite) -> Entite:
    combatencours: Combat = Combat(combattant1, combattant2)
    quiestvainqueur: Entite = combatencours.effectue_combat()
    return quiestvainqueur


def determine_le_resultat_du_tournois(qui: list[Entite], nbcombat: int) -> List[List[int]]:
    resultat: List[List[int]] = effectuer_un_tournois(qui, nbcombat)
    return resultat
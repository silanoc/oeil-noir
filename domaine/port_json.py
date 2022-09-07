#! /usr/bin/env python3
# coding: utf-8

import json

#from domaine.entite import Entite

"""
def mettre_contenu_json_dans_liste(adresse = "interface/json/data_monstre.json") -> list:
    contenu: list = []
    for tous_les_item in json.load(open(adresse)):
        contenu.append(Entite(**tous_les_item))
    return contenu
"""

def mettre_le_contenu_json_dans_dico(adresse = "interface/json/data_monstre.json") -> dict:
    contenu = json.load(open(adresse))
    return contenu       
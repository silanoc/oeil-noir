#! /usr/bin/env python3
# coding: utf-8

import json

"""port faisant l'interface entre domaine et interface.json"""


def mettre_le_contenu_json_dans_dico(adresse="interface/json/data_monstre.json") -> dict:
    contenu = json.load(open(adresse))
    return contenu
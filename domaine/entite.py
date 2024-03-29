#! /usr/bin/env python3
# coding: utf-8

"""génération des monstres et des personnages"""

from domaine.lanceur_de import d20
import domaine.port_json


class Entite:
    """Une entité peut être un hèros ou un monstre. Dans tous les cas, ils ont des attributs et méthodes communes.
    
    constructeur :
    * initialise via les valeurs d'un dictionnaire
    * attribue les pvencous en fonction de ceux max
    """
    def __init__(self, **tous_les_monstres):
        for attr_name, attr_value in tous_les_monstres.items():
            setattr(self, attr_name, attr_value)
        self.pvencours: int  =  self.pvmax
        
    def jet_attaque(self, jet: int = d20()) -> bool:
        """Defini si l'attaque est réussi, avec un 1d20 en paramètre (la fonction ne fait donc que comparer).
        Réussi si le jet est inférieur à la valeur d'attaque
        
        :param int jet: valeur de jet de dé exécuté en paramètre
        
        :returns reussite_attaque
        :rtype bool
        """
        return jet < self.attaque
    
    def jet_parade(self, jet: int = d20()) -> bool:
        """Fait un test de parade avec 1d20 passé en paramètre.
        Fonction non refactorisé en 1 ligne, comme jet_attaque, au cas envie de rendre le code bavard.
        Réussi si le jet est inférieur à la valeur de parade
        
        :returns reussite_parade
        :rtype bool
        """
        if jet < self.parade:
            reussite_parade = True
            #print ("parade reussite " +str(jet))
        else :
            reussite_parade = False
            #print ("parade ratée " + str(jet))
        return reussite_parade 
    
    def est_vivant(self) -> bool:
        """regarde la valeur de pvencours. Vivant (donc true) si au mpoins 1 pv
        
        :returns True ou False
        :rtype bool
        """
        return self.pvencours > 0
    

def generer_des_monstre() -> list:
    """Mettre dans une liste une instance d'Entité pour chaque monstre issus d'un dictionnaire.
    Ce dictionnaire provient d'un fichier json, lu par le port_json
    
    :returns: liste_monstre
    :rtype: list
    """
    dico_monstre: dict = domaine.port_json.mettre_le_contenu_json_dans_dico()
    liste_monstre: list = []
    for tous_les_item in dico_monstre:
        liste_monstre.append(Entite(**tous_les_item))
    return liste_monstre
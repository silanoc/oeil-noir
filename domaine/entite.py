#! /usr/bin/env python3
# coding: utf-8

from domaine.lanceur_de import d20

#----------
# classes pour générer les personnages 
# et leurs méthodes
#---------

class Entite:
    """Une entité peut être un hèros ou un monstre. Dans tous les cas, ils ont des attributs et méthodes communes."""
    def __init__(self, **tous_les_monstres):
        """constructeur
        initialise via les valeurs de json
        attribue les pvencous en fonction de ceux max
        """
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
        #jet: int = d20()
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
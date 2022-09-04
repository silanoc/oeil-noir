#! /usr/bin/env python3
# coding: utf-8

from domaine.lanceur_de import d6, d20 
from domaine.entite import Entite as Entite

class Combat():
    
    def __init__(self,joueur1: Entite, joueur2: Entite) -> None:
        """Defini l'attaquant et le défenseur dans un combat.
        
        :param Entite joueur1: une instance de Entite
        :param Entite joueur2: une instance de Entite"""
        self.attaquant = joueur1
        self.defenseur = joueur2
    
    def determine_degat(self,nbdedegat: int ,valbonus: int, chiffre_protection: int) -> int:
        """défini le nmbre de point de dégat du type 2d6+2 - protection d'armure
        soit [nbdedegat]d6+[valbonus] - [chiffre_protection]
        Ne peux pas être négatif
        
        """
        degat: list[int] = [d6() for i in range(nbdedegat)]
        complement: list[int] = [valbonus, chiffre_protection * -1 ]
        degat.extend(complement)
        totaldegat: int = sum(degat)
        if totaldegat < 0 : totaldegat = 0
        return totaldegat
        
        """
        degat: int = 0
        for i in range (nbdedegat):
            degat += d6()
        degat = degat + valbonus - chiffre_protection
        if degat < 0:
            degat = 0
        return degat
        """
    
    def effectue_combat(self) -> Entite:
        self.attaquant.pvencours: int = self.attaquant.pvmax
        self.defenseur.pvencours: int = self.defenseur.pvmax
        tour_combat: int = 0  
        while ((self.attaquant.pvencours >= 0) and (self.defenseur.pvencours >= 0)):
        #while self.attaquant.est_vivant() and self.defenseur.est_vivant():
            tour_combat += 1
            #print("tour :" + str(tour_combat))
            att = self.attaquant.jet_attaque(d20())
            if att == True:
                defe = self.defenseur.jet_parade(d20())
                if defe == False:
                    self.defenseur.pvencours -= self.determine_degat(self.attaquant.nb_de_degat, self.attaquant.degat_bonus,self.defenseur.valeur_protection)
                    #print("def pv : " + str(self.defenseur.pvencours))
                    if self.defenseur.pvencours <= 0:
                    #if not self.defenseur.est_vivant:
                        gagnant = self.attaquant
                        return gagnant
                        break
            att = self.defenseur.jet_attaque(d20())
            if att == True:
                defe = self.attaquant.jet_parade(d20())
                if defe == False:
                    self.attaquant.pvencours -= self.determine_degat(self.defenseur.nb_de_degat, self.defenseur.degat_bonus,self.attaquant.valeur_protection)
                    #print ("att pv : "+str(self.attaquant.pvencours))
                    if self.attaquant.pvencours <= 0:
                        gagnant = self.defenseur
                        return gagnant                  
                        break                
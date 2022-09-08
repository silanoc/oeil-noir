#! /usr/bin/env python3
# coding: utf-8

from typing import List

from domaine.lanceur_de import d6, d20 
from domaine.entite import Entite as Entite

class Combat():
    """Defini l'attaquant et le défenseur dans un combat.
    Classe permattant d'effectuer le combat entre les deux.
        
    :param Entite joueur1: une instance de Entite
    :param Entite joueur2: une instance de Entite
    """
    
    def __init__(self,joueur1: Entite, joueur2: Entite) -> None:
        self.attaquant = joueur1
        self.defenseur = joueur2
    
    def determine_degat(self,nbdedegat: int ,valbonus: int, value_protection: int) -> int:
        """défini le nombre de point de dégat du type 2d6+2 - protection d'armure
        soit [nbdedegat]d6+[valbonus] - [value_protection]
        Ne peux pas être négatif
        
        :param int nbdedegat: nombre de dé de dégat.
        :param int valbonus: nombre de dégat bonus, peut etre négatif.
        :param int value_protection: valeur de la protection. 
            Nbre positif, doit être soustrait ou passé en négatif pour addition.
        
        :returns: totaldegat 
        :rtype: int
        """
        degat: list[int] = [d6() for i in range(nbdedegat)]
        complement: list[int] = [valbonus, value_protection * -1 ]
        degat.extend(complement)
        totaldegat: int = sum(degat)
        if totaldegat < 0 : totaldegat = 0
        return totaldegat
    
    def effectue_combat(self) -> Entite:
        """Le combat est constitué d'assaut. Un assaut de 2 phases.
        A chaque phase on alterne qui attaque et qui pare.
        Le combat s'arrete quand un des deux n'a plus de point de vie.
        
        :returns: gagnant, qui des deux protagonistes à gagné le combat.
        :rtype: Entite
        
        """
        self.attaquant.pvencours: int = self.attaquant.pvmax
        self.defenseur.pvencours: int = self.defenseur.pvmax
        nb_assaut: int = 0
        phase:int = 1
        gagnant = None
        #while self.attaquant.pvencours >= 0 and self.defenseur.pvencours >= 0:
        while self.attaquant.est_vivant and self.defenseur.est_vivant:
            nb_assaut += 1
            #print("Assaut numéro :" + str(nb_assaut))
            if phase == 1:
                self.phase_combat(celui_qui_attaque = self.attaquant, celui_qui_pare = self.defenseur)
                phase: int = 2    
            elif phase == 2:
                self.phase_combat(celui_qui_attaque = self.defenseur, celui_qui_pare = self.attaquant)
                phase: int = 1

            if self.attaquant.pvencours < 0:
                gagnant: Entite =  self.defenseur
                break    
            if self.defenseur.pvencours < 0:
                gagnant: Entite = self.attaquant
                break      
        return gagnant
            
    def phase_combat(self, celui_qui_attaque: Entite, celui_qui_pare: Entite):
        """1 phase :
        La personne qui attaque doit faire un test d'attaque.
        Si loupé, fin.
        Si réussit, le défenseur doit testé sa parade.
        Si la parade est réussi, aucun dégat, sinon calculer retirer les dégats des pv en cours.
        
        :param Entite celui_qui_attaque:
        :param Entite celui_qui_pare"""
        att: bool =  celui_qui_attaque.jet_attaque(d20())
        if att == True:
            defe: bool =  celui_qui_pare.jet_parade(d20())
            if defe == False:
                celui_qui_pare.pvencours -= self.determine_degat(celui_qui_attaque.nb_de_degat,
                                                                      celui_qui_attaque.degat_bonus,
                                                                      celui_qui_attaque.valeur_protection) 

                
def effectuer_un_tournois(participants: list, nbround: int) -> List[List[int]]:
    resultats: List[List[int]]  =  [[0] * (len(participants)) for _ in range(len(participants))]
    for nmbredecombat in range(nbround):
        for i in range(0, len(participants)):
            for j in range (i+1,len(participants)):
                #print (participants[i],participants[j])
                combatencours = Combat(participants[i],participants[j])
                quiestvainqueur = combatencours.effectue_combat()
                if quiestvainqueur == participants[i]:
                    resultats[i][j]+= 1
                else:
                    resultats[j][i]+= 1
    return resultats
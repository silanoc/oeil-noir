#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#------------------
#simulateur de combat autour du JdR l'oeil noir
#auteur : silanoc
#sur téléphone portable - juillet 2019
#version 1
#--------------------

from random import *
	
#--------
# jet de dé
#---------
	
def d20():
    a =randint(1,20)
    return a
    
def d6():
    a =randint(1,6)
    return a

#----------
# classes pour générer les personnages 
# et leurs méthodes
#---------

class perso:
    def __init__(self):
        self.classe="generique"
        self.courage=10
        self.attaque=10
        self.parade=8
        self.degat=2
        self.nb_de_degat=1
        self.degat_bonus=1
        self.pvmax=10
        self.pvencours=self.pvmax
        self.valeur_protection=1
        self.classe_de_monstre=1
    def jet_attaque(self):
        jet=d20()
        if jet<self.attaque:
            reussite_attaque=True
            #print ("attaque reussite " +str(jet))
        else :
            reussite_attaque=False
            #print ("attaque ratée " + str(jet))
        return reussite_attaque
    def jet_parade(self):
        jet=d20()
        if jet<self.parade:
            reussite_parade=True
            #print ("parade reussite " +str(jet))
        else :
            reussite_parade=False
            #print ("parade ratée " + str(jet))
        return reussite_parade 

#-------------#
#  Bestiaire  #
#-------------#

class ork(perso):
    def __init__(self):
        perso.__init__(self)
        self.classe="ork"
        self.courage=8
        self.attaque=9
        self.parade=7
        self.pvmax=8
        self.pvencours=self.pvmax
        self.valeur_protection=2
        #self.degat=1d+4
        self.nb_de_degat=1
        self.degat_bonus=4
        self.classedemonstre=8

class gobelin(perso):
    def __init__(self):
        perso.__init__(self)
        self.classe="gobelin"
        self.courage=5
        self.attaque=7
        self.parade=6
        self.pvmax=12
        self.pvencours=self.pvmax
        self.valeur_protection=2
        #self.degat=1d+2
        self.nb_de_degat=1
        self.degat_bonus=2
        self.classedemonstre=5
        
class ogre(perso):
    def __init__(self):
        perso.__init__(self)
        self.classe="ogre"
        self.courage=22
        self.attaque=6
        self.parade=5
        self.pvmax=40
        self.pvencours=self.pvmax
        self.valeur_protection=3
        #self.degat=2d+4
        self.nb_de_degat=2
        self.degat_bonus=4
        self.classedemonstre=18
        
class troll(perso):
    def __init__(self):
        perso.__init__(self)
        self.classe="troll"
        self.courage=25
        self.attaque=8
        self.parade=8
        self.pvmax=50
        self.pvencours=self.pvmax
        self.valeur_protection=3
        #self.degat=3d
        self.nb_de_degat=3
        self.degat_bonus=0
        self.classedemonstre=30
        
class kobold(perso):
    def __init__(self):
        perso.__init__(self)
        self.classe="kobold"
        self.courage=10
        self.attaque=16
        self.parade=4
        self.pvmax=20
        self.pvencours=self.pvmax
        self.valeur_protection=1
        #self.degat=1d
        self.nb_de_degat=1
        self.degat_bonus=0
        self.classedemonstre=15
        
class dragon_volant(perso):
    def __init__(self):
        perso.__init__(self)
        self.classe="dragon volant"
        self.courage=20
        self.attaque=7
        self.parade=5
        self.pvmax=50
        self.pvencours=self.pvmax
        self.valeur_protection=4
        #self.degat=1d+4
        # griffe=1d
        # dent 2d
        # queue 1d
        self.nb_de_degat=2
        self.degat_bonus=0
        self.classedemonstre=50
    

#-----------
# classe pour générer un combat entre 2 protagonistes
#---------

class combat():
    def __init__(self,joueur1, joueur2):
        self.attaquant=joueur1
        self.defenseur=joueur2
    def determine_degat(self,nbdedegat,valbonus,chiffre_protection):
        degat=0
        for i in range (nbdedegat):
            degat+=d6()
        degat+=valbonus
        degat=degat-chiffre_protection
        if degat<0:
            degat=0
        return degat
    def effectue_combat(self):
        self.attaquant.pvencours=self.attaquant.pvmax
        self.defenseur.pvencours=self.defenseur.pvmax
        tour_combat=0  
        while ((self.attaquant.pvencours>=0) and (self.defenseur.pvencours>=0)):
            tour_combat+=1
            #print("tour :" + str(tour_combat))
            att=self.attaquant.jet_attaque()
            if att==True:
                defe=self.defenseur.jet_parade()
                if defe==False:
                    self.defenseur.pvencours-=self.determine_degat(self.attaquant.nb_de_degat, self.attaquant.degat_bonus,self.defenseur.valeur_protection)
                    #print("def pv : " + str(self.defenseur.pvencours))
                    if self.defenseur.pvencours<=0:
                        gagnant=self.attaquant
                        return gagnant
                        break
            att=self.defenseur.jet_attaque()
            if att==True:
                defe=self.attaquant.jet_parade()
                if defe==False:
                    self.attaquant.pvencours-=self.determine_degat(self.defenseur.nb_de_degat, self.defenseur.degat_bonus,self.attaquant.valeur_protection)
                    #print ("att pv : "+str(self.attaquant.pvencours))
                    if self.attaquant.pvencours<=0:
                        gagnant=self.defenseur
                        return gagnant                  
                        break                   

#------
# fonctions pour le programme
#------

def bannieredebutprogramme():
    #a afficher au début
    print("-------------------------------------------------------------------")
    print("Bienvenue dans mon programme de simulation de combat de l'oeil noir")
    print("___________________________________________________________________")
    print("")

def genererlesmonstres():
    #générer les instances de monstre à partir des objets
    global ork1, gobelin1, ogre1, troll1, kobold1, dragonvolant1
    ork1=ork()   
    gobelin1=gobelin()
    ogre1=ogre()
    troll1=troll()
    kobold1=kobold()
    dragonvolant1=dragon_volant()

def tournoisentremonstre():
    #initialisation des participants et des scores
        participants=[ork1, gobelin1, ogre1, troll1, kobold1, dragonvolant1]
        resultats=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        nbround=int(input("Combien de combats souhaitez-vous ?"))
        #combat
        for nmbredecombat in range(nbround):
            for i in range(0, len(participants)):
                for j in range (i+1,len(participants)):
                    #print (participants[i],participants[j])
                    combatencours=combat(participants[i],participants[j])
                    quiestvainqueur=combatencours.effectue_combat()
                    if quiestvainqueur==participants[i]:
                        resultats[i][j]+=1
                    else:
                        resultats[j][i]+=1
        #affiche les resultats
        for k in range (6):
            print(str(participants[k].classe) +"\t"+ str(resultats[k]))


#-----------
# déroulement du programme
#--------     

if __name__=="__main__":

    genererlesmonstres()
    bannieredebutprogramme()
    
    user_answer="a"
    user_answer=input("Que voulez vous faire : \n un tournois (taper 1) ou quitter (taper Q) \n")
    while user_answer != "Q":
        tournoisentremonstre()                    
        user_answer = input("Que voulez vous faire : \n un tournois (taper 1) ou quitter (taper Q) \n")


        
               
##Test pour 1 combat
##
##combatencours=combat(ork1,gobelin1)
##combatencours.effectue_combat()
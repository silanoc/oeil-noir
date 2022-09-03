![Logo 1ère édition oeil noir](./images/320px-L'Œil_noir_(première_édition)_Logo.svg.png)
# Projet : simulation de l'œil noir
Auteur : silanoc
date création : 5 avril 2021
dernière modification : 15 avril 2021
refonte totale: début septembre 2022

## Sources du jeu
Les codes sont faits à partir du jeu de rôle l'œil noir, plus précisement à partir des règles de la 1ère édition. Tout simplement parce que c'est à partir de cela que j'ai découvert le JDR.
* article wikipedia https://fr.wikipedia.org/wiki/L%27%C5%92il_noir
* pour télécharger les règles, scénarios... : 
    * http://oeilnoir.jdr.free.fr/telechargements/telechargements_regles.htm
    * http://www.jdrp.fr/site/l-oeil-noir-jdr-24.html
## Objectif 
- Faire des simulations de combat autour des règles du JDR l'œil noir
- Améliorer mes connaissances de codage en utilisant la méthode de projet comme mis en avant par le réseau Planète Science.
## Contenu
Le premier fichier *combatentremonstre.py* est issus d'un travail sur mon ordiphone dans les transports en commun et permet de tester qui est le plus fort entre les 6 monstres du livre des règles de base. Il est amélioré par la suite de façon plus classique sur ordinateur.
Cela permet de tester le système de combat, et de répondre à la question : quel est le monstre le plus puissant ?
Pour cela, on organise un tournoi, où chaque monstre combat 1000 fois chacun des autres et l'on compte le nombre de victoires.
Exemple de résultat obtenu :

| |ork|gobelin|ogre|troll|kobold|dragon volant|
|---|---|---|---|---|---|---|
|ork     |0|711| 21| 0| 523| 3|
|gobelin |289| 0| 0| 0| 311| 0|
|ogre    |979| 1000| 0|121| 999| 639|
|troll   |1000| 1000| 879| 0| 1000| 969|
|kobold  |477| 689| 1| 0| 0| 0|
|dragon volant	|997| 1000|361| 31| 1000| 0|

S'il n'y a pas d'erreur dans le code, c'est donc le troll le plus puissant !

## Refonte en architecture hexagonale

```
oeil noir
|
+-- domaine
|   |
|   +-- entite.py - contient la classe entitée, qui permet de générer des héros ou monstres
|   +-- generation_perso.py - pour génere au hasard un héros
|   +-- lanceur_de.py - pour lander de d6 ou d20
|
+-- interface
|   |
|   +-- console
|   +-- json - les données (caractèristiques des monstres...) sont dans des fichiers json
|   +-- tests - 1 fichier de test par fichier dans le domaine
|
+-- programme - à vider tranquillement
    |
    +-- combatentremonstre.py - le programme initial, qui est transformé et amélioré
```
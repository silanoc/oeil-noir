# oeil-noir
Auteur : silanoc
date : 5 avril 2021

## Sources du jeu
Les codes sont fait à partir du jeu de rôle l'oeil noir, plus précisement à partir des régles de la 1ère édition. Tout simplement parce que c'est à partir de cela que j'ai découvert le jdr.
* article wikipedia
* pour télécharger les régles, scénarios... : 
    * http://oeilnoir.jdr.free.fr/telechargements/telechargements_regles.htm
    * http://www.jdrp.fr/site/l-oeil-noir-jdr-24.html
## objectif 
- Faire des simulations de combat autour des régles du jdr l'oeil noir

## contenu
Le premier fichier *combatentremonstre.py* est issus d'un travail sur le tel portable et permet de tester qui est le plus fort entre les 6 monstres du livre des règles de base.
Cela permet de tester le système de combat, et de répondre à la question : quel est le monstre le plus puissant ?
Pour cela on oraganise un tournois, ou chaque monstre combat 1000 fois chacun des autres et l'on compte le nombre de victoire.
Exemple de résultat obtenu

| |ork|gobelin|ogre|troll|kobold|dragon volant|
|---|---|---|---|---|---|---|
|ork     |0|711| 21| 0| 523| 3|
|gobelin |289| 0| 0| 0| 311| 0|
|ogre    |979| 1000| 0|121| 999| 639|
|troll   |1000| 1000| 879| 0| 1000| 969|
|kobold  |477| 689| 1| 0| 0| 0|
|dragon volant	|997| 1000|361| 31| 1000| 0|

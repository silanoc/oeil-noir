![Logo 1ère édition oeil noir](./images/320px-L'Œil_noir_(première_édition)_Logo.svg.png)
# Projet : simulation de l'œil noir
- Auteur : silanoc
- date création : 5 avril 2021
- dernière modification de la V0 : 15 avril 2021
- refonte totale: début septembre 2022. 

## Objectif 
- Faire des simulations de combat autour des règles du JDR l'œil noir. Savoir quel monstre du livre des règles est le plus fort.
- Améliorer mes connaissances de codage en utilisant la méthode de projet comme mis en avant par le réseau Planète Science.

## Lancement 
- exécuter `main.py`
- lire la doc `build/html/index.html`

## Docker
- `docker build -t oeil_noir_en_console .`
- `docker run -it oeil_noir_en_console`

- image téléchargeable sur : https://hub.docker.com/r/silanoc/oeil_noir

## Refonte en architecture hexagonale
Les dossiers et fichiers principaux

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
+-- images
|   |
|   +-- pixel_art_logo_oeil_noir.txt - pour affichage console
|
+-- programme - à vider tranquillement
    |
    +-- combatentremonstre.py - le programme initial, qui est transformé et amélioré
```
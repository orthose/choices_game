# choices_game
Descriptif: Progiciel de jeu narratif à choix multiples entièrement personnalisable
Langage de programmation: Python 3
Bibliothèque graphique: Tkinter

Comment l'installer et l'exécuter sous Ubuntu 20.04 ?
-----------------------------------------------------

1. Installer Python 3 <sudo apt install python3>

2. Cloner le répertoire git <git clone https://github.com/orthose/choices_game>

3. Supprimer les répertoires de git <rm -rf .git*>

4. Installer les bibliothèques tierces suivantes
<sudo apt install -y python-pil.imagetk>
<sudo apt install python3-pygame>

5. Exécuter le programme <python3 choices_game.py>

Comment l'installer et l'exécuter sous Windows 10 ?
---------------------------------------------------

1. Installer (gratuitement) Python 3.8 depuis le Windows Store
ou en téléchargeant l'installateur depuis https://www.python.org/downloads/windows

2. Récupérer l'archive zip du programme depuis https://github.com/orthose/choices_game

3. Supprimer le fichier .gitignore

4. Installer les bibliothèques tierces suivantes
<pip install pillow>
<pip install pygame>

5. Exécuter le programme <python choices_game.py>
ou double-cliquer sur le fichier choices_game.py

Comment personnaliser le jeu ?
------------------------------

1. Ouvrir le dossier config/ contenant tous les fichiers de personnalisation

2. Compléter et modifier le fichier config/pages.py afin de créer le scénario du jeu
et personnaliser le rendu graphique de chaque page

3. Compléter le dictionnaire de config/alias.py afin d'ajouter des alias pouvant
être utilisés dans le texte des pages

4. Modifier les valeurs des variables de config/config.py afin de modifier le rendu
graphique par défaut de toutes les pages du jeu

5. Ajouter des images au format .jpg dans le dossier pictures/

6. Ajouter des musiques au format .mp3 dans le dossier sounds/

ATTENTION: Ne modifier aucun autre fichier que ceux cités, sous peine d'affecter le bon
fonctionnement du programme

Auteur: Maxime VINCENT

#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

from Page import *

# TODO: Pages de données du jeu à modifier pour personnalisation

# Couleurs pré-paramétrées
white = "#ffffff"


# Liste de toutes les pages
# Pensez à créer au minimum une page d'accueil,
# une page de victoire et une page de défaite
accueil = Page("Page d'accueil")
histoire = Page("Page du scénario")


# Première page à afficher obligatoire
# pour démarrer le jeu
Page.first_page = accueil


# Page d'accueil obligatoire pour démarrer le jeu
# Paramétrage de l'image à afficher
accueil.image = "accueil.jpg"
# Paramétrage du texte à afficher
# Vous pouvez utiliser des alias de la forme @alias
# Pour cela ajouter les dans le fichier alias.py
accueil.text = "Bienvenue dans @game. Un jeu fait pour vous émerveiller de la beauté de la nature. Voulez-vous commencer à jouer ?"
# Ajout d'un choix à la page
accueil.add_choice("Oui, allons-y.", histoire)
accueil.add_choice("Je préfère réfléchir", accueil)
histoire.add_choice("Revenir à l'accueil", accueil)
# Il existe de nombreuses variables de personnalisation graphique
# Pour les connaître démarrer l'interpréteur python3
# import Page; help(Page); help(Page.GraphicalParameters)
# Les valeurs possibles pour ces variables sont fournies 
# en partie dans les fichiers texte du dossier config
# Vous pouvez également retrouver de plus amples renseignements
# à l'adresse http://tkinter.fdex.eu/doc/sa.html
# Si vous ne les paramétrez pas manuellement pour chaque page
# ce seront les valeurs par défaut du fichier config.py qui
# seront utilisées
accueil.graphic_global.background = white

# Vérification de la validité des choix de chaque page
# Ne pas commenter ou supprimer
Page.check_choices()


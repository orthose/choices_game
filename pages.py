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
herbe = "#22ee22"


# Liste de toutes les pages
accueil = Page("Le commencement d'une belle aventure")
victoire = Page("Une belle réussite")


# Première page à afficher
Page.first_page = accueil


# Page d'accueil obligatoire
accueil.image = "accueil.jpg"
accueil.text = "Bienvenue dans @game. Un jeu fait pour vous émerveiller de la beauté de la nature. Voulez-vous commencer à jouer ?"
accueil.add_choice("Non, je ne préfère pas.", accueil)
accueil.add_choice("Oui, allons-y.", victoire)
accueil.graphic_global.background = herbe

# Page de victoire
victoire.image = "victoire.img"
victoire.text = "Vous venez de remporter la partie ! Bravo pour tous vos efforts !"
victoire.add_choice("Recommencer", accueil)


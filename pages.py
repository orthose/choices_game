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
histoire = Page("Voici toute l'histoire")
victoire = Page("Une belle réussite")
defaite = Page("Une défaite cuisante")


# Première page à afficher
Page.first_page = accueil


# Page d'accueil obligatoire
accueil.image = "accueil.jpg"
accueil.text = "Bienvenue dans @game. Un jeu fait pour vous émerveiller de la beauté de la nature. Voulez-vous commencer à jouer ?"
accueil.add_choice("Oui, allons-y.", histoire)
accueil.graphic_global.background = herbe

histoire.text = "Je marche dans la forêt quand soudain je vois un chevreuil."
histoire.add_choice("Je le tue", defaite)
histoire.add_choice("Je le laisse en vie", victoire)
histoire.add_choice("Je rentre chez moi", accueil)

# Page de victoire
victoire.image = "victoire.jpg"
victoire.text = "Vous venez de remporter la partie ! Bravo pour tous vos efforts !"
victoire.add_choice("Recommencer", accueil)
victoire.add_choice("Je veux perdre !", defaite)

defaite.text = "Vous avez perdu la partie... Désolé..."
defaite.add_choice("Accueil", accueil)
defaite.add_choice("Victoire", victoire)


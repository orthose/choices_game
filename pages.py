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
space_color = "#3387c0"


# Liste de toutes les pages
accueil = Page("accueil")
vaisseau = Page("vaisseau")
furtif = Page("furtif")
destroyeur = Page("destroyeur")


# Page d'accueil obligatoire
accueil.image = "accueil.jpg"
accueil.background = space_color
accueil.text = "Bienvenue dans @game. La guerre a été déclarée par @enemy. @friend doit réagir au plus vite !"
accueil.add_choice("Commencer", vaisseau)


# Page de choix du vaisseau
vaisseau.image = "vaisseau.jpg"
vaisseau.background = space_color
vaisseau.text = "Veuillez choisir votre vaisseau spatial de combat..."
vaisseau.add_choice("Le Furtif, un vaisseau aussi silencieux que la brise !", furtif)
vaisseau.add_choice("Le Destroyeur, un vaisseau qui fonce dans le tas !", destroyeur)



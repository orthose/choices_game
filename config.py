#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

# Variables globales de la configuration graphique
# Elles sont personnalisables avec précautions
# Pour les paramétrer se référer au site web :
# http://tkinter.fdex.eu/doc/sa.html

from pages import *

# Couleur par défaut de l'arrière-plan d'une page
default_background_page = "#ffffff"

# Titre par défaut de la fenêtre
default_window_title = "Jeu des Choix"

# Titre par défaut d'une page
default_page_title = "Page sans nom"

# Couleur par défaut de l'arrière-plan du titre d'une page
default_background_title = "#ffffff"

# Couleur par défaut du texte du titre d'une page
default_foreground_title = "black"

# Épaisseur par défaut de l'étiquette du titre d'une page
default_borderwidth_title = None

# Relief par défaut de l'étiquette du titre d'une page
default_relief_title = "flat"

# Titre par défaut d'une page
default_font_title = ('Ubuntu', 30, 'bold')

# Image par défaut d'une page
default_image = "default_image.jpg"

# Couleur par défaut de l'arrière-plan
# du choix 1 lorsque le curseur passe devant
default_activebackground_choice1 = "yellow"

def configure_first_page(page):
    """Permet de configurer la première page
    à s'afficher automatiquement, en modifiant
    toutes les valeurs par défaut.
    :param page: Page d'entrée dans le jeu
    :type page: Page
    """
    pass


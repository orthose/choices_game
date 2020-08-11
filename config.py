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
default_page_background = "#ffffff"

# Titre par défaut de la fenêtre
default_window_title = "Jeu des Choix"

# Titre par défaut d'une page
default_page_title = "Page sans nom"

# Couleur par défaut de l'arrière plan du titre d'une page
default_title_background = "#ffffff"

# Titre par défaut d'une page
default_title_font = ('Ubuntu', 30, 'bold')

# Image par défaut d'une page
default_image = "default_image.jpg"

def configure_first_page(page):
    """Permet de configurer la première page
    à s'afficher automatiquement, en modifiant
    toutes les valeurs par défaut.
    :param page: Page d'entrée dans le jeu
    :type page: Page
    """
    pass


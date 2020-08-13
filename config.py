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

#############################################
# Personnalisation de la fenêtre principale #
#############################################

# Titre par défaut de la fenêtre
default_window_title = "Jeu des Choix"

# Couleur par défaut de l'arrière-plan d'une page
default_background_page = "#ffffff"

# Curseur par défaut de la page
default_cursor_page = "left_ptr"

# Marges par défaut en x et y des widgets de la page
default_padx = 50; default_pady = 10

# Police par défaut de la page
default_font = ('Ubuntu', 15, 'normal')

#############################################
# Personnalisation de la zone de titre      #
#############################################

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

# Marges par défaut en x et y du titre d'une page
default_padx_title = default_padx; default_pady_title = default_pady

# Titre par défaut d'une page
default_font_title = ('Ubuntu', 30, 'bold')

#############################################
# Personnalisation de la zone d'image       #
#############################################

# Image par défaut d'une page
default_image = "default_image.jpg"

#############################################
# Personnalisation de la zone de texte      #
#############################################

# Texte par défaut de la zone de texte
default_text = "Exemple de texte"

# Couleur d'arrière-plan par défaut de la zone de texte
default_background_text = "#ffffff"

# Couleur de la police par défaut de la zone de texte
default_foreground_text = "black"

# Épaisseur par défaut de la zone de texte
default_borderwidth_text = None

# Relief par défaut de la zone de texte
default_relief_text = "flat" 

# Marges par défaut en x et y de la zone de texte
default_padx_text = default_padx; default_pady_text = default_pady

# Police par défaut de la zone de texte
default_font_text = default_font

#############################################
# Personnalisation de la zone de choix      #
#############################################

### Tuple pour les choix 1, 2, 3 et 4 ###

# Texte à afficher par défaut sur ce choix
default_text_choice = ("Choix 1", "Choix 2", "Choix 3", "Choix 4")

# Curseur par défaut du choix
default_cursor_choice = (default_cursor_page, ) * 4

# Arrière-plan par défaut du choix
default_background_choice = ("#ffffff", ) * 4

# Couleur par défaut de l'arrière-plan
# du choix 1 lorsque le curseur passe devant
default_activebackground_choice = ("yellow", ) * 4

# Couleur du texte par défaut du choix
default_foreground_choice = ("black", ) * 4

# Épaisseur par défaut du bouton de choix
default_borderwidth_choice = (None, ) * 4

# Relief par défaut du bouton de choix
default_relief_choice = ("groove", ) * 4 

# Marges par défaut en x et y des boutons
default_padx_choice = (default_padx, ) * 4
default_pady_choice = (default_pady, ) * 4

# Police par défaut du bouton de choix
default_font_choice = (default_font, ) * 4


def configure_first_page(page):
    """Permet de configurer la première page
    à s'afficher automatiquement, en modifiant
    toutes les valeurs par défaut.
    :param page: Page d'entrée dans le jeu
    :type page: Page
    """
    pass


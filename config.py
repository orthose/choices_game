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

# Marges en x et y des widgets de la page
default_padx = 50; default_pady = 0

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

default_text = "Exemple de texte"
 
default_background_text = "#ffffff"

default_foreground_text = "black"

default_borderwidth_text = None

default_relief_text = "flat" 

default_font_text = default_font

#############################################
# Personnalisation de la zone de choix      #
#############################################

### Choice (1) ###

# Texte à afficher par défaut sur ce choix
default_text_choice1 = "Choix 1"

# Curseur par défaut du choix
default_cursor_choice1 = default_cursor_page

# Arrière-plan par défaut du choix
default_background_choice1 = "#ffffff"

# Couleur par défaut de l'arrière-plan
# du choix 1 lorsque le curseur passe devant
default_activebackground_choice1 = "yellow"

# Couleur du texte par défaut du choix
default_foreground_choice1 = "black"

# Épaisseur par défaut du bouton de choix
default_borderwidth_choice1 = None

# Relief par défaut du bouton de choix
default_relief_choice1 = "groove" 

# Police par défaut du bouton de choix
default_font_choice1 = default_font

### Choice (2) ###
 
default_text_choice2 = "Choix 2"

default_cursor_choice2 = default_cursor_page

default_background_choice2 = "#ffffff"

default_activebackground_choice2 = "yellow"

default_foreground_choice2 = "black"

default_borderwidth_choice2 = None

default_relief_choice2 = "groove" 

default_font_choice2 = default_font

### Choice (3) ###

default_text_choice3 = "Choix 3"

default_cursor_choice3 = default_cursor_page

default_background_choice3 = "#ffffff"

default_activebackground_choice3 = "yellow"

default_foreground_choice3 = "black"

default_borderwidth_choice3 = None

default_relief_choice3 = "groove" 

default_font_choice3 = default_font

### Choice (4) ###

default_text_choice4 = "Choix 4"

default_cursor_choice4 = default_cursor_page
 
default_background_choice4 = "#ffffff"

default_activebackground_choice4 = "yellow"

default_foreground_choice4 = "black"

default_borderwidth_choice4 = None

default_relief_choice4 = "groove" 

default_font_choice4 = default_font


def configure_first_page(page):
    """Permet de configurer la première page
    à s'afficher automatiquement, en modifiant
    toutes les valeurs par défaut.
    :param page: Page d'entrée dans le jeu
    :type page: Page
    """
    pass


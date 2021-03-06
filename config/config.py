#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

# TODO: Variables graphiques par défaut du jeu à modifier pour personnalisation
# Ce n'est pas obligatoire mais cela peut être utile pour un comportement
# harmonisé entre les pages si vous désirez créer une ambiance particulière


# Variables globales de la configuration graphique
# Elles sont personnalisables avec précautions
# Pour les paramétrer se référer au site web :
# http://tkinter.fdex.eu/doc/sa.html

#############################################
# Personnalisation de la fenêtre principale #
#############################################

# Titre par défaut de la fenêtre
default_window_title = "Jeu des Choix"

# Couleur par défaut de l'arrière-plan d'une page
default_background_page = "#ffffff"

# Curseur par défaut de la page
default_cursor_page = "left_ptr"

# Marges externes par défaut en x et y des widgets de la page
default_padx = 50; default_pady = 10

# Marges internes par défaut en x et y des widgets de la page
default_ipadx = 3; default_ipady = 3

# Police par défaut de la page
default_font_family = 'Ubuntu'
default_font_size = 15
default_font_weight = 'normal'
default_font = (default_font_family, default_font_size, default_font_weight)

# Disposition par défaut entre 0 et 3
default_placement_page = 0

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

# Marges internes par défaut en x et y du titre d'une page
default_padx_title = default_padx; default_pady_title = default_pady

# Marges externes par défaut en x et y du titre d'une page
default_ipadx_title = default_ipadx; default_ipady_title = default_ipady

# Titre par défaut d'une page
default_font_title = (default_font_family, default_font_size * 2, 'bold')

#############################################
# Personnalisation de la zone d'image       #
#############################################

# Image par défaut d'une page
default_image = "default_image.jpg"

# Marges par défaut en x et y de l'image
default_padx_image = default_padx; default_pady_image = default_pady
# Flottant pour diviser la hauteur de la fenêtre
# Le résultat fixe la hauteur de l'image
default_divider_height_image = 1.5

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

# Marges externes par défaut en x et y de la zone de texte
default_padx_text = default_padx; default_pady_text = default_pady

# Marges internes par défaut en x et y de la zone de texte
default_ipadx_text = default_ipadx; default_ipady_text = default_ipady

# Police par défaut de la zone de texte
default_font_text = default_font

# Police par défaut à utiliser pour les tags des alias
default_tag_font_text = (default_font_family, default_font_size, 'bold')

# Couleur d'arrière-plan par défaut pour les tags des alias
default_tag_background_text = "#ffffff"

# Couleur de police par défaut pour les tags des alias
default_tag_foreground_text = "red"

# Raye les tags des alias si fixé à 1
default_tag_overstrike_text = 0

# Souligne les tags des alias si fixé à 1
default_tag_underline_text = 0

# Nombre de lignes de la zone de texte
default_lines_text = 4

#############################################
# Personnalisation de la zone de choix      #
#############################################

### Tuple pour les choix 1, 2, 3 et 4 ###

# Texte à afficher par défaut sur ce choix
default_text_choices = ("Choix 1", "Choix 2", "Choix 3", "Choix 4")

# Curseur par défaut du choix
default_cursor_choices = (default_cursor_page, ) * 4

# Arrière-plan par défaut du choix
default_background_choices = ("#ffffff", ) * 4

# Couleur par défaut de l'arrière-plan
# du choix 1 lorsque le curseur passe devant
default_activebackground_choices = ("yellow", ) * 4

# Couleur du texte par défaut du choix
default_foreground_choices = ("black", ) * 4

# Épaisseur par défaut du bouton de choix
default_borderwidth_choices = (None, ) * 4

# Relief par défaut du bouton de choix
default_relief_choices = ("groove", ) * 4 

# Marges externes par défaut en x et y des boutons
default_padx_choices = (default_padx, ) * 4
default_pady_choices = (default_pady, ) * 4

# Marges internes par défaut en x et y des boutons
default_ipadx_choices = (default_ipadx, ) * 4
default_ipady_choices = (default_ipady, ) * 4

# Police par défaut du bouton de choix
default_font_choices = (default_font, ) * 4

#############################################
# Personnalisation de la musique            #
#############################################

# Musique par défaut d'une page
default_sound = None#"default_sound.mp3"


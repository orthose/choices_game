#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

# ATTENTION: Ne pas modifier ce fichier pour la personnalisation
# Il s'agit du fichier à exécuter pour lancer le jeu
# Utilisez la commande <python3 choices_game.py>

from Graphic import *
from Page import *; from pages import *
from config import default_window_title

# Lance l'interface graphique du jeu
graphic = Graphic(default_window_title, first_page=Page.first_page)
graphic.mainloop()

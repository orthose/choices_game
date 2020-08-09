#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

from alias import *

# Dictionnaire des pages du jeu avec un format
# précis à respecter mais qui restent modifiables
# Les alias ne peuvent figurer que dans text
pages = dict()

# Page d'accueil obligatoire
pages["accueil"] = {
    "image": "accueil.jpg",
    "background": "#3387c0",
    "text": "Bienvenue dans @game. La guerre a été déclarée par @enemy. @friend doit réagir au plus vite !",
    "choices": [["Commencer", "vaisseau"]]
}

# Page de choix du vaisseau
pages["vaisseau"] = {
    "image": "vaisseau.jpg",
    "background": "#3387c0",
    "text": "Veuillez choisir votre vaisseau spatial de combat...",
    "choices": [["Le Furtif, un vaisseau aussi silencieux que la brise !", "furtif"], 
                ["Le Destroyeur, un vaisseau qui fonce dans le tas !", "destroyeur"]]
}

# Dictionnaire des liens entre les pages
# Toutes les pages doivent apparaître une
# fois uniquement et être reliées à au moins
# une autre page
links = dict()

for page in pages.keys():
    links[page] = list()
    for choice in pages[page]["choices"]:
        links[page].append(choice[1])


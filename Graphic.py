#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

# ATTENTION: Ne pas modifier ce fichier pour la personnalisation
# Il s'agit du fichier gérant l'interface graphique

from tkinter import * # Bibliothèque graphique
# sudo apt-get install -y python-pil.imagetk
from PIL import Image, ImageTk # Bibliothèque de gestion des images
import tkinter.scrolledtext as st # Zone de texte avec barre de déplacement
# sudo apt-get install python3-pygame
from pygame import mixer # Bibliothèque de gestion de l'audio mp3
from config.alias import replace_alias_tag, replace_alias # Gestion des alias dans la zone de texte

# Pour l'utilisation de la bibliothèque Tkinter
# les docs utilisées sont principalement :
# http://tkinter.fdex.eu/index.html
# https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
class Graphic(Tk):
    """Gère la partie graphique du jeu
    et permet d'afficher une page.
    
    Ne pas modifier pour la personnalisation.
    """
    
    def __init__(self, title, first_page=None):
        """Initialise la fenêtre principale.
        :param title: Titre de la fenêtre
        :param first_page: Première page à s'afficher
        :type title: str
        :type first_page: Page
        """
        if first_page == None:
            raise ValueError("La première page n'a pas été instanciée !")
            
        # Appel au constructeur de Tk
        super().__init__()
        
        # Titre de la fenêtre principale
        self.title(title)
        
        # Par défaut on fixe la fenêtre en plein écran
        self.geometry("{L}x{H}+0+0".format(L=self.winfo_screenwidth(), H=self.winfo_screenheight()))
        # Empêche le redimensionnement de la page
        # https://www.it-swarm.dev/fr/python/comment-puis-je-empecher-le-redimensionnement-dune-fenetre-avec-tkinter/1045090982/
        #self.resizable(width=False, height=False)
        
        # Menu des actions supplémentaires
        self.menu_bar = Menu(self)
        self.sound_is_enabled = True
        self.menu_bar.add_command(label="Activer le son", command=self.enable_sound)
        self.menu_bar.add_command(label="Couper le son", command=self.disable_sound)
        self.menu_bar.add_command(label="Recommencer", command=lambda page=first_page: self.print_page(page))
        self.menu_bar.add_command(label="Quitter", command=self.quit)
        self.config(menu=self.menu_bar)
        
        # Zone de titre de la page
        self.label_title = Label(self)
        self.label_title.pack()
        
        # Zone d'affichage de l'image
        self.canvas_image = Canvas(self)
        self.image = first_page.image
        # Lors du redimensionnement de la fenêtre l'image
        # doit également être redimensionnée
        self.canvas_image.bind('<Configure>', lambda e: self.__image(self.image))
        self.canvas_image.pack(pady=first_page.graphic_image.pady)
        
        # Zone de texte avec barre de défilement intégrée
        self.text_area = st.ScrolledText(self)
        # Lors du redimensionnement de la fenêtre le texte
        # doit également être redimensionné
        self.text_area.bind('<Configure>', lambda e: self.text_area.config(height=(self.window_height // 100)))
        self.text_area.pack(fill=X)
        
        # Boutons des différents choix (jusqu'à 4 choix)
        # Liste des boutons de choix pour plus de praticité
        self.choices_button = [Button(self), Button(self), Button(self), Button(self)]
        # Lors du redimensionnement de la fenêtre le texte
        # doit également être redimensionné dans les boutons
        # https://www.reddit.com/r/learnpython/comments/6dndqz/how_would_you_make_text_that_automatically_wraps/
        for choice in self.choices_button:
            choice.bind('<Configure>', lambda e: choice.config(wraplength = choice.winfo_width()))
            
        # Initialisation du lecteur de musique mp3
        self.sound = first_page.sound
        mixer.init()
            
        # Affichage de la première page (le point d'entrée)
        self.print_page(first_page)
    
    @property 
    def window_width(self):
        self.update()
        self._window_width = self.winfo_width()
        return self._window_width
    
    @property 
    def window_height(self):
        self.update()
        self._window_height = self.winfo_height()
        return self._window_height
        
    def print_page(self, page):
        """Affiche une page.
        :param page: Page à afficher
        :type page: Page
        """
        
        if page == None:
            raise ValueError("Impossible d'afficher une page non-instanciée !")
            
        # Lancement de la musique de la page
        self.sound = page.sound
        self.run_sound()
            
        # Appel des méthodes privées pour configurer le contenu
        # et la forme des widgets de la page
        
        # Couleur de l'arrière-plan de la page
        self.__page(**page.graphic_global.__dict__)
        # Titre de la page
        self.__title(page.title, **page.graphic_title.__dict__)
        # Affichage de l'image
        self.__image(page.image, **page.graphic_image.__dict__)
        # Texte de la page
        self.__text(page.text, **page.graphic_text.__dict__)
        # Boutons des choix
        self.__choices(page.choices, **page.graphic_choices.__dict__)
    
    def __page(self, **kwargs):
        """Configure la page de manière globale.
        """
        self.configure(cursor=kwargs["cursor"], bg=kwargs["background"])
    
    def __title(self, title, **kwargs):
        """Configure le titre de la page.
        """
        self.label_title.config(text=replace_alias(title), bg=kwargs["background"], fg=kwargs["foreground"], bd=kwargs["borderwidth"], relief=kwargs["relief"], padx=kwargs["padx"], pady=kwargs["pady"], font=kwargs["font"], justify=CENTER)
    
    def __image(self, image, **kwargs):
        """Configure l'image de la page.
        :param image: Nom de l'image dans le dossier pictures/
        :type image: str
        """

        # https://stackoverflow.com/questions/6582387/image-resize-under-photoimage
        
        # Modification de l'attribut pour le redimensionnement
        self.image = image
        
        # Pour supprimer le contenu du canvas
        self.canvas_image.delete("all")
        
        # Chargement du fichier dans le dossier pictures/
        self.loaded_image = Image.open("pictures/"+image)
        
        # Calcul du ratio entre la longueur et la hauteur
        ratio = max(self.loaded_image.size) / min(self.loaded_image.size)
        
        # La taille maximale du plus grand côté de l'image redimensionnée
        # est calculée dans max_size en fonction de la hauteur de la fenêtre principale
        # car tous les widgets sont assemblés sur la hauteur 
        new_size = tuple(); max_size = self.window_height // 2
        
        # Le plus grand côté de l'image est sur sa longueur
        if self.loaded_image.size[0] == max(self.loaded_image.size):
            new_size = (max_size, int(max_size // ratio))
        # Le plus grand côté de l'image est sur sa hauteur
        else:
            new_size = (int(max_size // ratio), max_size)
            
        # Instruction pour redimensionner
        self.loaded_image = self.loaded_image.resize(new_size, Image.ANTIALIAS)
        # Conversion au format PhotoImage pour être compatible avec le canvas
        self.converted_image = ImageTk.PhotoImage(self.loaded_image)
        
        # Création de la zone du canvas et ajout à la fenêtre principale
        self.canvas_image.config(width = new_size[0], height = new_size[1])
        self.canvas_image.create_image(0, 0, anchor=NW, image=self.converted_image)
        
        # Modification de la marge en y de l'image
        self.canvas_image.pack(pady=kwargs["pady"])
    
    def __text(self, text, **kwargs):
        """Configure la zone de texte de la page.
        :param text: Texte à afficher dans la zone
        :type text: str
        """
    
        # https://stackoverflow.com/questions/17657212/how-to-code-the-tkinter-scrolledtext-module/17658025
        # https://stackoverflow.com/questions/32577726/python-3-tkinter-how-to-word-wrap-text-in-tkinter-text
        
        # Pour autoriser les modifications
        self.text_area.configure(state="normal")
        # Suppression du contenu de l'aire de texte
        # https://stackoverflow.com/questions/27966626/how-to-clear-delete-the-contents-of-a-tkinter-text-widget
        self.text_area.delete(1.0, END)
        
        # Configuration de la zone de texte
        # wrap=WORD permet de découper le texte en mots
        self.text_area.config(bg=kwargs["background"], fg=kwargs["foreground"], bd=kwargs["borderwidth"], relief=kwargs["relief"], padx=kwargs["padx"], pady=kwargs["pady"], font=kwargs["font"], wrap=WORD)
        
        # Résolution des alias
        solve_alias = replace_alias_tag(text)
        text = solve_alias["string"]
      
        # Insertion du texte
        self.text_area.insert(INSERT, text)
        #self.text_area.tag_configure("center", justify=CENTER)
        #self.text_area.tag_add("center", 1.0, "end")
        
        # Suppression des tags
        for tag in self.text_area.tag_names(): self.text_area.tag_delete(tag) 
        # Création et configuration des tags
        for tag in solve_alias["tags"]:
            self.text_area.tag_add(tag[0], tag[1], tag[2])
            self.text_area.tag_config(tag[0], font=kwargs["tag_font"], background=kwargs["tag_background"], foreground=kwargs["tag_foreground"], overstrike=kwargs["tag_overstrike"], underline=kwargs["tag_underline"])
        
        # Force la zone en lecture seule
        self.text_area.configure(state="disabled")
        
    def __choices(self, choices_data, **kwargs):
        """Configure les boutons de choix de la page.
        :param choices_data: Ensemble de couples (message, target_page)
        :type choices_data: set
        """
        
        # Suppression visuelle de tous les boutons
        # https://www.it-swarm.dev/fr/python/comment-supprimer-les-widgets-tkinter-dune-fenetre/1069571513/
        for choice in self.choices_button: choice.pack_forget()
        
        # Affichage des boutons en fonction des données
        for index, choice in enumerate(choices_data):
            button_msg, target_page = choice
            # Résolution des alias
            button_msg = replace_alias(button_msg)
            self.choices_button[index].config(text=button_msg, cursor=kwargs["cursor"][index], bg=kwargs["background"][index], activebackground=kwargs["activebackground"][index], fg=kwargs["foreground"][index], bd=kwargs["borderwidth"][index], relief=kwargs["relief"][index], padx=kwargs["padx"][index], pady=kwargs["pady"][index], font=kwargs["font"][index], justify=LEFT, command=lambda page=target_page: self.print_page(page))
            self.choices_button[index].pack(fill=X, expand=True, padx=kwargs["padx"][index], pady=kwargs["pady"][index])
            
    def run_sound(self):
        """Lance la musique mp3 du fichier
        enregistré dans l'attribut self.sound.
        """
        if mixer.music.get_busy():
            mixer.music.fadeout(1000)
        if self.sound != None and self.sound_is_enabled:
            mixer.music.load("sounds/"+self.sound)
            mixer.music.play(loops=-1)
            
    def enable_sound(self):
        """Active la musique.
        """
        self.sound_is_enabled = True
        self.run_sound()
        
    def disable_sound(self):
        """Désactive la musique.
        """
        self.sound_is_enabled = False
        self.run_sound()


#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

from tkinter import *
from PIL import Image, ImageTk #sudo apt-get install -y python-pil.imagetk
import tkinter.scrolledtext as st
from Page import *
import config

# Pour l'utilisation de la bibliothèque Tkinter
# les docs utilisées sont principalement :
# http://tkinter.fdex.eu/index.html
# https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
class Graphic(Tk):
    """Gère la partie graphique du jeu
    et permet d'afficher une page.
    """
    
    def __init__(self, title=config.default_window_title):
        """Initialise la fenêtre principale.
        :param title: Titre de la fenêtre
        :type title: str
        """
        
        # Appel au constructeur de Tk
        super().__init__()
        
        # Par défaut on fixe la fenêtre en plein écran
        self.geometry("{L}x{H}+0+0".format(L=self.winfo_screenwidth(), H=self.winfo_screenheight()))
        # Empêche le redimensionnement de la page
        # https://www.it-swarm.dev/fr/python/comment-puis-je-empecher-le-redimensionnement-dune-fenetre-avec-tkinter/1045090982/
        #self.resizable(width=False, height=False)
        
        # Zone de titre de la page
        self.label_title = Label(self)
        self.label_title.pack()
        
        # Zone d'affichage de l'image
        self.canvas_image = Canvas(self)
        self.image = config.default_image
        # Lors du redimensionnement de la fenêtre l'image doit
        # également être redimensionnée
        self.canvas_image.bind('<Configure>', lambda e: self.__image(self.image))
        self.canvas_image.pack()
        """
        # Zone de texte avec barre de défilement intégrée
        self.text_area = st.ScrolledText(self, height=(self.winfo_height() // 100), font = ("Times New Roman", 15), wrap=WORD)
        
        # Boutons des différents choix (jusqu'à 4 choix)
        self.choice1 = Button(self, text = "Choix 1", justify=LEFT)
        self.choice2 = Button(self, text = "Choix 2")
        self.choice3 = Button(self, text = "Choix 3")
        self.choice4 = Button(self, text = "Choix 4")"""
        self.configure_initial_window()
    
    def configure_initial_window(self):
        """Configure la fenêtre et ses widgets
        lors de l'initialisation.
        """
        
        # Couleur de l'arrière-plan de la page
        self.__page()
        
        # Titre de la page 
        self.__title()
        
        
        
        """
        # Champ pour l'image
        # https://stackoverflow.com/questions/6582387/image-resize-under-photoimage
        
        # Chargement du fichier dans le dossier pictures/
        self.image = Image.open("pictures/"+config.default_image)
        # Calcul du ratio entre la longueur et la hauteur
        ratio = max(self.image.size) / min(self.image.size)
        # La taille maximale du plus grand côté de l'image redimensionnée
        # est calculée dans max_size en fonction de la hauteur de la fenêtre principale
        # car tous les widgets sont assemblés sur la hauteur 
        new_size = tuple(); max_size = self.winfo_height() // 2
        # Le plus grand côté de l'image est sur sa longueur
        if self.image.size[0] == max(self.image.size):
            new_size = (max_size, int(max_size // ratio))
        # Le plus grand côté de l'image est sur sa hauteur
        else:
            new_size = (int(max_size // ratio), max_size)
        # Instruction pour redimensionner
        self.image = self.image.resize(new_size, Image.ANTIALIAS)
        # Conversion au format PhotoImage pour être compatible avec le canvas
        self.image = ImageTk.PhotoImage(self.image)
        # Création de la zone du canvas et ajout à la fenêtre principale
        self.canvas_image = Canvas(self, width = new_size[0], height = new_size[1])
        self.canvas_image.create_image(0, 0, anchor=NW, image=self.image)
        #self.canvas_image.delete("all") # Pour supprimer le contenu du canvas
        self.canvas_image.pack()
        
        # https://stackoverflow.com/questions/17657212/how-to-code-the-tkinter-scrolledtext-module/17658025
        # https://stackoverflow.com/questions/32577726/python-3-tkinter-how-to-word-wrap-text-in-tkinter-text
        print(self.winfo_height() // 50)
        self.text_area = st.ScrolledText(self, height=(self.winfo_height() // 100), font = ("Times New Roman", 15), wrap=WORD)
        self.text_area.bind('<Configure>', lambda e: self.text_area.config(height=(self.winfo_height() // 100)))
        self.text_area.pack(fill=X, padx=10, pady=10)
        self.text_area.insert(INSERT, "Bonjour")
        #self.text_area.delete(1.0, END) https://stackoverflow.com/questions/27966626/how-to-clear-delete-the-contents-of-a-tkinter-text-widget
        self.text_area.insert(INSERT, "Vive Marjane et tout car elle est sympa cette fille je te jure oui vraiment!")
        #self.text_area.tag_configure("center", justify=CENTER)
        #self.text_area.tag_add("center", 1.0, "end")
  
        # Making the text read only 
        self.text_area.configure(state ='disabled') 
        
        # https://www.reddit.com/r/learnpython/comments/6dndqz/how_would_you_make_text_that_automatically_wraps/
        self.choice1 = Button(self, text = "Choix 1 blab blab vive la vie vive les betteraves etc enfin voilà tu comprends quoi fin j'espère", justify=LEFT)
        self.choice1.bind('<Configure>', lambda e: self.choice1.config(wraplength = self.choice1.winfo_width()))
        self.choice1.pack(fill=X, expand=True)
        self.choice1.config(wraplength = self.choice1.winfo_width())
        self.choice2 = Button(self, text = "Choix 2Choix 1 blab blab vive la vie vive les betteraves etc enfin voilà tu comprends quoi fin j'espère")
        self.choice2.pack(fill=X, expand=True)
        self.choice3 = Button(self, text = "Choix 3")
        self.choice3.pack(fill=X, expand=True)
        self.choice4 = Button(self, text = "Choix 4")
        self.choice4.pack(fill=X, expand=True)
        #self.choice4.pack_forget() https://www.it-swarm.dev/fr/python/comment-supprimer-les-widgets-tkinter-dune-fenetre/1069571513/
        
        #TODO: Structurer configure_initial_window en plusieurs méthodes privées
        # voir ci-dessous
        
        #TODO: Finir de relier graphics et config
        
        # Mise à jour des paramètres de la fenêtre
        self.update()"""
    
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
        pass
    
    def __page(self, title=config.default_window_title, background=config.default_background_page):
        """Configure la page.
        """
        # Titre de la fenêtre principale
        self.title(title)
        # Couleur d'arrière-plan de la page
        self.configure(bg=background)
    
    def __title(self, title=config.default_page_title, background=config.default_background_title, foreground=config.default_foreground_title, borderwidth=config.default_borderwidth_title, relief=config.default_relief_title, font=config.default_font_title):
        """Configure le titre de la page.
        """
        self.label_title.config(text=title, bg=background, fg=foreground, bd=borderwidth, relief=relief, font=font, justify=CENTER)
    
    def __image(self, image):
        """Configure l'image de la page.
        """

        # Champ pour l'image
        # https://stackoverflow.com/questions/6582387/image-resize-under-photoimage
        
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
        self.loaded_image = ImageTk.PhotoImage(self.loaded_image)
        
        # Création de la zone du canvas et ajout à la fenêtre principale
        self.canvas_image.config(width = new_size[0], height = new_size[1])
        self.canvas_image.create_image(0, 0, anchor=NW, image=self.loaded_image)
    
    def __text(self, text):
        pass
    """
    def __title(self, title=config.default_page_title, background=config.default_background_title, activebackground=config.default_activebackground_title, foreground=config.default_foreground_title, borderwidth=config.default_borderwidth_title, relief=config.default_relief_title, font=config.default_font_title)"""
    def __choices(self, choices):
        pass
    

#champ_label = Label(window, text="Ceci est un test !", bg="#ff0000", padx=50, pady=3)
#champ_label.pack()

#Canvas(window, width=250, height=100).pack(side=TOP, padx=5, pady=5)
#Button(window, text = "Beaucoup de texte énormément de texte à la folie vraiment beaucoup", relief = GROOVE).pack( padx=5, pady=5)


graphic = Graphic()
graphic.mainloop()


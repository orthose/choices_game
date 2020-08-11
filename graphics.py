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
        super().__init__()
        self.title(title)
        self.configure_initial_window()
    
    def configure_initial_window(self):
        """Configure la fenêtre et ses widgets
        lors de l'initialisation.
        """
        # Taille totale de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Taille de la fenêtre
        self.window_width = screen_width
        self.window_height = screen_height
        # Par défaut on fixe la fenêtre en plein écran
        # On diminue un peu la hauteur pour parer à l'éventualité d'une barre de menu
        # sur le bureau de l'utilisateur
        self.geometry("{L}x{H}+0+0".format(L=self.window_width, H=self.window_height - 100))
        # Empêche le redimensionnement de la page
        # https://www.it-swarm.dev/fr/python/comment-puis-je-empecher-le-redimensionnement-dune-fenetre-avec-tkinter/1045090982/
        self.resizable(width=False, height=False)
        
        # Couleur de l'arrière-plan de la page
        self.configure(bg=config.default_page_background)
        
        # Titre de la page 
        self.label_title = Label(self, text=config.default_page_title, font=config.default_title_font, bg=config.default_title_background, justify = CENTER)
        self.label_title.pack()
        
        # Champ pour l'image
        # https://stackoverflow.com/questions/6582387/image-resize-under-photoimage
        
        # Chargement du fichier dans le dossier pictures/
        self.image = Image.open("pictures/"+config.default_image)
        # Calcul du ratio entre la longueur et la hauteur
        ratio = max(self.image.size) / min(self.image.size)
        # La taille maximale du plus grand côté de l'image redimensionnée
        # est calculée dans max_size en fonction de la hauteur de la fenêtre principale
        # car tous les widgets sont assemblés sur la hauteur 
        new_size = tuple(); max_size = self.window_height // 2
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
        self.text_area = st.ScrolledText(self, width = 30, height = 8, font = ("Times New Roman", 15)) 
        self.text_area.pack(fill=X, padx=10, pady=10)
        self.text_area.insert(INSERT, "Bonjour")
        #self.text_area.delete(1.0, END) https://stackoverflow.com/questions/27966626/how-to-clear-delete-the-contents-of-a-tkinter-text-widget
        self.text_area.insert(INSERT, "Vive Marjane et tout car elle est sympa cette fille je te jure oui vraiment!")
        #self.text_area.tag_configure("center", justify=CENTER)
        #self.text_area.tag_add("center", 1.0, "end")
  
        # Making the text read only 
        self.text_area.configure(state ='disabled') 
        
        self.choice1 = Button(self, text = "Choix 1")
        self.choice1.pack(fill=X, expand=True)
        self.choice2 = Button(self, text = "Choix 2")
        self.choice2.pack(fill=X, expand=True)
        self.choice3 = Button(self, text = "Choix 3")
        self.choice3.pack(fill=X, expand=True)
        self.choice4 = Button(self, text = "Choix 4")
        self.choice4.pack(fill=X, expand=True)
        #self.choice4.pack_forget() https://www.it-swarm.dev/fr/python/comment-supprimer-les-widgets-tkinter-dune-fenetre/1069571513/
        
        #TODO: Créer une méthode qui effectue les sauts de ligne automatiquement en fonction
        # taille widget et adapte police du texte pour les boutons !
        
        #TODO: Structurer configure_initial_window en plusieurs méthodes privées
        # voir ci-dessous
        
        #TODO: Finir de relier graphics et config
        
        # Mise à jour des paramètres de la fenêtre
        self.update()
        
    def print_page(self, page):
        """Affiche une page.
        :param page: Page à afficher
        :type page: Page
        """
        pass
    
    def __background(self, background):
        """Change la couleur d'arrière-plan
        de la fenêtre principale.
        """
        self.configure(bg=background)
    
    def __title(self, title):
        pass
    
    def __image(self, image):
        pass
    
    def __text(self, text):
        pass
    
    def __choices(self, choices):
        pass
    

#champ_label = Label(window, text="Ceci est un test !", bg="#ff0000", padx=50, pady=3)
#champ_label.pack()

#Canvas(window, width=250, height=100).pack(side=TOP, padx=5, pady=5)
#Button(window, text = "Beaucoup de texte énormément de texte à la folie vraiment beaucoup", relief = GROOVE).pack( padx=5, pady=5)


graphic = Graphic()
graphic.mainloop()


#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

# ATTENTION: Ne pas modifier ce fichier pour la personnalisation

from config.alias import replace_alias # Utilisé pour des tests
import config.config as config # Fichier de configuration graphique

class Page:
    """Données stockées dans une page du jeu.
    L'intérêt est de vérifier la validité des données.
    Cette classe ne doit pas être modifiée pour la personnalisation.
    
    Pour modifier le rendu graphique des éléments de la page
    vous pouvez modifier la valeur des attributs suivants:
    
    Page::graphic_global -> Rendu graphique global de la page
    Page::graphic_title -> Rendu graphique du titre de la page
    Page::graphic_text -> Rendu graphique de la zone de texte
    Page::graphic_choices -> Rendu graphique des boutons de choix
    
    Pour connaître les sous-attributs de chacun de ces attributs
    voir la classe GraphicalParameters.
    """
    
    # Première page point d'entrée du jeu
    # À modifier dans pages.py sous peine
    # d'erreur au démarrage du jeu
    first_page = None
    
    # Dictionnaire de toutes les pages de données
    # Inutile dans un fonctionnement avec un unique
    # point d'entrée
    #all_pages = dict()
    
    # Dictionnaire des liens entre les pages
    # Toutes les pages doivent apparaître une
    # fois uniquement et être reliées à au moins
    # une autre page
    links = dict()
    
    def __init__(self, title=config.default_page_title):
        """Tous les attributs sont privés
        car on veut que leur modification
        soit encadrée.
        
        :param title: Titre de la page, attention une fois
         choisi il n'est plus modifiable.
        :type title: str
        """
        if type(title) != str:
            raise TypeError("Page::title doit être de type str")
        if title == "":
            raise ValueError("Page::title ne doit pas être vide")
        if title != replace_alias(title):
            raise ValueError("Page::title ne doit pas comporter d'alias")
            
        # Données du contenu général
        self.__title = title
        self.__image = config.default_image
        self.__text = config.default_text
        self.__choices = set()
        self.__sound = config.default_sound
        
        # Données graphiques classées par section
        # Données graphiques globales
        self.graphic_global = GraphicalParameters(GraphicalParameters.GLOBAL)
        
        # Données graphiques du titre de la page
        self.graphic_title = GraphicalParameters(GraphicalParameters.TITLE)
        
        # Données graphiques de l'image de la page
        self.graphic_image = GraphicalParameters(GraphicalParameters.IMAGE)
        
        # Données graphiques du texte de la page
        self.graphic_text = GraphicalParameters(GraphicalParameters.TEXT)
        
        # Données graphiques des boutons de choix de la page
        self.graphic_choices = GraphicalParameters(GraphicalParameters.CHOICES)
        
        #Page.all_pages[title] = self
        Page.links[self] = list()
    
    @property
    def title(self):
        return self.__title
        
    @property
    def image(self):
        return self.__image
        
    @property
    def text(self):
        return self.__text
        
    @property
    def choices(self):
        return self.__choices
        
    @property
    def sound(self):
        return self.__sound
        
    @image.setter
    def image(self, image):
        Page.check_file(image, "image")
        self.__image = image
        
    @text.setter
    def text(self, text):
        if type(text) != str:
            raise TypeError("Page::text doit être de type str et peut comporter des alias")
        self.__text = text
        
    @sound.setter
    def sound(self, sound):
        Page.check_file(sound, "sound")
        self.__sound = sound
    
    @staticmethod   
    def check_file(file_name, param):
        if type(file_name) != str:
            raise TypeError("Page::"+param+" doit être de type str")
        if file_name != replace_alias(file_name):
            raise ValueError("Page::"+param+" ne doit pas contenir d'alias")
        
    def add_choice(self, button_msg, target_page):
        """Ajoute un choix à la page, limitée à 4 choix
        :param button_msg: Texte qui apparaîtra sur le bouton
        :param target_page: Page cible lorsqu'on clique sur le bouton
        :type button_msg: str
        :type target_page: Page
        """
        
        if len(self.choices) >= MaxChoicesException.MAX:
            raise MaxChoicesException()  
        if type(button_msg) != str or type(target_page) != Page:
            raise TypeError("button_msg doit être de type str et target_page de type Page")
        # Décommenter pour empêcher l'utilisation d'alias dans les boutons
        #if button_msg != replace_alias(button_msg):
        #    raise ValueError("button_msg ne doit pas comporter d'alias")
        # On peut vouloir avoir un faux choix qui ramène sur la même page
        # Ici, on laisse cette souplesse mais on peut décommenter si l'on
        # souhaite un comportement plus restrictif
        #if target_page == self:
        #    raise ValueError("target_page ne doit pas pointer vers la page courante")
        if target_page == None:
            raise ValueError("target_page doit être instanciée")
        if button_msg == "":
            button_msg = config.default_text_choice[len(self.choices)]
            
        choice = (button_msg, target_page)
        self.__choices.add(choice)     
        Page.links[self].append(target_page)
    
    @staticmethod
    def check_choices():
        """Vérifie que toutes les pages pointent au moins vers
        une page qui n'est pas elle-même.
        
        Renvoie une erreur si une page invalide est détectée.
        """
        for page in Page.links.keys():
            if len(page.choices) == 0 or (len(page.choices) == 1 and list(page.choices)[0][1] == page):
                raise TargetPagesException(page)
        
class GraphicalParameters:
    """Permet de gérer les données des paramètres graphiques
    de chaque widget. La validité des données est essentiellement
    vérifiée par tkinter par la suite.
    
    Vous pouvez modifier la valeur des attributs suivants
    en fonction du widget concerné:
    
    widget == GLOBAL
        cursor; background
        
    widget == TITLE
        background; foreground; borderwidth; relief; padx; pady; font
        
    widget == IMAGE
        pady
        
    widget == TEXT
        background; foreground; borderwidth; relief; padx; pady; font; 
        tag_font; tag_background; tag_foreground; tag_overstrike; tag_underline
    
    ATTENTION pour le widget CHOICES, les paramètres
    sont des tuples de 1 à 4 valeurs !
      
    widget == CHOICES
        cursor; background; activebackground; foreground; borderwidth; relief;
        padx; pady; font
    """
    
    # Constantes pour spécifier le type d'objet graphique
    GLOBAL = 0; TITLE = 1; IMAGE = 2; TEXT = 3; CHOICES = 4
    
    def __init__(self, widget):
        """Tous les arguments possibles sont
        initialisés à None. Il faut ensuite
        donner une valeur manuellement pour les
        arguments que l'on veut utiliser.
        :param widget: Constante à choisir ci-dessus
        :type widget: int
        """
        
        self.__widget = widget
        
        if self.__widget == GraphicalParameters.GLOBAL:
            self.cursor = config.default_cursor_page
            self.background = config.default_background_page
        
        elif self.__widget == GraphicalParameters.TITLE:
            self.background = config.default_background_title
            self.foreground = config.default_foreground_title
            self.borderwidth = config.default_borderwidth_title
            self.relief = config.default_relief_title
            self.padx = config.default_padx_title
            self.pady = config.default_pady_title
            self.font = config.default_font_title
            
        elif self.__widget == GraphicalParameters.IMAGE:
            self.pady = config.default_pady_image
        
        elif self.__widget == GraphicalParameters.TEXT:
            self.background = config.default_background_text
            self.foreground = config.default_foreground_text
            self.borderwidth = config.default_borderwidth_text
            self.relief = config.default_relief_text
            self.padx = config.default_padx_text
            self.pady = config.default_pady_text
            self.font = config.default_font_text
            self.tag_font = config.default_tag_font_text
            self.tag_background = config.default_tag_background_text
            self.tag_foreground = config.default_tag_foreground_text
            self.tag_overstrike = config.default_tag_overstrike_text
            self.tag_underline = config.default_tag_underline_text
        
        elif self.__widget == GraphicalParameters.CHOICES:
            # Attention ici les paramètres sont des tuples
            self.cursor = config.default_cursor_choices
            self.background = config.default_background_choices
            self.activebackground = config.default_activebackground_choices
            self.foreground = config.default_foreground_choices
            self.borderwidth = config.default_borderwidth_choices
            self.relief = config.default_relief_choices
            self.padx = config.default_padx_choices
            self.pady = config.default_pady_choices
            self.font = config.default_font_choices
        
        else:
            raise ValueError("Constante de widget invalide")
            
    def __setattr__(self, name, value):
        """Redéfinition de __setattr__ pour forcer
        le type des paramètres graphiques des boutons de choix
        à être des tuples.
        """
        if name != "_GraphicalParameters__widget" and self.__widget == GraphicalParameters.CHOICES:
            if type(value) != tuple:
                raise TypeError("Les paramètres graphiques des boutons de choix doivent être des tuples")
            elif len(value) >  MaxChoicesException.MAX:
                raise MaxChoicesException()
        super().__setattr__(name, value)
        

class MaxChoicesException(Exception):
    """Si l'ajout d'un choix dans une page fait dépasser
    le nombre de 4 choix, une exception est levée.
    """
    
    MAX = 4 # 4 choix au maximum
    
    def __init__(self):
        self.message = "Nombre maximum de {} choix dépassé".format(MaxChoicesException.MAX)
        
    def __str__(self):
        return self.message
        
class TargetPagesException(Exception):
    """Si une page ne pointe vers aucune autre ou juste elle-même,
    l'erreur sera déclenchée.
    """
    
    def __init__(self, page):
        self.message = "La page " + page.title + " ne pointe pas vers une autre page" 
        
    def __str__(self):
        return self.message
    

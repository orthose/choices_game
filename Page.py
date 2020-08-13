#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

from re import match
from alias import replace_alias
import config

class Page:
    """Données stockées dans une page du jeu.
    L'intérêt est de vérifier la validité des données.
    Cette classe ne doit pas être modifiée.
    
    Toutes les pages sont accessibles via l'attribut
    de classe Page.all_pages["une_page"].
    """
    
    # Première page point d'entrée du jeu
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
        
        # Données graphiques classées par section
        # Données graphiques globales
        self.graphic_global = GraphicalParameters()
        self.graphic_global["background"] = config.default_background_page
        self.graphic_global["cursor"] = config.default_cursor_page
        self.graphic_global["padx"] = config.default_padx
        self.graphic_global["pady"] = config.default_pady
        self.graphic_global["font"] = config.default_font
        
        # Données graphiques du titre de la page
        self.graphic_title = GraphicalParameters()
        self.graphic_title["background"] = default_background_title
        self.graphic_title["foreground"] = default_foreground_title
        self.graphic_title["borderwidth"] = default_borderwidth_title
        self.graphic_title["relief"] = default_relief_title
        self.graphic_title["font"] = default_font_title
        
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
        
    @image.setter
    def image(self, image):
        if type(image) != str:
            raise TypeError("Page::image doit être de type str")
        if image != replace_alias(image):
            raise ValueError("Page::image ne doit pas contenir d'alias")
        self.__image = image
        
    @text.setter
    def text(self, text):
        if type(text) != str:
            raise TypeError("Page::text doit être de type str et peut comporter des alias")
        self.__text = text
        
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
        if button_msg != replace_alias(button_msg):
            raise ValueError("button_msg ne doit pas comporter d'alias")
        if target_page == self:
            raise ValueError("target_page ne doit pas pointer vers la page courante")
        if button_msg == "":
            button_msg = config.default_text_choice[len(self.choices)]
            
        choice = (button_msg, target_page)      
        self.__choices.add(choice)     
        Page.links[self].append(choice[1])
        
        
class GraphicalParameters:
    """Permet de gérer les données des paramètres graphiques
    de chaque widget et de vérifier la validité du format et type
    de ces paramètres.
    """
    
    # Constantes pour spécifier le type d'objet graphique
    GLOBAL = 0; TITLE = 1; TEXT = 2; CHOICES = 3
    
    def __init__(self, widget):
        """Tous les arguments possibles sont
        initialisés à None. Il faut ensuite
        donner une valeur manuellement pour les
        arguments que l'on veut utiliser.
        :param widget: Constante à choisir ci-dessus
        :type widget: int
        """
        
        self.__widget = widget
        
        if widget == GraphicalParameters.GLOBAL:
            self.__cursor = config.default_cursor_page
            self.__background = config.default_background_page
        
        elif widget == GraphicalParameters.TITLE:
            self.__background = config.default_background_title
            self.__foreground = config.default_foreground_title
            self.__borderwidth = config.default_borderwidth_title
            self.__relief = config.default_relief_title
            self.__padx = config.default_padx_title
            self.__pady = config.default_pady_title
            self.__font = config.default_font_title
        
        elif widget == GraphicalParameters.TEXT:
            self.__background = config.default_background_text
            self.__foreground = config.default_foreground_text
            self.__borderwidth = config.default_borderwidth_text
            self.__relief = config.default_relief_text
            self.__padx = config.default_padx_text
            self.__pady = config.default_pady_text
            self.__font = config.default_font_text
        
        elif widget == GraphicalParameters.CHOICES:
            # Attention ici les paramètres sont des tuples
            self.__cursor = config.default_cursor_choices
            self.__background = config.default_background_choices
            self.__activebackground = config.default_activebackground_choices
            self.__foreground = config.default_foreground_choices
            self.__borderwidth = config.default_borderwidth_choices
            self.__relief = config.default_relief_choices
            self.__padx = config.default_padx_choices
            self.__pady = config.default_pady_choices
            self.__font = config.default_font_choices
        
        else
            raise ValueError("Constante de widget invalide")
        
    @property
    def cursor(self):
        return self._cursor
        
    @cursor.setter
    def cursor(self, cursor):
        # https://www.tcl.tk/man/tcl8.6/TkCmd/cursors.htm
        all_cursors = list_values('cursors.txt')
        if not cursor in all_cursors
            raise ValueError("Nom de curseur de GraphicalParameters::cursor invalide")
        else
            self._cursor = cursor
            
    @property
    def background(self):
        return self.__background
        
    @background.setter
    def background(self, background):
        if check_color(background, "background"):
            self.__background = background
        
    @property
    def activebackground(self):
        return self.__activebackground
        
    @activebackground.setter
    def activebackground(self, activebackground):
        if check_color(activebackground, "activebackground"):
            self.__activebackground = activebackground
        
    @property
    def foreground(self):
        return self.__foreground
        
    @foreground.setter
    def foreground(self, foreground):
        if check_color(foreground, "foreground"):
            self.__foreground = foreground
        
    @property
    def borderwidth(self):
        return self.__borderwidth
        
    @borderwidth.setter
    def borderwidth(self, borderwidth):
        
        if check_int(borderwidth, "borderwidth")
            self.__borderwidth = borderwidth
        
    @property
    def relief(self):
        return self.__relief
       
    @relief.setter
    def relief(self, relief):
        if type(relief) != str:
            raise TypeError("GraphicalParameters::relief doit être de type str")
        all_reliefs = list_values('reliefs.txt')
        all_reliefs += [r.lower() for r in all_reliefs]
        if not relief in all_reliefs:
            raise ValueError("Valeur de GraphicalParameters::relief invalide")
        self.__relief = relief
        
    @property
    def padx(self):
        return self.__padx
        
    @property
    def pady(self):
        return self.__pady
        
    @padx.setter
    def padx(self, padx):
        if check_int(padx, "padx"):
            self.__padx = padx
            
    @pady.setter
        if check_int(padx, "pady"):
            self.__padx = padx
            
    @property
    def font(self):
    
            
        
    def check_color(color, param_name):
        """Vérifie que la couleur est valide.
        :param color: Couleur à vérifier
        :param param_name: Nom du paramètre à afficher en cas d'erreur
        :type color: str
        :type param_name: str
        :return: True si valide, False sinon
        :rtype: bool
        """
        if type(color) != str:
            raise TypeError("GraphicalParameters::"+param_name+" doit être de type str")
            
        # http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        all_colors = list_values('colors.txt')
        
        if not ((color in all_colors) or  match("#([0-9]|[a-f]){6}", color)):
            raise ValueError("Couleur de GraphicalParameters::"+param_name+" invalide")
        
        return True
        
    def check_int(integer, param_name):
        """Vérifie la validité d'un intier positif ou nul.
        :param integer: Valeur de l'entier
        :param param_name: Nom du paramètre à afficher en cas d'erreur
        :type integer: int
        :type param_name: str
        :return: True si valide, False sinon
        :rtype: bool
        """
        if type(integer) != int:
            raise TypeError("GraphicalParameters::"+param_name+" doit être de type int")
        if integer < 0:
            raise ValueError("GraphicalParameters::"+param_name+" doit être positif ou nul")
        return True
        
    def list_values(file_name):
        """Met dans une liste toutes les valeurs d'un fichier
        texte dont les valeurs sont séparées par des sauts de ligne.
        :param file_name: Nom du fichier source
        :type file_name: str
        """
        with open(file_name, 'r') as fichier:
            all_values = fichier.read()
        return all_values.split("\n")
        

class MaxChoicesException(Exception):
    """Si l'ajout d'un choix dans une page fait dépasser
    le nombre de 4 choix, une exception est levée.
    """
    
    MAX = 4 # 4 choix au maximum
    
    def __init__(self):
        self.message = "Nombre maximum de {} choix dépassé".format(MaxChoicesException.MAX)
        
    def __str__(self):
        return self.message

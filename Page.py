#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

from re import match
from alias import replace_alias

class Page:
    """Données stockées dans une page du jeu.
    L'intérêt est de vérifier la validité des données.
    Cette classe ne doit pas être modifiée.
    
    Toutes les pages sont accessibles via l'attribut
    de classe Page.all_pages["une_page"].
    """
    
    # Dictionnaire de toutes les pages de données
    all_pages = dict()
    
    # Dictionnaire des liens entre les pages
    # Toutes les pages doivent apparaître une
    # fois uniquement et être reliées à au moins
    # une autre page
    links = dict()
    
    def __init__(self, title):
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
        self.__title = title
        self.__image = str()
        self.__background = "#ffffff" # blanc par défaut
        self.__text = str()
        self.__choices = set()
        Page.all_pages[title] = self
        Page.links[title] = list()
    
    @property
    def title(self):
        return self.__title
        
    @property
    def image(self):
        return self.__image
        
    @property
    def background(self):
        return self.__background
        
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
        
    @background.setter
    def background(self, background):
        if type(background) != str:
            raise TypeError("Page::background doit être de type str")
        if not match("#([0-9]|[a-f]){6}", background):
            raise ValueError("Page::background doit être sous le format #ffffff")
        self.__background = background
        
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
            
        choice = (button_msg, target_page)      
        self.__choices.add(choice)     
        Page.links[self.title].append(choice[1]) 

class MaxChoicesException(Exception):
    """Si l'ajout d'un choix dans une page fait dépasser
    le nombre de 4 choix, une exception est levée.
    """
    
    MAX = 4 # 4 choix au maximum
    
    def __init__(self):
        self.message = "Nombre maximum de {} choix dépassé".format(MaxChoicesException.MAX)
        
    def __str__(self):
        return self.message

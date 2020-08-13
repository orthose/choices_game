#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

# Dictionnaire des alias permettant de personnaliser
# certaines variables importantes du texte
alias = {
    "@game": "La randonnée pédestre",
}

def replace_alias(string):
    """Remplace les alias par leur vraie valeur 
    dans la chaine de caractères en paramètre.
       
    :param string: chaîne de caractères à modifier
    :type string: str
    :return: Renvoie une nouvelle chaîne de
     caractères modifiée
    :rtype: str
    """
    for one_alias in alias.keys():
        if one_alias in string:
            string = string.replace(one_alias, alias[one_alias])
            
    return string

def replace_alias_tag(string):
    """Remplace les alias par leur vraie valeur 
    dans la chaine de caractères en paramètre,
    et calcule les tags pour mettre en valeur les
    alias dans l'interface graphique.
       
    :param string: chaîne de caractères à modifier
    :type string: str
    :return: Renvoie une nouvelle chaîne de
     caractères modifiée et les tags
    :rtype: dict
    """
    tags = list(); nb_tags = 0
    for one_alias in alias.keys():
        while one_alias in string:
            first_index = string.find(one_alias)
            last_index = first_index + len(alias[one_alias])
            tags.append(("alias"+str(nb_tags), float("1."+str(first_index)), float("1."+str(last_index))))
            string = string.replace(one_alias, alias[one_alias], 1)
            
            nb_tags += 1
            
    return {"string":string, "tags":tags}
    

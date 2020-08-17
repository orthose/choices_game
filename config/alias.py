#####################################################
#                                                   #
# Jeu à choix multiples édité sous licence GNU v3.0 #
# https://github.com/orthose/choices_game.git       #
# Auteur: Maxime Vincent                            #
#                                                   #
#####################################################

import re

# TODO: Ajouter et modifier les alias pour la personnalisation
# Les alias vous simplifieront la vie lorsque vous écrierez
# le texte d'une page (uniquement pour la zone de texte centrale)
# Veuillez respecter le format @alias pour que cela fonctionne

# Dictionnaire des alias permettant de personnaliser
# certaines variables importantes du texte
alias = {
    "@game": "Mon formidable jeu",
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
    # On trouve tous les alias
    all_alias = list()
    for one_alias in alias.keys():
        if one_alias in string:
            all_alias.append(one_alias)
            
    # On cherche toutes les occurences des alias dans le texte
    # avec l'indice de la première lettre de l'alias
    all_alias_order = list()
    for one_alias in all_alias:
        first_occurences = [a.start() for a in re.finditer(one_alias, string)]
        for fo in first_occurences:
            all_alias_order.append((fo, one_alias))
    
    # On cherche à obtenir simplement la liste des alias
    # dans le bon ordre par rapport au texte
    all_alias_order.sort()
    all_alias_order = [aao[1] for aao in all_alias_order]
    
    # Calcul et résolution des alias
    tags = list(); nb_tags = 0
    for one_alias in all_alias_order:
        first_index = string.find(one_alias)
        last_index = first_index + len(alias[one_alias])
        tags.append(("alias"+str(nb_tags), "1."+str(first_index), "1."+str(last_index)))
        string = string.replace(one_alias, alias[one_alias], 1)
            
        nb_tags += 1
            
    return {"string":string, "tags":tags}
    

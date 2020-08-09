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
    "@game": "La Guerre de Proxima",
    "@friend": "La Fédération terrestre",
    "@enemy": "Les Colons rebelles"
}

def replace_alias(string):
    """ 
    " Remplace les alias par leur vraie valeur
    " dans la chaine de caractères en paramètre
    " @param string: chaîne de caractères
    " @return: Renvoie une nouvelle chaîne de
    " caractères modifiée
    """
    for one_alias in alias.keys():
        if one_alias in string:
            string = string.replace(one_alias, alias[one_alias])
            
    return string

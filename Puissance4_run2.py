import random
from Puissance4_run1 import * 



#######################
# VOS FONCTIONS ICI #
#######################

def est_jouable(grille, colonne):
    j = colonne - 1
    for i in range(LIGNES - 1, -1, -1):
        if grille[i][j] == 0:
            return i
    return -1

def place_pion(grille, joueur, colonne):
    test = est_jouable(grille, colonne)
    if test == -1:
        return False
    grille[test][colonne - 1] = joueur
    return True

#********************************
# programme principal    
#********************************

    
            
    
    




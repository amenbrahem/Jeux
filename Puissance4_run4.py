import random
import re
from Puissance4_run3 import * 



#######################
# VOS FONCTIONS ICI #
#######################


def grille_pleine(grille):
    if 0 not in grille[0] :
        return True

def gagnant(grille):
    res_ligne = alignement_ligne(grille)
    res_cln=alignement_colonne(grille)
    res_desc=alignement_descendant(grille)
    res_asc=alignement_ascendant(grille)

    if res_ligne == 1 or res_cln==1 or res_desc==1 or res_asc==1:
        print("joueur 1 gagne")
        return 1
    elif res_ligne == 2 or res_cln==2 or res_desc==2 or res_asc==2:
        print("joueur 2 gagne")
        return 2
    return -1


#********************************
# programme principal    
#********************************
    
                
                
    
    




import random
from Puissance4_run2 import * 



#######################
# VOS FONCTIONS ICI #
#######################

def calc_pion(t,joueur,x):
    for i in range(x):
        if t[i]==t[i+1]==t[i+2]==t[i+3]==joueur:
            return True
    return False

def alignement_ligne(grille):
    for i in range(LIGNES-1,-1,-1):
        if(calc_pion(grille[i],1,4)):
            return 1
        elif(calc_pion(grille[i],2,4)):
            return 2
    
    return -1

def alignement_colonne(grille):

    for j in range(COLONNES):
        colonne = [grille[i][j] for i in range(LIGNES)]
        if(calc_pion(colonne,1,3)):
            return 1
        elif(calc_pion(colonne,2,3)):
            return 2
    return -1
def alignement_descendant(grille) :
    for i in range(3):
        for j in range(4):
            if grille[i][j]==grille[i+1][j+1]==grille[i+2][j+2]==grille[i+3][j+3]==1:
                return 1
            elif grille[i][j]==grille[i+1][j+1]==grille[i+2][j+2]==grille[i+3][j+3]==2:
                return 2
    return -1
def alignement_ascendant(grille):
    for i in range(LIGNES-1,2,-1):
        for j in range(0,4):
            if grille[i][j]==grille[i-1][j+1]==grille[i-2][j+2]==grille[i-3][j+3]==1:
                return 1
            elif grille[i][j]==grille[i-1][j+1]==grille[i-2][j+2]==grille[i-3][j+3]==2:
                return 2
    return -1


#********************************
# programme principal    
#********************************

                
                
    
    




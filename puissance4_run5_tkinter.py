# -*- coding: utf-8 -*-

from tkinter import *
from Puissance4_run4 import *

TAILLE_CASE = 100
MARGE = 10
LARGEUR = COLONNES * (TAILLE_CASE + MARGE) + MARGE
HAUTEUR = LIGNES * (TAILLE_CASE + MARGE) + MARGE

def clic(event):
    global joueur, grille, en_cours
    if not en_cours:
        return
    
    colonne = (event.x - MARGE) // (TAILLE_CASE + MARGE) + 1
    if est_jouable(grille, colonne):
        place_pion(grille, joueur, colonne)
        dessin_jeu(grille)
        winner = gagnant(grille)
        if winner ==1 or winner==2 :
            chaine.configure(text=f"Le joueur {winner} a gagné !")
            en_cours = False
            return
        joueur = 1 if joueur == 2 else 2
        chaine.configure(text=f"Au tour du joueur {joueur}")
        can.configure(background='yellow' if joueur == 1 else 'red')

def dessin_jeu(grille):
    for i in range(LIGNES):
        for j in range(COLONNES):
            can.create_rectangle(MARGE + j * (TAILLE_CASE + MARGE), MARGE + i * (TAILLE_CASE + MARGE),\
                                 MARGE + j * (TAILLE_CASE + MARGE)+TAILLE_CASE,\
                                 MARGE + i * (TAILLE_CASE + MARGE)+TAILLE_CASE,fill="blue")
            if grille[i][j] == 0:
                can.create_oval(MARGE + j * (TAILLE_CASE + MARGE)+5, MARGE + i * (TAILLE_CASE + MARGE )+5,\
                                MARGE + j * (TAILLE_CASE + MARGE )+TAILLE_CASE-5,\
                                MARGE + i * (TAILLE_CASE + MARGE )+TAILLE_CASE-5, fill ='white')         
            elif grille[i][j] == 1:
                can.create_oval(MARGE + j * (TAILLE_CASE + MARGE)+5, MARGE + i * (TAILLE_CASE + MARGE)+5,\
                                MARGE + j * (TAILLE_CASE + MARGE)+TAILLE_CASE-5,\
                                MARGE + i * (TAILLE_CASE+ MARGE )+TAILLE_CASE-5, fill ='red')                
            elif grille[i][j] == 2:
                can.create_oval(MARGE + j * (TAILLE_CASE + MARGE)+5, MARGE + i * (TAILLE_CASE + MARGE)+5,\
                                MARGE + j * (TAILLE_CASE+ MARGE)+TAILLE_CASE-5,\
                                MARGE + i * (TAILLE_CASE + MARGE)+TAILLE_CASE-5, fill ='yellow')

# Programme principal
fen = Tk()         
fen.title('Puissance 4')

can = Canvas(fen, width = LARGEUR, height = HAUTEUR, background='blue')
can.pack(side = LEFT)

bouton_quitter = Button(fen, text="Quitter", command=fen.destroy)
bouton_quitter.pack(side=BOTTOM)

chaine = Label(fen)
chaine.pack(side = RIGHT)

# Initialise le jeu
grille = genere_grille()
dessin_jeu(grille)
joueur = 1
chaine.configure(text= str(joueur)+ " joue")
en_cours = True

# Associe l'événement clic à la fonction clic
can.bind('<Button-1>', clic)

fen.mainloop()

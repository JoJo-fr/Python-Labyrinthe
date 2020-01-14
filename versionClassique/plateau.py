# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *
import random

# a retirer 
import os 
os.system("rm -rf __pycache__")

cases_fixes = {
    str(Carte(False,False,False,True)) : [ # '╠' 
        (0,2),
        (0,4),
        (2,2), 
    ], 
    str(Carte(False,True,False,False)) : [ # '╣'
        (6,2),
        (6,4),
        (4,4)
    ],
    str(Carte(True,False,False,False)) : [ # '╦'

        (2,0),
        (4,0),
        (4,2)
    ],
    str(Carte(False,False,True,True))  : [ # '╩'
        (2,6),
        (4,6),
        (2,4)
    ] 
}

les_coins = [
    # les posiotions des coins en x  y et la valeur 
    (0,0,Carte(True,False,False,True,0,[])),
    (0,6,Carte(True,True,False,False,0,[])),
    (6,6,Carte(False,True,True,False,0,[])),
    (6,0,Carte(True,False,True,True,0,[]))
]

def Plateau(nbJoueurs, nbTresors): #modifier la génération de joueur
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: 
        - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes ont été placée de manière aléatoire
        - la carte amovible qui n'a pas été placée sur le plateau
    """
    liste_carte_amovible = []
    le_plateau = Matrice(7,7,0)
    liste_carte_amovible.append(creerCartesAmovibles(1,33))

    # j'ajoute les coins
    compteur_joueur = 0
    for (x,y,val) in les_coins:
        if compteur_joueur < nbJoueurs:
            compteur_joueur += 1
            val["Pions"].append(compteur_joueur)
            setVal(le_plateau,x,y,val)          
        else:
            setVal(le_plateau,x,y,val)

    # j'ajoute les cases fixes
    for (carte_fixe,liste_pos) in cases_fixes.items() :
        for (x,y) in liste_pos:
            setVal(le_plateau,x,y,carte_fixe)
    afficheMatrice(le_plateau)

    for x in range(7):
        for y in range(7):
            if getVal(le_plateau,x,y) == 0:
                setVal(le_plateau,x,y,car)
    afficherMatrice(le_plateau)
Plateau(4,49)
def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésorsgetNbLigne
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: 
            tresorDebut: le numéro du premier trésor à créer
            nbTresors: le nombre total de trésor à créer
        résultat: 
            la liste mélangée aléatoirement des cartes amovibles créees
    """
    liste_carte_amovible = []
    liste_tresor == []

    if liste_carte_amovible == []: # premiére carte du jeux 
        carte = Carte(bool(random.randint(0,1)), # Nord
                                   bool(random.randint(0,1)), # Est
                                   bool(random.randint(0,1)), # Sud
                                   bool(random.randint(0,1)), # Ouest
                                   tresorDebut)
        liste_carte_amovible.append(carte)
    for elem in range(33): # carte restante
        while len(liste_carte_amovible) != nbTresors:
            tresor_aléatoire = random.randint(1,nbTresors)
            if tresor_aléatoire not in liste_tresor:
                 carte = Carte(bool(random.randint(0,1)), # Nord
                                       bool(random.randint(0,1)), # Est
                                       bool(random.randint(0,1)), # Sud
                                       bool(random.randint(0,1)), # Ouest
                                       tresor_aléatoire)
                 liste_carte_amovible.append(carte)
    return random.shuffle(liste_carte_amovible)
             

def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    carte_info = getVal(plateau,lig,col)
    if getVal(plateau,lig,col) == carte_info:
        return True
    return False

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    pass


def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    pass

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    pass

def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    pass

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    pass


def test():
    pass    
 
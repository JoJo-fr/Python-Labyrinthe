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

def Plateau(nbJoueurs, nbTresors): #modifier la génération de joueur
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
<<<<<<< Updated upstream
        - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes ont été placée de manière aléatoire
        - la carte amovible qui n'a pas été placée sur le plateau
    """
    pass

=======
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    plateau = Matrice(7,7) # on créer le plateau 
    ligne_plateau = getNbLignes(plateau) # récupére le nombre de ligne de plateau
    colonne_plateau = getNbColonnes(plateau) # récupére le nombre de colonne de plateau
    liste_tresor = []
    #liste_joueur = []
    
    for x in range(ligne_plateau):
        for y in range(colonne_plateau):
            tresor = random.randint(1,nbTresors) # génére de maniére aléatoire un numéro de trésor en tre 1 et nbTresor
            #joueur = random.randint(1,4) # génére de maniére aléatoire un numéro de pion
            #génére une carte aléatoire avec un nombre aléatoire aléatoire d'un trésor (1 à nbTresor)
            #génére un joueur aléatoire
            if tresor not in liste_tresor or liste_tresor == []:
                info_carte = Carte(bool(random.randint(0,1)), # Nord
                                   bool(random.randint(0,1)), # Est
                                   bool(random.randint(0,1)), # Sud
                                   bool(random.randint(0,1)), # Ouest
                                   tresor)
            setVal(plateau,x,y,info_carte)
            liste_tresor.append(tresor)
    print(plateau) 
    return plateau   
Plateau(4,46)
>>>>>>> Stashed changes

def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant aléatoirement nbTresor trésorsgetNbLigne
    
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    pass


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



def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
<<<<<<< Updated upstream

=======
    ligne_plateau = getNbLignes(plateau)
    colonne_plateau = getNColonnes(plateau)
    for x in ligne_plateau:
        for y in colonne_plateau:
            if getVal(plateau,x,y) == numJoueur:
                return (x,y)
    return None
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
    pass
=======
    setVal(plateau,lin,col,numJoueur)
>>>>>>> Stashed changes

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
 
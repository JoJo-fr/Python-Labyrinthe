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
import ast # convert string to dict

# a retirer 
"""
import os 
os.system("rm -rf __pycache__")
"""

def Plateau(nbJoueurs, nbTresors): #modifier la génération de joueur
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: 
        - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes ont été placée de manière aléatoire
        - la carte amovible qui n'a pas été placée sur le plateau
    """
    dictionaire_plateau = {}
    dictionaire_plateau["matrice"] = Matrice(7,7,0) # créer une matrice
    dictionaire_plateau["joueurs"] = [nbJoueurs] # injecter une clé et valeur nbjoueur

    liste_de_carte_amovible = creerCartesAmovibles(1,random.randint(1,45))
    random.shuffle(liste_de_carte_amovible)

    placement_carte(dictionaire_plateau,liste_de_carte_amovible) # injecter les carte fixe et amovible

def placement_carte(dictionaire_plateau,cartes):
    """
    cette fonction vas injecter les carte dans la matrice
    """
    index = -1

    # ajouter toutes les cartes fixe sur le plateau
    for x in range(7):
        for y in range(7):
            index += 1
            if x == 0 and y == 0:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,False,True,True,0,[])) # '╔'
            if x == 0 and y == 6:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,True,True,False,0,[])) # '╗'
            if x == 6 and y == 0:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(True,False,False,True,0,[])) # '╗'
            if x == 6 and y == 6:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(True,True,False,False,0,[])) # '╝'
            if x == 0 and y == 2:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,False,False,True,0,[])) # '╠'
            if x == 0 and y == 4:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,False,False,True,0,[])) # '╠'
            if x == 2 and y == 2:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,False,False,True,0,[])) # '╠'
            if x == 6 and y == 2:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,True,False,False,0,[])) # '╣'
            if x == 6 and y == 4:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,True,False,False,0,[])) # '╣'
            if x == 4 and y == 4:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,True,False,False,0,[])) # '╣'
            if x == 2 and y == 0:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(True,False,False,False,0,[])) # '╦'
            if x == 4 and y == 0:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(True,False,False,False,0,[])) # '╦'
            if x == 4 and y == 2:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(True,False,False,False,0,[])) # '╦'
            if x == 2 and y == 6:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,False,True,True,0,[])) # '╩'
            if x == 4 and y == 6:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,False,True,True,0,[])) # '╩'
            if x == 2 and y == 4:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,False,True,True,0,[])) # '╩'
    # ajouter les cartes amovible sur le plateau
    print(cartes)
    index = -1
    for x in range(7):
       for y in range(7):
           if getVal(dictionaire_plateau["matrice"],x,y) == 0 and index != len(cartes):
                index += 1
                setVal(dictionaire_plateau["matrice"],x,y,cartes[index])
    afficheMatrice(dictionaire_plateau["matrice"])
    return dictionaire_plateau

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
    liste_trésors = []
    index_trésor = -1
    
    #génére une liste de nombre, déplace aléatoirement les nombre dans la liste
    for nb in range(tresorDebut + nbTresors):
        liste_trésors.append(nb)
    random.shuffle(liste_trésors)

    for carte in range(16):
        index_trésor += 1
        if index_trésor < len(liste_trésors):
            liste_carte_amovible.append(Carte(False,False,True,False,liste_trésors[index_trésor],[])) # carte '╔'
        else:
            liste_carte_amovible.append(Carte(False,False,True,False,0,[]))
    for carte in range(6):
        index_trésor += 1
        if index_trésor < len(liste_trésors):
            liste_carte_amovible.append(Carte(False,False,True,False,liste_trésors[index_trésor],[])) # carte '╠'
        else:
            liste_carte_amovible.append(Carte(False,False,True,False,0,[]))
    for carte in range(12):
        index_trésor += 1
        if index_trésor < len(liste_trésors):
            liste_carte_amovible.append(Carte(True,False,True,False,liste_trésors[index_trésor],[])) # carte '║'
        else:
            liste_carte_amovible.append(Carte(False,False,True,False,0,[]))
    return liste_carte_amovible

Plateau(4,49)
def prendreTresorPlateau(plateau,lig,col,numTresor): # fonction à fixer
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
#prendreTresorPlateau(Plateau(4,4),0,0,1)

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    matrice = plateau["val"]
    for x in range(7):
        for y in range(7):
            if numJoueur in getVal(matrice["matrice"],x,y):
                return (x,y)
    return None

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    matrice = plateau["val"]
    index = -1
    for x in range(7):
        for y in range(7):
            if numJoueur in matrice["joueurs"]:
                for joueur in matrice["joueurs"]:
                    index += 1
                    if joueur == numJoueur:
                        del matrice["joueurs"][index]

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    index = -1
    matrice = plateau["val"]
    for x in range(7):
        for y in range(7):
            index += 1
            if (x,y) == (lin,col):
                matrice[index]["Pions"].append(numJoueur)
                return 0

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
    calque = Matrice(7, 7, -1)
    count = 0
    setVal(calque, ligD, colD, count)
    case_voisine = [(ligD, colD)]
    tester = [(ligD, colD)]
    while len(tester) != 0 and (ligA, colA) not in case_voisine:
        count += 1
        li = []
        for ligne, colone in tester:
            nouveau = [(ligne-1,colone), (ligne+1,colone), (ligne,colone-1), (ligne,colone+1)]
            nouveau = [(lig, col) for lig, col in nouveau if lig >= 0 and col >= 0 and lig <= getNbLignes(plateau) -1 and col <= getNbColonnes(plateau)-1 and (lig, col) not in case_voisine]
            for lig, col in nouveau:
                if lig == ligne-1 and passageNord(getVal(plateau, ligne, colone), getVal(plateau, lig, col)):
                    li.append((lig, col))
                    setVal(calque, lig, col, count)
                if lig == ligne+1 and passageSud(getVal(plateau, ligne, colone), getVal(plateau, lig, col)):
                    li.append((lig, col))
                    setVal(calque, lig, col, count)                    
                if col == colone-1 and passageOuest(getVal(plateau, ligne, colone), getVal(plateau, lig, col)):
                    li.append((lig, col))
                    setVal(calque, lig, col, count)
                if col == colone+1 and passageEst(getVal(plateau, ligne, colone), getVal(plateau, lig, col)):
                    li.append((lig, col))
                    setVal(calque, lig, col, count)
            case_voisine += li
        tester = li
    return (ligA, colA) in case_voisine

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
    index = -1
    matrice = plateau["val"]
    for x in range(7):
        for y in range(7):
            index += 1
            if matrice[index]["Trésor"] == numTresor:
                return (x,y)
    
 
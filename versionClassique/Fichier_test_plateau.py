# -*- coding: utf-8 -*-

from plateau import *

def test_matrice(labyrinthe):
    pass

matrice_carte = [
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":1,"Pion":[]}, #(0,0)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":2,"Pion":[]}, #(0,1)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":3,"Pion":[]}, #(0,2)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":4,"Pion":[]}, #(0,3)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":5,"Pion":[]}, #(0,4)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":6,"Pion":[]}, #(0,5)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":7,"Pion":[]}, #(0,6)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":8,"Pion":[]}, #(1,0)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":9,"Pion":[]}, #(1,1)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":10,"Pion":[]}, #(1,2) 10
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":11,"Pion":[]}, #(1,3) 
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":12,"Pion":[]}, #(1,4)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":13,"Pion":[]}, #(1,5)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":14,"Pion":[]}, #(1,6)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":15,"Pion":[]}, #(2,0)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":16,"Pion":[]}, #(2,1)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":17,"Pion":[]}, #(2,2)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":18,"Pion":[]}, #(2,3)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":19,"Pion":[]}, #(2,4)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":20,"Pion":[]}, #(2,5) 20
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":21,"Pion":[]}, #(2,6) 
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":22,"Pion":[]}, #(3,0)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":23,"Pion":[]}, #(3,1)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":24,"Pion":[]}, #(3,2)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(3,3)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(3,4)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(3,5)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(3,6)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(4,0)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(4,1) 30
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(4,2) 
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(4,3)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(4,4)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(4,5)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(4,6)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(5,0)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(5,1)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(5,2)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(5,3)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(5,4) 40
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(5,5) 
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(5,6)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(6,0)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(6,1)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(6,2)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(6,3)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(6,4)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(6,5)
    {"Nord": True, "Est": True,"Sud":True,"Ouest":False,"Tr?sor":0,"Pion":[]}, #(6,6) 49
    ]

"""

                info_carte = Carte(bool(random.randint(0,1)), # Nord
                                   bool(random.randint(0,1)), # Est
                                   bool(random.randint(0,1)), # Sud
                                   bool(random.randint(0,1)), # Ouest
                                   tresor)
"""

"""
    liste_carte_amovible = []
    le_plateau = Matrice(7,7,0) # créer une matrice 
    liste_carte_amovible.append(creerCartesAmovibles(1,nbTresors)) # ajout d'une liste de carte aleatoire

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
            setVal(le_plateau,x,y,ast.literal_eval(carte_fixe))

    # ajouter les cartes sur les case amovible
    for x in range(7):
        for y in range(7):
            if getVal(le_plateau,x,y) == 0:
                    # setVal(le_plateau,x,y,liste_carte_amovible[0][random.randint(1,32)])
                    setVal(le_plateau,x,y,liste_carte_amovible[0][random.randint(1,len(liste_carte_amovible))])
    #afficheMatrice(le_plateau)
    return le_plateau

"""

"""

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
"""

                   """
                   else: # si on dépasse le nombre de trésor 
                        carte = Carte(bool(random.randint(0,1)), # Nord
                                               bool(random.randint(0,1)), # Est
                                               bool(random.randint(0,1)), # Sud
                                               bool(random.randint(0,1)), # Ouest
                                               [])
                        liste_carte_amovible.append(carte)
                    """ 
                    """
                    liste_carte_amovible = []
    liste_tresor = []
    compteur = 0 # carte à générer 12:'║', '╔':20, '╠':18

    if liste_carte_amovible == []: # premiére carte du jeux 
        carte = Carte(False, # Nord
                        False, # Est
                        False, # Sud
                        True, # Ouest
                        tresorDebut) # '╠'

        liste_carte_amovible.append(carte)
    for elem in range(33): # carte restante
        while len(liste_carte_amovible) != nbTresors:
             tresor_aléatoire = random.randint(1,nbTresors)
             if tresor_aléatoire not in liste_tresor and liste_tresor != nbTresors:
                   liste_tresor.append(tresor_aléatoire)
                   if compteur <= 20:
                       compteur += 1
                       carte = Carte(False, # Nord
                                                False, # Est
                                                True, # Sud
                                                True, # Ouest
                                                tresor_aléatoire) # '╔'
                       liste_carte_amovible.append(carte)
                   elif compteur > 20 and compteur <= 32:
                        compteur += 1
                        carte = Carte(True, # Nord
                                                False, # Est
                                                True, # Sud
                                                False, # Ouest
                                                tresor_aléatoire) # '║'
                        liste_carte_amovible.append(carte)
                   elif compteur > 32 and compteur <= 50:
                        compteur += 1
                        carte = Carte(True, # Nord
                                                False, # Est
                                                True, # Sud
                                                True, # Ouest
                                                tresor_aléatoire) # '╠'
                        liste_carte_amovible.append(carte)
    return liste_carte_amovible
                    """
                    """

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


import os 
os.system("rm -rf __pycache__")


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

    liste_de_carte_amovible = creerCartesAmovibles(1,random.randint(1,45)) # génére une liste aléatoire de carte dans une liste
    random.shuffle(liste_de_carte_amovible) # mélange les carte de maniérre aléatoire

    placement_carte(dictionaire_plateau,liste_de_carte_amovible,nbJoueurs) # injecter les carte fixe et amovible
    return dictionaire_plateau

def placement_carte(dictionaire_plateau,cartes,nbJoueurs):
    """
    cette fonction vas injecter les carte dans la matrice
    """
    index = -1
    # ajouter toutes les cartes fixe sur le plateau
    for x in range(7):
        for y in range(7):
            index += 1
            if x == 0 and y == 0:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,False,True,True,0,[1])) # '╔'
            if x == 0 and y == 6:
                setVal(dictionaire_plateau["matrice"],x,y,Carte(False,True,True,False,0,[2])) # '╗'
            if x == 6 and y == 0:
                if nbJoueurs > 2: # si on à 3 joueurs alors placer le joueur 3
                    setVal(dictionaire_plateau["matrice"],x,y,Carte(True,False,False,True,0,[3])) # '╗'
                else:
                    setVal(dictionaire_plateau["matrice"],x,y,Carte(True,False,False,True,0,[])) # '╗'
            if x == 6 and y == 6:
                if nbJoueurs > 3: # si on à 4 joueurs alors placer le joueur 4
                    setVal(dictionaire_plateau["matrice"],x,y,Carte(True,True,False,False,0,[4])) # '╝'
                else:
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
    index = -1
    for x in range(7):
       for y in range(7):
           if getVal(dictionaire_plateau["matrice"],x,y) == 0 and index != len(cartes):
                index += 1
                setVal(dictionaire_plateau["matrice"],x,y,cartes[index])
    #afficheMatrice(dictionaire_plateau["matrice"])
    return dictionaire_plateau

def creerCartesAmovibles(tresorDebut,nbTresors): # fonction valider
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

#Plateau(4,49)
def prendreTresorPlateau(plateau,lig,col,numTresor): # prendre un trésor signifie le retirer de la carte ?
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
    labyrinthe = plateau["matrice"]
    carte = getVal(labyrinthe,lig,col)
    if getTresor(carte) == numTresor:
        return True
    return False
#prendreTresorPlateau(Plateau(4,4),0,0,1)

def getCoordonneesJoueur(plateau,numJoueur): # fonction valider
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    index = -1
    labyrinthe = plateau["matrice"]
    matrice = labyrinthe["val"]
    for x in range(7):
        for y in range(7):
            index += 1
            if possedePion(matrice[index],numJoueur) == True:
                return (x,y)
    return None
#getCoordonneesJoueur(Plateau(4,49),4)

def prendrePionPlateau(plateau,lin,col,numJoueur): # fonction valider
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    labyrinthe = plateau["matrice"]
    carte = getVal(labyrinthe,lin,col)
    prendrePion(carte,numJoueur)

#prendrePionPlateau(Plateau(4,5),0,6,2)

def poserPionPlateau(plateau,lin,col,numJoueur): # fonction valider
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    labyrinthe = plateau["matrice"]
    carte = getVal(labyrinthe,lin,col)
    poserPion(carte,numJoueur)


def marquageDirect(calque,plateau,val,marque):

    calque = Matrice(7,7)

    res=False
    nb_lignes = 7
    nb_Cols = 7
    for l in range(nb_lignes):
        for c in range(nb_Cols):
            if getVal(calque,l,c) == 0: # je ne suis pas marqué
                carte_actuelle = getVal(plateau["matrice"],l,c)
                if murEst(carte_actuelle) == True and murOuest(carte_actuelle) == True and murNord(carte_actuelle) == True and murSud(carte_actuelle) == True: 
                    if l > 0 and getVal(calque,l-1,c) == val: # mon voisin du haut est marqué
                        setVal(calque,l,c,marque)
                        res = True
                    elif l < nb_lignes-1 and getVal(calque,l+1,c) == val:# mon voisin du bas est marqué
                        setVal(calque,l,c,marque)
                        res = True
                    elif c > 0 and getVal(calque,l,c-1) == val: # mon voisin de gauche est marqué
                        setVal(calque,l,c,marque)
                        res = True
                    elif c < nb_Cols-1 and getVal(calque,l,c+1) == val:# mon voisin de droite est marqué
                        setVal(calque,l,c,marque)
                        res = True
    return res
    

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
    calque = Matrice(7,7,0)
    setVal(calque,ligD,colD,3)
    matrice=True
    while matrice==True:
        matrice=marquageDirect(calque,plateau["matrice"],3,3)
    if getVal(calque,ligA-1,colD-1)==3:
        return True
    return False
    

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

def getCoordonneesTresor(plateau,numTresor): # fonction valider
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    index = -1
    labyrinthe = plateau["matrice"]
    for x in range(7):
        for y in range(7):
            index += 1
            position = labyrinthe["val"][index]
            if getTresor(position) == numTresor:
                return (x,y)
    return None
#getCoordonneesTresor(Plateau(4,45),1)
    
 
                    """
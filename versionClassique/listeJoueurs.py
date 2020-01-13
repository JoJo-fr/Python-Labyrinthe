# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    liste_joueur = []
    for nom in nomsJoueurs:
        Joueur(nom)
    return liste_joueur

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs.append({"Nom": joueur,"Trésor":[],"Courant":0})

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs une liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueur_courant = joueurs.random.randint(1,len(joueurs)-1)
    joueurs[joueur_courant]["Courant"] = 1

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    liste_trésor_pris = []
    for joueur in joueurs:
        print (joueur["Trésor"])
        while len(joueur["Trésor"]) != nbTresorMax:
            trésor_nb = random .randint(1, nbTresors)
            if trésor_nb not in joueur["Trésor"]:
                joueur["Trésor"].append(trésor_nb)
    """
    liste_trésor_pris = []
    for J in range(len(joueurs)):
        trésor = random.randint(1, nbTresors)
        while len(joueurs[J]["Trésor"]) != nbTresorMax:
            if trésor not in liste_trésor_pris or liste_trésor_pris == []:
                joueurs[J]["Trésor"].append(trésor)
                liste_trésor_pris.append(trésor)
                trésor = random.randint(1, nbTresors)
            trésor = random.randint(1, nbTresors)
    """
def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    for joueur in range(len(joueurs)):
        if joueurs[joueur]["Courant"] == 0 and joueurs[joueur] < len(joueurs):
            joueurs[joueur]["Courant"] == 1
            joueurs[joueur+1]["Courant"] == 0
        else :
            joueurs[joueur]["Courant"] == 1
            joueurs[0]["Courant"] == 0

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    for joueur in joueurs:
        if joueur["Courant"] == 0:
            return joueur

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueur = getJoueurCourant(joueurs)
    del joueur["Trésor"][0]

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    print(joueurs[numJoueur])
    return getNbTresorsRestants(joueurs[numJoueur])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """ 
    for joueur in joueurs:
        if joueur["Courant"] == 0:
            return joueurs.index(joueur)+1

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    for joueur in joueurs:
        if joueur["Courant"] == 0:
            return joueur["Nom"]

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return joueurs[numJoueur+1]["Nom"]

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    joueur = joueurs[numJoueur]
    return prochainTresor(joueur)

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    for joueur in joueurs:
        if joueurs[joueur]["Courant"] == 1:
            return joueurs[joueur]["Trésor"][0]

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    if tresorCourant(joueurs) == []:
        return True
    return False
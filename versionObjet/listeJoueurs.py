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

class ListeJoueurs(object):

    def __init__(self,nomsJoueurs):
        """
        créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
        Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
        paramètre: nomsJoueurs une liste de chaines de caractères
        résultat: la liste des joueurs avec un joueur courant mis à 0
        """
        self.liste_joueur = []
        self.numjoueur=0
        cpt=1
        for joueurs in nomsJoueurs :
            player=Joueur(joueurs)
            player.numjoueur=cpt
            self.liste_joueur.append(player)
            cpt+=1
    

    def ajouterJoueur(self, joueur):
        """
        ajoute un nouveau joueur à la fin de la liste
        paramètres: joueurs un liste de joueurs
                    joueur le joueur à ajouter
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """ 
        self.liste_joueur.append(Joueur(joueur))

    def initAleatoireJoueurCourant(self):
        """
        tire au sort le joueur courant
        paramètre: joueurs une liste de joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        joueur_courant = random.randint(1,len(self.liste_joueur))
        joueur_choisie = self.liste_joueur[joueur_courant-1]
        self.liste_joueur.pop(0)
        self.liste_joueur.append(joueur_choisie)

    def distribuerTresors(self,nbTresors=24, nbTresorMax=0):
        """
        distribue de manière aléatoire des trésors entre les joueurs.
        paramètres: joueurs la liste des joueurs
                    nbTresors le nombre total de trésors à distribuer (on rappelle que les trésors sont des entiers de 1 à nbTresors)   
                    nbTresorsMax un entier fixant le nombre maximum de trésor 
                                qu'un joueur aura après la distribution
                                si ce paramètre vaut 0 on distribue le maximum
                                de trésor possible  
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        deja_attribue = []
        for x in range(len(self.liste_joueur)):

            while len(self.liste_joueur[x].tresors) != nbTresorMax:
                tresor_aleatoire = random.randint(1,nbTresors)
                if tresor_aleatoire not in deja_attribue :
                    deja_attribue.append(tresor_aleatoire)

                    if tresor_aleatoire not in self.liste_joueur[x].tresors:
                        self.liste_joueur[x].tresors.append(tresor_aleatoire)
            
        
    def changerJoueurCourant(self): 
        """
        passe au joueur suivant (change le joueur courant donc)
        paramètres: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        joueur_courant_changer = self.liste_joueur[0]
        self.liste_joueur.pop(0)
        self.liste_joueur.insert(len(self.liste_joueur),joueur_courant_changer)

    def getNbJoueurs(self):
        """
        retourne le nombre de joueurs participant à la partie
        paramètre: joueurs la liste des joueurs
        résultat: le nombre de joueurs de la partie
        """
        return len(self.liste_joueur)

    def getJoueurCourant(self):
        """
        retourne le joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le joueur courant
        """
        return self.liste_joueur[0]

    def joueurCourantTrouveTresor(self):
        """
        Met à jour le joueur courant lorsqu'il a trouvé un trésor
        c-à-d enlève le trésor de sa liste de trésors à trouver
        paramètre: joueurs la liste des joueurs
        cette fonction ne retourne rien mais modifie la liste des joueurs
        """
        self.liste_joueur[0].tresorTrouve()
 
    def nbTresorsRestantsJoueur(self,numJoueur):
        """
        retourne le nombre de trésors restant pour le joueur dont le numéro 
        est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur
        résultat: le nombre de trésors que joueur numJoueur doit encore trouver
        """
        return Joueur.getNbTresorsRestants(self.liste_joueur[numJoueur-1])

    def numJoueurCourant(self):
        """
        retourne le numéro du joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le numéro du joueur courant
        """ 
        #cpt=0
        #for joueur in self.liste_joueur:
        return self.liste_joueur[0].numjoueur

    def nomJoueurCourant(self): # à fixer
        """
        retourne le nom du joueur courant
        paramètre: joueurs la liste des joueurs
        résultat: le nom du joueur courant
        """
        return self.liste_joueur[0].nom

    def nomJoueur(self,numJoueur):
        """
        retourne le nom du joueur dont le numero est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur    
        résultat: le nom du joueur numJoueur
        """
        return self.liste_joueur[numJoueur].nom

    def prochainTresorJoueur(self,numJoueur):
        """
        retourne le trésor courant du joueur dont le numero est donné en paramètre
        paramètres: joueurs la liste des joueurs
                    numJoueur le numéro du joueur    
        résultat: le prochain trésor du joueur numJoueur (un entier)
        """
        return Joueur.prochainTresor(self.liste_joueur[numJoueur])

    def tresorCourant(self):
        """
        retourne le trésor courant du joueur courant
        paramètre: joueurs la liste des joueurs 
        résultat: le prochain trésor du joueur courant (un entier)
        """
        return self.liste_joueur[0].tresors[0]

    def joueurCourantAFini(self):
        """
        indique si le joueur courant a gagné
        paramètre: joueurs la liste des joueurs 
        résultat: un booleen indiquant si le joueur courant a fini
        """
        if self.liste_joueur[0].tresors == []:
            return True
        return False
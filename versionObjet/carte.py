# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random
"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


class Carte(object):
    
    def __init__(self,nord,est,sud,ouest,tresor=0,pions=[]):
        self.nord=nord
        self.est=est
        self.sud=sud
        self.ouest=ouest
        self.tresor=tresor
        self.pions=pions

    def estValide(self):
        """
        retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
        paramètre: c une carte
        """
        cpt=0
        liste=[self.nord,self.est,self.sud,self.ouest]
        for elem in liste:
            if elem:
                cpt+=1
        if cpt<=2:
            return True

    def murNord(self):  # ok
        """
        retourne un booléen indiquant si la carte possède un mur au nord
        paramètre: c une carte
        """
        
        return self.nord

    def murSud(self): # ok
        """
        retourne un booléen indiquant si la carte possède un mur au sud
        paramètre: c une carte
        """
        return self.sud

    def murEst(self):  # ok
        """
        retourne un booléen indiquant si la carte possède un mur à l'est
        paramètre: c une carte
        """
        return self.est

    def murOuest(self):  # ok
        """
        retourne un booléen indiquant si la carte possède un mur à l'ouest
        paramètre: c une carte
        """
        return self.ouest

    def getListePions(self):
        """
        retourne la liste des pions se trouvant sur la carte
        paramètre: c une carte
        """
        return self.pions

    def setListePions(self,listePions):
        """
        place la liste des pions passées en paramètre sur la carte
        paramètres: c: est une carte
                    listePions: la liste des pions à poser
        Cette fonction ne retourne rien mais modifie la carte
        """
        self.pions=listePions

    def getNbPions(self): # ok 
        """
        retourne le nombre de pions se trouvant sur la carte
        paramètre: c une carte
        """
        return len(self.pions)

    def possedePion(self,pion):
        """
        retourne un booléen indiquant si la carte possède le pion passé en paramètre
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        """
        return pion in self.pions

    def getTresor(self):  # ok
        """
        retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
        paramètre: c une carte
        """
        if self.tresor != None:
            return self.tresor
        return 0

    def prendreTresor(self):
        """
        enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
        paramètre: c une carte
        résultat l'entier représentant le trésor qui était sur la carte
        """
        trésor = self.tresor
        self.tresor=0
        return trésor 

    def mettreTresor(self,tresor):
        """
        met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
        paramètres: c une carte
                    tresor un entier positif
        résultat l'entier représentant le trésor qui était sur la carte
        """
        trésor_remplacé = self.tresor
        self.tresor = tresor
        return trésor_remplacé

    def prendrePion(self, pion):
        """
        enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        Cette fonction modifie la carte mais ne retourne rien
        """
        if pion in self.pions:
            self.pions.remove(pion)

    def poserPion(self, pion):
        """
        pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
        paramètres: c une carte
                    pion un entier compris entre 1 et 4
        Cette fonction modifie la carte mais ne retourne rien
        """
        if pion not in self.pions:
            self.pions.append(pion)

    def tournerHoraire(self):  # ok
        """
        fait tourner la carte dans le sens horaire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        liste=[self.nord,self.est,self.sud,self.ouest]
        last=liste[-1]
        liste.pop()
        liste.insert(0,last)
        self.nord=liste[0]
        self.est=liste[1]
        self.sud=liste[2]
        self.ouest=liste[3]
        

    def tournerAntiHoraire(self):  # ok
        """
        fait tourner la carte dans le sens anti-horaire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        liste=[self.nord,self.est,self.sud,self.ouest]
        self.nord=liste[1]
        self.est=liste[2]
        self.sud=liste[3]
        self.ouest=liste[0]

    def tourneAleatoire(self): 
        """
        faire tourner la carte d'un nombre de tours aléatoire
        paramètres: c une carte
        Cette fonction modifie la carte mais ne retourne rien    
        """
        nb_tours = random.randint(1,4) # nombre de tours générer de facon aléatoire 
        for i in range(nb_tours):
            self.tournerAntiHoraire() # on tourne la carte dans le sens antihoraire i fois
        

    def coderMurs(self):
        """
        code les murs sous la forme d'un entier dont le codage binaire 
        est de la forme bNbEbSbO où bN, bE, bS et bO valent 
        soit 0 s'il n'y a pas de mur dans dans la direction correspondante
        soit 1 s'il y a un mur dans la direction correspondante
        bN est le chiffre des unité, BE des dizaine, etc...
        le code obtenu permet d'obtenir l'indice du caractère semi-graphique
        correspondant à la carte dans la liste listeCartes au début de ce fichier
        paramètre c une carte
        retourne un entier indice du caractère semi-graphique de la carte
        """
        nb=0
        if self.nord:
            nb+=2**0
        if self.est:
            nb+=2**1
        if self.sud:
            nb+=2**2
        if self.ouest:
            nb+=2**3
        return nb
        

    def decoderMurs(self,code):
        """
        positionne les murs d'une carte en fonction du code décrit précédemment
        paramètres c une carte
                code un entier codant les murs d'une carte
        Cette fonction modifie la carte mais ne retourne rien
        """
        murs = []
        for i in reversed(range(4)):
            if code-2**i >= 0:
                code -= 2**i
                murs.append(True)
            elif code - 2**i <= 0:
                murs.append(False)

        self.nord = murs[3]
        self.est = murs[2]
        self.sud = murs[1]
        self.ouest = murs[0]
        


    def toChar(self):
        """
        fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
        paramètres c une carte
        """

        return listeCartes[self.coderMurs()]


    def passageNord(self,carte2):
        """
        suppose que la carte2 est placée au nord de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par le nord
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        if not self.nord and not carte2.sud:
            return True
        else:
            return False
    def passageSud(self,carte2):
        """
        suppose que la carte2 est placée au sud de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par le sud
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        if not self.sud and not carte2.nord:
            return True
        else:
            return False

    def passageOuest(self,carte2):
        """
        suppose que la carte2 est placée à l'ouest de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par l'ouest
        paramètres carte1 et carte2 deux cartes
        résultat un booléen
        """
        if not self.ouest and not carte2.est:
            return True
        else:
            return False

    def passageEst(self,carte2):
        """
        suppose que la carte2 est placée à l'est de la carte1 et indique
        s'il y a un passage entre ces deux cartes en passant par l'est
        paramètres carte1 et carte2 deux cartes
        résultat un booléen    
        """
        if not self.est and not carte2.ouest:
            return True
        else:
            return False

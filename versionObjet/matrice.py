# -*- coding: utf-8 -*-
"""
                           Projet Labyrinthe 
        Projet Python 2019-2020 de 1ere année et AS DUT Informatique Orléans
        
   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------
class Matrice(object):

    def __init__(self,nbLignes,nbColonnes,valeurParDefaut=0):
        """
        constructeur
        """
        self._nbLignes=nbLignes
        self._nbColonnes=nbColonnes
        self._listeDesValeurs=[valeurParDefaut]*(nbLignes*nbColonnes)

    def getNbLignes(self):
        return self._nbLignes

    def getNbColonnes(self):
        return self._nbColonnes

    def getVal(self,lig,col):
        return self._listeDesValeurs[lig*self._nbColonnes+col]

    def setVal(self,lig,col,val):
        self._listeDesValeurs[lig*self._nbColonnes+col]=val

    def afficheLigneSeparatrice(self,tailleCellule=4):
        print()
        for i in range(self.getNbColonnes()+1):
            print('-'*tailleCellule+'+',end='')
        print()
   
    def affiche(self,tailleCellule=4):
        nbColonnes=self.getNbColonnes()
        nbLignes=self.getNbLignes()
        print(' '*tailleCellule+'|',end='')
        for i in range(nbColonnes):
            print(str(i).center(tailleCellule)+'|',end='')
        self.afficheLigneSeparatrice(tailleCellule)
        for i in range(nbLignes):
            print(str(i).rjust(tailleCellule)+'|',end='')
            for j in range(nbColonnes):
                print(str(self.getVal(i,j)).rjust(tailleCellule)+'|',end='')
            self.afficheLigneSeparatrice(tailleCellule)
        print()
#------------------------------------------        
# decalages
#------------------------------------------
    def decalageLigneAGauche(self, numLig, nouvelleValeur=0):
        """
        permet de décaler une ligne vers la gauche en insérant une nouvelle
        valeur pour remplacer la premiere case à droite de cette ligne
        le fonction retourne la valeur qui a été éjectée
        paramèteres: matrice la matrice considérée
                    numLig le numéro de la ligne à décaler
                    nouvelleValeur la valeur à placer
        résultat la valeur qui a été ejectée lors du décalage
        """
        matriceClone = self
        res = self.getVal(numLig, 0) # la valeur a exclure 
        for x in range(0,7):
            print(x)
            self.setVal(numLig,x,matriceClone.getVal(numLig,x+1))
        self.setVal(numLig,6,nouvelleValeur) # ajout de la nouvelle valeur a droite car on decale a gauche 

        return res

    def decalageLigneADroite(self, numLig, nouvelleValeur=0):
        """
        decale la ligne numLig d'une case vers la droite en insérant une nouvelle
        valeur pour remplacer la premiere case à gauche de cette ligne
        paramèteres: matrice la matrice considérée
                    numLig le numéro de la ligne à décaler
                    nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        matriceClone = self
        res = self.getVal(numLig, 6) # la valeur a exclure 
        
        for x in range(6,-1,-1):
            self.setVal(numLig,x,matriceClone.getVal(numLig,x-1))

        self.setVal(numLig,0,nouvelleValeur) # ajout de la nouvelle valeur a gauche car on decale a droite 

        return res

    def decalageColonneEnHaut(self, numCol, nouvelleValeur=0):
        """
        decale la colonne numCol d'une case vers le haut en insérant une nouvelle
        valeur pour remplacer la premiere case en bas de cette ligne
        paramèteres: matrice la matrice considérée
                    numCol le numéro de la colonne à décaler
                    nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        
        matriceClone = self
        res = self.getVal( 0, numCol) # la valeur a exclure 
        for x in range(0,6):
            print(x)
            self.setVal(x,numCol,matriceClone.getVal(x+1,numCol))
        self.setVal(6,numCol,matriceClone.getVal(6,numCol))
        self.setVal(6,numCol,nouvelleValeur) # ajout de la nouvelle valeur a droite car on decale a gauche 

        return res

    def decalageColonneEnBas(self, numCol, nouvelleValeur=0):
        """
        decale la colonne numCol d'une case vers le bas en insérant une nouvelle
        valeur pour remplacer la premiere case en haut de cette ligne
        paramèteres: matrice la matrice considérée
                    numCol le numéro de la colonne à décaler
                    nouvelleValeur la valeur à placer
        résultat: la valeur de la case "ejectée" par le décalage
        """
        matriceClone = self
        res = self.getVal(0, numCol) # la valeur a exclure 
        for x in range(0,6):
            print(x)
            self.setVal(x,numCol,matriceClone.getVal(x+1,numCol))

        self.setVal(6,numCol,matriceClone.getVal(6,numCol))
        self.setVal(6,numCol,nouvelleValeur) # ajout de la nouvelle valeur a droite car on decale a gauche 

        return res


# x = Matrice(7,7)
# setVal(x,0,2,10)
# setVal(x,1,2,11)
# setVal(x,2,2,12)
# setVal(x,3,2,13)
# setVal(x,4,2,14)
# setVal(x,5,2,15)
# setVal(x,6,2,16)
# afficheMatrice(x) 
# print("Valeur dégagé : " + str(decalageColonneEnBas(x,2,8)))
# afficheMatrice(x) 
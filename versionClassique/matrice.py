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

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    if nbColonnes > 0 and nbLignes > 0 :
        mat = {}
        mat['nbLignes'] = nbLignes
        mat['nbColonnes'] = nbColonnes
        mat['val'] = [valeurParDefaut]*(nbColonnes*nbLignes)
        return mat
    else:
        return "Erreur, nbColones et nbLinges doivent etres positifs"

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice["nbLignes"]

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return matrice["nbColonnes"]

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice['val'][ligne * getNbColonnes(matrice) + colonne]


def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice['val'][ligne * getNbColonnes(matrice) + colonne] = valeur


#-----------------------------------------
# Fonctions utiles au débuggage
#-----------------------------------------

def afficheLigneSeparatrice(matrice, tailleCellule=4):
    """
    Affichage d'une matrice
    fonction annexe pour afficher les lignes séparatrices
    """
    print()
    for i in range(getNbColonnes(matrice) + 1):
        print('-' * tailleCellule + '+', end='')
    print()


def afficheMatrice(matrice, tailleCellule=4):
    """
    Affiche la matrice en mode texte
    """
    nbColonnes = getNbColonnes(matrice)
    nbLignes = getNbLignes(matrice)
    print(' ' * tailleCellule + '|', end='')
    for i in range(nbColonnes):
        print(str(i).center(tailleCellule) + '|', end='')
    afficheLigneSeparatrice(matrice, tailleCellule)
    for i in range(nbLignes):
        print(str(i).rjust(tailleCellule) + '|', end='')
        for j in range(nbColonnes):
            print(str(getVal(matrice, i, j)).rjust(tailleCellule) + '|', end='')
        afficheLigneSeparatrice(matrice, tailleCellule)
    print()



#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    matriceClone = matrice
    res = getVal(matrice, numLig, 0) # la valeur a exclure 
    for x in range(0,7):
        print(x)
        setVal(matrice,numLig,x,getVal(matriceClone,numLig,x+1))
    setVal(matrice,numLig,6,nouvelleValeur) # ajout de la nouvelle valeur a droite car on decale a gauche 

    return res

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    matriceClone = matrice
    res = getVal(matrice, numLig, 6) # la valeur a exclure 
    
    for x in range(6,-1,-1):
        setVal(matrice,numLig,x,getVal(matriceClone,numLig,x-1))

    setVal(matrice,numLig,0,nouvelleValeur) # ajout de la nouvelle valeur a gauche car on decale a droite 

    return res

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    matriceClone = matrice
    res = getVal(matrice, 0, numCol) # la valeur a exclure 
    for x in range(0,6):
        print(x)
        setVal(matrice,x,numCol,getVal(matriceClone,x+1,numCol))
    setVal(matrice,6,numCol,getVal(matriceClone,6,numCol))
    setVal(matrice,6,numCol,nouvelleValeur) # ajout de la nouvelle valeur a droite car on decale a gauche 

    return res

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    matriceClone = matrice
    res = getVal(matrice, 0, numCol) # la valeur a exclure 
    for x in range(0,6):
        print(x)
        setVal(matrice,x,numCol,getVal(matriceClone,x+1,numCol))

    setVal(matrice,6,numCol,getVal(matriceClone,6,numCol))
    setVal(matrice,6,numCol,nouvelleValeur) # ajout de la nouvelle valeur a droite car on decale a gauche 

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
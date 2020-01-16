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


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    Carte_drop = {
        "Nord":nord,
        "Est":est,
        "Sud":sud,
        "Ouest":ouest,
        "Trésor":tresor,
        "Pions":pions}

    return Carte_drop
assert Carte(True,True,False,False,5,[1,2,3,4]) == {
        "Nord":True,
        "Est":True,
        "Sud":False,
        "Ouest":False,
        "Trésor":5,
        "Pions":[1,2,3,4]}

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    cpt=0
    if murNord(c):
        cpt+=1
    if murOuest(c):
        cpt+=1
    if murEst(c):
        cpt+=1
    if murSud(c):
        cpt+=1
    if cpt>2:
        return False
    else:
        return True

def murNord(c):  # ok
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    
    return c["Nord"]

def murSud(c): # ok
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c["Sud"]

def murEst(c):  # ok
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c["Est"]

def murOuest(c):  # ok
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c["Ouest"]

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["Pions"]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["Pions"]=listePions

def getNbPions(c): # ok 
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c["Pions"])

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    return pion in c["Pions"]

def getTresor(c):  # ok
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["Trésor"]
def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    trésor = c["Trésor"]
    c["Trésor"]=0
    return trésor 

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    trésor_remplacé = c["Trésor"]
    c["Trésor"] = tresor
    return trésor_remplacé

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion in c["Pions"]:
        c["Pions"].remove(pion)

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c["Pions"]:
        c["Pions"].append(pion)

def tournerHoraire(c):  # ok
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    liste=[c["Nord"],c["Est"],c["Sud"],c["Ouest"]]
    last=liste[-1]
    liste.pop()
    liste.insert(0,last)
    c["Nord"]=liste[0]
    c["Est"]=liste[1]
    c["Sud"]=liste[2]
    c["Ouest"]=liste[3]
    

def tournerAntiHoraire(c):  # ok
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    liste=[c["Nord"],c["Est"],c["Sud"],c["Ouest"]]
    c["Nord"]=liste[1]
    c["Est"]=liste[2]
    c["Sud"]=liste[3]
    c["Ouest"]=liste[0]

def tourneAleatoire(c): 
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    nb_tours = random.randint(1,4) # nombre de tours générer de facon aléatoire 
    for i in range(nb_tours):
        tournerAntiHoraire(c) # on tourne la carte dans le sens antihoraire i fois
    

def coderMurs(c):
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
    if murNord(c):
        nb+=2**0
    if murEst(c):
        nb+=2**1
    if murSud(c):
        nb+=2**2
    if murOuest(c):
        nb+=2**3
    return nb
    

def decoderMurs(c,code):
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

    c["Nord"] = murs[3]
    c["Est"] = murs[2]
    c["Sud"] = murs[1]
    c["Ouest"] = murs[0]
    


def toChar(c): #TODO
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """

    return listeCartes[coderMurs(c)]


def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if not murNord(carte1) and not murSud(carte2):
        return True
    else:
        return False

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if not murSud(carte1) and not murNord(carte2):
        return True
    else:
        return False

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if not murOuest(carte1) and not murEst(carte2):
        return True
    else:
        return False

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    if not murEst(carte1) and not murOuest(carte2):
        return True
    else:
        return False

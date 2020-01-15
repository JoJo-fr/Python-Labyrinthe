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
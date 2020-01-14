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
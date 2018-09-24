# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 08:05:03 2018

@author: hoehnd
"""

#Konstanten
GROESSE = 10 #Spielfeldgröße (x und y)

from random import randint

class Schiff(object):
    
    def __init__(self,laenge):
        self.laenge = laenge
        
class Computer(object):
    
    #def __init__(self):

    def waehleSchiffposition(self, schiff):
        x = randint(0, GROESSE)
        y = randint(0, GROESSE)
        jop = randint(0,2)
        if jop == 0:
            richtung = True
        else:
            richtung = False
        try:
            Meer.setzeSchiff(meerComputer, x, y, richtung, schiff)
        except:
            Computer.waehleSchiffposition(meerComputer, schiff)


    def zug(self):
        x = randint(0, GROESSE)
        y = randint(0, GROESSE)
        
        if meerSpieler.get(x,y) == 2 or meerSpieler.get(x,y) == 3:
            self.zug()
        else:
            Meer.schiessen(meerSpieler,x,y)
            #ToDo prüfen ob man gewonnen hat
            
class Spieler(object):
    
    #def __init__(self):

    def waehleSchiffposition(self, schiff):
        x = int(input("x: "))
        y = int(input("y: "))
        richtung = bool(input("True = Waagerecht | False = Senkrecht"))
        try:
            Meer.setzeSchiff(meerSpieler, x, y, richtung, schiff)
        except:
            print("Hier kann kein Schiff platziert werden!")
            Spieler.waehleSchiffposition(meerSpieler, schiff)

    def zug(self):
        x = int(input("x: "))
        y = int(input("y: "))
        
        if meerComputer.get(x,y) == 2 or meerComputer.get(x,y) == 3:
            print("Dort haben Sie schon hingeschossen!")
            self.zug()
        else:
            Meer.schiessen(meerComputer,x,y)
            #ToDo prüfen ob man gewonnen hat ?
            if Meer.gewonnen(meerSpieler) == True:
                print("Sie haben gewonnen!")

class Meer(object):
    
    # 0 = Wasser
    # 1 = Schiff
    # 2 = Wasser kein Treffer
    # 3 = Treffer
    
    def __init__(self,FelderX,FelderY):
        self.FelderX = FelderX
        self.FelderY = FelderY
        self.meer = [0]*self.FelderX
        for i in range(0,self.FelderX):
            self.meer[i] = [0]*self.FelderY
           
    #wird benötigt um zu überprüfen ob an die jeweilige Stelle bereits geschossen wurde             
    def get(self,x,y):
        return self.meer[x][y]
    
    def zeige(self):
        for i in range(0,self.FelderY):
            string = ""
            for j in range(0,self.FelderX):
                if self.meer[j][i] == 0:
                    string += " ~"
                elif self.meer[j][i] == 1:
                    string += " S"
                elif self.meer[j][i] == 2:
                    string += " °"
                elif self.meer[j][i] == 3:
                    string += " T"
            print(string)
                    
    def setzeSchiff(self,x,y,richtung,schiff):
        #waagerecht
        if(richtung == True):
            for i in range(0,schiff.laenge):
                self.meer[y][x] = 1
                y += 1
        #senkrecht
        else:
            for i in range(0,schiff.laenge):
                self.meer[y][x] = 1
                x += 1
                
    def schiessen(self,x,y):
        if self.meer[y][x] == 1:
            self.meer[y][x] = 3
        else:
            self.meer[y][x] = 2
        self.gewonnen()
            
    def gewonnen(self):
        anzTreffer = 0
        for i in range(0,self.FelderY):
            for j in range(0,self.FelderX):
                if self.meer[j][i] == 3:
                    anzTreffer += 1
        #Alle Schiffe sind versenkt
        if anzTreffer == 3: #ToDo 3 durch Anzahl der Schiffe*Schifflaenge ersetzen
            return True
             
###############################################        

#Hilfsvariablen
ende = False #Wird auf True gesetzt, sobald ein Spieler gewonnen hat.
zug = True #True = Spielerzug | False = Computerzug

#Spielfelder definieren
meerComputer = Meer(GROESSE,GROESSE)
meerSpieler = Meer(GROESSE,GROESSE)

#Schiffe definieren            
schlachtschiff = Schiff(5)
kreuzer = Schiff(4)
zerstoerer = Schiff(3)
uboot = Schiff(2)

#Spieler erstellen
computer = Computer()
spieler = Spieler()

#Spieler platziert Schiffe
print("Platziere deine Flotte.")

print("Platziere dein Schlachtschiff (5)")
Spieler.waehleSchiffposition(spieler, schlachtschiff)

print("Platziere deinen Kreuzer (4)")
Spieler.waehleSchiffposition(spieler, kreuzer)
#ToDo weitere Schiffe platzieren

print("Du hast deine Schiffe platziert.")
Meer.zeige(meerSpieler)

#Computer platziert Schiffe
Computer.waehleSchiffposition(computer, schlachtschiff)
Computer.waehleSchiffposition(computer, kreuzer)

#Jetzt wird gespielt
#print("Los Gehts!")
#while (ende == False):
 #   if(zug == True):
        #Spielerzug
  #      zug = False
  #  else:
        #Computerzug
   #     zug = True
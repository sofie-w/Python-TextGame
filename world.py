import random
from enemy import Enemy, Special_Enemy
from room import Room
from items import appel, brood, taart, soep, ijs, handschoen, zwaard, pijl_boog, mes, knuppel, sleutel_zilver, sleutel_goud
from item_maken import Item
from gegevens import hight, width



class World: #Maakt een random wereld
    def __init__(self, _name):

        self.world = [['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.']]
        self.name = _name
        self.poss_items = []
        self.poss_Enemy = []
        self.rooms = []
        self.muur = Room('muur', self)

    def create_world(self, persoon):
        
        
        for i in range(4):
            self.poss_items.append(appel)
        for i in range(4):
            self.poss_items.append(brood)
        self.poss_items.append(zwaard)
        self.poss_items.append(pijl_boog)
        for i in range(3):
            self.poss_items.append(sleutel_goud)
        for i in range(3):
            self.poss_items.append(sleutel_zilver)
            
            
        monster1 = Enemy()
        monster2 = Enemy()
        monster3 = Enemy()
        monster4 = Enemy()
        monster5 = Enemy()
        monster6 = Enemy()
        monster7 = Enemy()
        monster8 = Special_Enemy('vuur monster', 'Het monster spuwt vuur naar je toe, het kost je 6 levens.')
        monster9 = Special_Enemy('vuur monster', 'Het monster spuwt vuur naar je toe, het kost je 6 levens.')
        monster10 = Special_Enemy('vuur monster', 'Het monster spuwt vuur naar je toe, het kost je 6 levens.')
        monster11 = Special_Enemy('water monster', 'Het monster maakt een waterkolk om je heen dit kost je 6 levens.')
        monster12 = Special_Enemy('water monster', 'Het monster maakt een waterkolk om je heen dit kost je 6 levens.')
        monster13 = Special_Enemy('water monster', 'Het monster maakt een waterkolk om je heen dit kost je 6 levens.')
        monster14 = Special_Enemy('plant monster', 'Het monster geeft je een klap met een tak dit kost je 6 levens.')
        monster15 = Special_Enemy('plant monster', 'Het monster geeft je een klap met een tak dit kost je 6 levens.')
        monster16 = Special_Enemy('plant monster', 'Het monster geeft je een klap met een tak dit kost je 6 levens.')
        
        self.poss_Enemy.append(monster1)
        self.poss_Enemy.append(monster2)
        self.poss_Enemy.append(monster3)
        self.poss_Enemy.append(monster4)
        self.poss_Enemy.append(monster5)
        self.poss_Enemy.append(monster6)
        self.poss_Enemy.append(monster7)
        self.poss_Enemy.append(monster8)
        self.poss_Enemy.append(monster9)
        self.poss_Enemy.append(monster10)
        self.poss_Enemy.append(monster11)
        self.poss_Enemy.append(monster12)
        self.poss_Enemy.append(monster13)
        self.poss_Enemy.append(monster14)
        self.poss_Enemy.append(monster15)
        self.poss_Enemy.append(monster16)
        
        
        #Voegt alle kamers toe
        #Zorg dat hight * width even is als het aantal kamers
        item_kamer = self.random_item()
        monster = self.random_enemy()
        keuken = Room('keuken', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        woonkamer = Room('woonkamer', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        eetkamer = Room('eetkamer', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        badkamer = Room('badkamer', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        gang = Room('gang', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        balkon = Room('balkon', self, item_kamer, monster) #!
        item_kamer = self.random_item()
        monster = self.random_enemy()
        tuin = Room('tuin', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        bibliotheek = Room('bibliotheek', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        slaapkamer = Room('slaapkamer', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        hobbykamer = Room('hobbykamer', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        balzaal = Room('balzaal', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        studeerkamer = Room('studeerkamer', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        serre = Room('serre', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        garage = Room('garage', self, item_kamer, monster)
        item_kamer = self.random_item()
        monster = self.random_enemy()
        kelder = Room('kelder', self, item_kamer, monster) #!
        item_kamer = self.random_item()
        monster = self.random_enemy()
        zolder = Room('zolder', self, item_kamer, monster) #!
        
        
        self.add_room(keuken)
        self.add_room(woonkamer)
        self.add_room(eetkamer)
        self.add_room(badkamer)
        self.add_room(gang)
        self.add_room(balkon)
        self.add_room(tuin)
        self.add_room(bibliotheek)
        self.add_room(slaapkamer)
        self.add_room(hobbykamer)
        self.add_room(balzaal)
        self.add_room(studeerkamer)
        self.add_room(serre)        
        self.add_room(garage)
        self.add_room(kelder)
        self.add_room(zolder)
        

        for i in range(hight):
            for j in range(width):
                room = random.choice(self.rooms)
                self.world[i][j] = room
                room.x = i
                room.y = j
                self.rooms.remove(room)
                
        for i in range(hight):
            for j in range(width):
                self.world[i][j].add_exit()
                

        self.first_room(persoon)
        
    def random_item(self):
        item_kamer = random.choice(self.poss_items)
        self.poss_items.remove(item_kamer)
        return(item_kamer)
    
    def random_enemy(self):
        enemy = random.choice(self.poss_Enemy)
        self.poss_Enemy.remove(enemy)
        return(enemy)


    def add_room(self, _new_room):
        self.rooms.append(_new_room)


    def first_room(self, persoon):
        x = random.randint(0, width-1)
        y = random.randint(0, hight-1)

        firstroom = self.world[x][y]
        persoon.set_current_room(firstroom)
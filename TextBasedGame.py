import random
import os
import sys

hight = 4
width = 4

class Room:
    def __init__(self, _room_name, _world, _item):
        #mana.add_room(self)
        self.exits = []
        self.items = []
        self.items.append(_item)
        self.world = _world
        self.name = _room_name
        
    
    def add_exit(self, x, y):
        if x-1 >= 0:
            self.exits.append(self.world.world[x-1][y].name)
            print('De kamer voor je zie je '+ self.exits[len(self.exits)-1])
        if x+1 <= hight-1:
            self.exits.append(self.world.world[x+1][y].name)
            print('De kamer achter je is de '+ self.exits[len(self.exits)-1])
        if y-1 >= 0:
            self.exits.append(self.world.world[x][y-1].name)
            print('De kamer links van je is '+ self.exits[len(self.exits)-1])
        if y+1 <= width-1:
            self.exits.append(self.world.world[x][y+1].name)
            print('De kamer rechts van je is '+ self.exits[len(self.exits)-1])
        
         
        
    def describe(self):
        print('Je bent nu in de ' + self.name + '. Je ziet een '+ self.items[0].item_name + ' liggen.') # Maak grammatica correct bij alle kamers!
        vraag = input('Wil je dit meenemen(y/n): ')
        if vraag == 'y':
            item = self.items[0]
            self.items.remove(self.items[0])
            return(item)
            
        else:
            return(0)
            
        
            
        
        

class World:
    def __init__(self, _name):
        
        self.world = [['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.']]
        self.name = _name
        self.rooms = []
    
    def create_world(self, person):
        #Voegt alle kamers toe
        #Zorg dat hight * width even is als het aantal kamers
        
        keuken = Room('keuken', self, appel)
        self.add_room(keuken)
        woonkamer = Room('woonkamer', self, appel)
        self.add_room(woonkamer)
        eetkamer = Room('eetkamer', self, sleutel_goud)
        self.add_room(eetkamer)
        badkamer = Room('badkamer', self, zwaard)
        self.add_room(badkamer)
        gang = Room('gang', self, appel)
        self.add_room(gang)
        balkon = Room('balkon', self, appel) #!
        self.add_room(balkon)
        tuin = Room('tuin', self, sleutel_goud)
        self.add_room(tuin)
        bibliotheek = Room('bibliotheek', self, appel)
        self.add_room(bibliotheek)
        slaapkamer = Room('slaapkamer', self, boog)
        self.add_room(slaapkamer)
        hobbykamer = Room('hobbykamer', self, brood)
        self.add_room(hobbykamer)
        fitnessruimte = Room('fitnessruimte', self, brood)
        self.add_room(fitnessruimte)
        studeerkamer = Room('studeerkamer', self, brood)
        self.add_room(studeerkamer)
        serre = Room('serre', self, sleutel_zilver)
        self.add_room(serre)
        garage = Room('garage', self, brood)
        self.add_room(garage)
        kelder = Room('kelder', self, brood) #!
        self.add_room(kelder)
        zolder = Room('zolder', self, sleutel_goud) #!
        self.add_room(zolder)

        for i in range(hight):
            for j in range(width):
                room = random.choice(self.rooms)
                self.world[i][j] = room
                self.rooms.remove(room)
                
        self.first_room(person)
                
        
        
    def add_room(self, _new_room):
        self.rooms.append(_new_room)
        
        
        
    def first_room(self, person):
        x = random.randint(0, width-1)
        y = random.randint(0, hight-1)
        
        #stop de player in deze kamer eerst:
        firstroom = self.world[x][y]
        #firstroom.describe()
        #firstroom.add_exit(x,y)
        person.set_current_room(firstroom)
        room = person.get_current_room(self, x,y)
        #print(room)
        
        
        
class Player:
    def __init__(self):
        self.inventory = []
        self.name =  input("Hoe heet je: ")
        print("Hoi "+ self.name + '!')
    
    def goto_room(self, name):
        print("hoi")
        
    def set_current_room(self, room):
        current_room = room
        item = current_room.describe()
        if item != 0:
            self.pick_up(item)
            
        
    def get_current_room(self, world, x, y):
        room = world.world[x][y]
        return(room)
    
    def pick_up(self, item):
        self.inventory.append(item)
        self.print_inv()
        
    def print_inv(self):
        for i in range(len(self.inventory)):
            print(self.inventory[i].item_name)
        
        
        
class Controller:
    def __init__(self):
        self.play_game()
        
        
    def play_game(self):
        person = Player()
        mana = World("Mana") 
        mana.create_world(person)
        clear_screen()
        print('Lopen: L \nInventory bekijken: I \nHonger bekijken: H')
        
        
        
        
class Item:
    def __init__(self, _name, _itemtype):
        self.item_name = _name
        self.item_type = _itemtype
        
        
def clear_screen():
    py.emptyEcho();
        
        

#Items in het spel
appel = Item('Appel', 'eten')
brood = Item('Brood', 'eten')
zwaard = Item('Zwaard', 'wapen')
boog = Item('Pijl en Boog', 'wapen')
sleutel_goud = Item('Gouden Sleutel', 'sleutel')
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel')

speel = Controller()
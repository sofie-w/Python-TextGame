import random

hight = 4
width = 4

class Room:
    def __init__(self, _room_name):
        mana.add_room(_room_name)
        self.exits = []
#          self.description = _uitleg
        
    def test(self):
        print("test")
    
    def add_exit(self, x, y):
        if x-1 >= 0:
            self.exits.append(mana.world[x-1][y])
            print('De kamer voor je zie je '+ self.exits[len(self.exits)-1])
        if x+1 <= hight-1:
            self.exits.append(mana.world[x+1][y])
            print('De kamer achter je is de '+ self.exits[len(self.exits)-1])
        if y-1 >= 0:
            self.exits.append(mana.world[x][y-1])
            print('De kamer links van je is '+ self.exits[len(self.exits)-1])
        if y+1 <= width-1:
            self.exits.append(mana.world[x][y+1])
            print('De kamer rechts van je is '+ self.exits[len(self.exits)-1])
        
         
        
    def describe(self, room):
        print('Je bent nu in de ' + room + '.') # Maak grammatica correct bij alle kamers!  
        
        
        

class World:
    def __init__(self, _name):
        self.world = [['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.']]
        self.name = _name
        self.rooms = []
    
    def create_world(self):
        for i in range(hight):
            for j in range(width):
                room = random.choice(self.rooms)
                self.world[i][j] = room
                self.rooms.remove(room)
                
        
        mana.print_world()
        
        #mana.first_room()
    def print_world(self):
        for i in range(hight):
            print(self.world[i])
            print(' ')
        
        
    def add_room(self, _new_room):
        self.rooms.append(_new_room)
        
    def first_room(self):
        x = random.randint(0, width-1)
#         x = 3
        y = random.randint(0, hight-1)
        
        #stop de player in deze kamer eerst:
        firstroom = self.world[x][y]
        #keuken = Room('keuken')
        #woonkamer = Room('woonkamer')
        #eetkamer = Room('eetkamer')
        #badkamer = Room('badkamer')
        #gang = Room('gang')
        #balkon = Room('balkon')
        #tuin = Room('tuin')
        #bibliotheek = Room('bibliotheek')
        #slaapkamer = Room('slaapkamer')
        
        #keuken.add_exit(x,y)
        
        current = Room("Currrent")
        print('Je begint in de '+ firstroom + '.')
        #current.describe(firstroom)
        current.add_exit(x,y)
        
class Player:
    def __init__(self, _name):
        self.inventory = []
        self.name =  _name
        print("Hoi "+ self.name + '!')
    
    def goto_room(self, name):
        print("hoi")
        
    def set_current_room(self, room):
        print("hoi")
    
    def get_current_room(self, x, y):
        print("hoi")
    
    def pick_up(self, item):
        print("hoi")
        
class Controller:
    def __init__(self):
        print('play')
        
        
    def play_game():
        print("hoi")
        
        
        
class Item:
    def __init__(self, _name, _itemtype):
        self.item_name = _name
        self.item_type = _itemtype
        
        
       
#Maakt de wereld
mana = World("Mana")       
    
    
#Voegt alle kamers toe
#Zorg dat hight * width even is als het aantal kamers
keuken = Room('keuken')
woonkamer = Room('woonkamer')
eetkamer = Room('eetkamer')
badkamer = Room('badkamer')
gang = Room('gang')
balkon = Room('balkon')
tuin = Room('tuin')
bibliotheek = Room('bibliotheek')
slaapkamer = Room('slaapkamer')
hobbykamer = Room('hobbykamer')
fitnessruimte = Room('fitnessruimte')
studeerkamer = Room('studeerkamer')
serre = Room('serre')
garage = Room('garage')
kelder = Room('kelder')
zolder = Room('zolder')

#Items in het spel
appel = Item('Appel', 'eten')
brood = Item('Brood', 'eten')
zwaard = Item('Zwaard', 'wapen')
boog = Item('Pijl en Boog', 'wapen')
sleutel_goud = Item('Gouden Sleutel', 'sleutel')
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel')
       

mana.create_world()

name = input("Hey, hoe wil je in dit spel heten: ")
user = Player(name)

mana.first_room()
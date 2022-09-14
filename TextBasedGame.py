import random

hight = 3
width = 3

class Room:
    def __init__(self, _room_name):
        mana.add_room(_room_name)
        self.exits = []
         self.description = _uitleg
        
    def test(self):
        print("test")
    
    def uitgang(self, x, y):
        if x-1 >= 0:
            self.exits.append(mana.world[x-1][y])
            print("in")
        print("uit")
        
    def describe(self, room):
        print('Je bent nu in de ' + room + '.')
        if room == 'keuken':
            print("Dit is de keuken...")
        if room == 'badkamer':
            print("Dit is de badkamer...")
        if room == 'tuin':
            print("Dit is de tuin...")
        if room == 'bibliotheek':
            print("Dit is de bibliotheek...")
        if room == 'woonkamer':
            print("Dit is de woonkamer...")
        if room == 'eetkamer':
            print("Dit is de eetkamer...")
        if room == 'slaapkamer':
            print("Dit is de slaapkamer...")
        if room == 'balkon':
            print("Dit is het balkon...")
        if room == 'gang':
            print("Je bent nu in de gang")
            
        
        
        

class World:
    def __init__(self, _name):
        self.world = [['.','.','.'],
                      ['.','.','.'],
                      ['.','.','.']]
        self.name = _name
        self.rooms = []
    
    def create_world(self):
        for i in range(hight):
            for j in range(width):
                room = random.choice(self.rooms)
                self.world[i][j] = room
                self.rooms.remove(room)
        print(self.world)
        
        mana.first_room()
        
        
    def add_room(self, _new_room):
        self.rooms.append(_new_room)
        
    def first_room(self):
        x = random.randint(0, width-1)
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
        
        
        
        current = Room("Currrent")
        print('Je begint in de '+ firstroom + '.')
        #current.describe(firstroom)
        current.uitgang(x,y)
        
class Player:
    def __init__(self, _name):
        self.inventory = []
        self.name =  _name
        print("Hoi "+ self.name + ', je komt straks in een huis terecht daar moet je wat gaan doen.')
    
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
        
        
       
       
mana = World("Mana")       
       
keuken = Room('keuken')
woonkamer = Room('woonkamer')
eetkamer = Room('eetkamer')
badkamer = Room('badkamer')
gang = Room('gang')
balkon = Room('balkon')
tuin = Room('tuin')
bibliotheek = Room('bibliotheek')
slaapkamer = Room('slaapkamer')

appel = Item('Appel', 'eten')
brood = Item('Brood', 'eten')
zwaard = Item('Zwaard', 'wapen')
boog = Item('Pijl en Boog', 'wapen')
sleutel_goud = Item('Gouden Sleutel', 'sleutel')
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel')
       

mana.create_world()

print('hoiii')

name = input("Hey, hoe wil je in dit spel heten: ")
user = Player(name)

mana.first_room()
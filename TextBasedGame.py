import random

hight = 4
width = 4

class Room:
    def __init__(self, _room_name, _world):
        #mana.add_room(self)
        self.exits = []
        self.world = _world
        self.name = _room_name
        
        #self.description = ""
#          self.description = _uitleg
        
    def test(self):
        print("test")
    
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
    
    def create_world(self, person):
        #Voegt alle kamers toe
        #Zorg dat hight * width even is als het aantal kamers
        
        keuken = Room('keuken', self)
        self.add_room(keuken)
        woonkamer = Room('woonkamer', self)
        self.add_room(woonkamer)
        eetkamer = Room('eetkamer', self)
        self.add_room(eetkamer)
        badkamer = Room('badkamer', self)
        self.add_room(badkamer)
        gang = Room('gang', self)
        self.add_room(gang)
        balkon = Room('balkon', self) #!
        self.add_room(balkon)
        tuin = Room('tuin', self)
        self.add_room(tuin)
        bibliotheek = Room('bibliotheek', self)
        self.add_room(bibliotheek)
        slaapkamer = Room('slaapkamer', self)
        self.add_room(slaapkamer)
        hobbykamer = Room('hobbykamer', self)
        self.add_room(hobbykamer)
        fitnessruimte = Room('fitnessruimte', self)
        self.add_room(fitnessruimte)
        studeerkamer = Room('studeerkamer', self)
        self.add_room(studeerkamer)
        serre = Room('serre', self)
        self.add_room(serre)
        garage = Room('garage', self)
        self.add_room(garage)
        kelder = Room('kelder', self) #!
        self.add_room(kelder)
        zolder = Room('zolder', self) #!
        self.add_room(zolder)
        #keuken = Room('keuken', '')
        #self.add_room(keuken)
        for i in range(hight):
            for j in range(width):
                room = random.choice(self.rooms)
                #print(room, "##")
                self.world[i][j] = room
                self.rooms.remove(room)
                
        self.first_room(person)
                
                
        
        
    def add_room(self, _new_room):
        self.rooms.append(_new_room)
        
        
        
    def first_room(self, person):
        x = random.randint(0, width-1)
#         x = 3
        y = random.randint(0, hight-1)
        
        #stop de player in deze kamer eerst:
        firstroom = self.world[x][y]
        firstroom.describe(firstroom.name)
        firstroom.add_exit(x,y)
        person.set_current_room(firstroom)
        room = person.get_current_room(self, x,y)
        print(room)
        
        
        
class Player:
    def __init__(self):
        self.inventory = []
        self.name =  input("Hoe heet je: ")
        print("Hoi "+ self.name + '!')
    
    def goto_room(self, name):
        print("hoi")
        
    def set_current_room(self, room):
        current_room = room
        
    
    def get_current_room(self, world, x, y):
        room = world.world[x][y]
        return(room)
    
    def pick_up(self, item):
        print("hoi")
        
        
class Controller:
    def __init__(self):
        self.play_game()
        
        
    def play_game(self):
        person = Player()
        mana = World("Mana") 
        mana.create_world(person)
        
        
        
        
class Item:
    def __init__(self, _name, _itemtype):
        self.item_name = _name
        self.item_type = _itemtype
        
        

#Items in het spel
appel = Item('Appel', 'eten')
brood = Item('Brood', 'eten')
zwaard = Item('Zwaard', 'wapen')
boog = Item('Pijl en Boog', 'wapen')
sleutel_goud = Item('Gouden Sleutel', 'sleutel')
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel')

speel = Controller()
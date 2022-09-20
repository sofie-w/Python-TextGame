import random

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
        self.x = 0
        self.y = 0


    def add_exit(self):
        if self.x-1 >= 0:
            self.exits.append(self.world.world[self.x-1][self.y])
            print('Voor(W): '+ self.exits[len(self.exits)-1].name)
        else:
            print("Voor(W): Muur")
            self.exits.append("Muur")
        if self.y-1 >= 0:
            self.exits.append(self.world.world[self.x][self.y-1])
            print('Links(A): '+ self.exits[len(self.exits)-1].name)
        else:
            print("Links(A): Muur")
            self.exits.append("Muur")
        if self.x+1 <= hight-1:
            self.exits.append(self.world.world[self.x+1][self.y])
            print('Achter(S): '+ self.exits[len(self.exits)-1].name)
        else:
            print("Achter(S): Muur")
            self.exits.append("Muur")
        if self.y+1 <= width-1:
            self.exits.append(self.world.world[self.x][self.y+1])
            print('Rechts(D): '+ self.exits[len(self.exits)-1].name + '\n')
        else:
            print("Rechts(D): Muur \n")
            self.exits.append("Muur")



    def describe(self):
        if len(self.exits):
            print('Je bent nu in de ' + self.name + '. Je ziet een '+ self.items[0].item_name + ' liggen.') # Maak grammatica correct bij alle kamers!
            vraag = input('Wil je dit meenemen(y/n): ')
            if vraag == 'y':
                item = self.items[0]
                self.items.remove(self.items[0])
                return(item)

            else:
                return(0)
        else:
            print('Je bent nu in de ' + self.name + '. De kamer lijkt leeg. Wil je verder(V) gaan of nog even zoeken(Z)')
            keuze = input('(V/Z): ')






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
                room.x = i
                room.y = j
                print(room.x)
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
        #room = person.get_current_room(self, x,y)
        #print(room)



class Player:
    def __init__(self):
        self.inventory = []
        self.name =  input("Hoe heet je: ")
        print("Hoi "+ self.name + '!')
        self.current_room = 'I'

    def goto_room(self):
        self.current_room.add_exit()
        door = 'ja'
        while door == 'ja':
            lopen = input("Waar wil je heen(W/A/S/D): ")
            if lopen == 'W' and self.current_room.exits[0] != 'Muur':
                self.set_current_room(self.current_room.exits[0])
                #self.current_room = self.current_room.exits[0]
                door = 'nee'
            elif lopen == 'A' and self.current_room.exits[1] != 'Muur':
                self.set_current_room(self.current_room.exits[1])
                #self.current_room = self.current_room.exits[1]
                door = 'nee'
            elif lopen == 'S' and self.current_room.exits[2] != 'Muur':
                self.set_current_room(self.current_room.exits[2])
                #self.current_room = self.current_room.exits[2]
                door = 'nee'
            elif lopen == 'D' and self.current_room.exits[3] != 'Muur':
                self.set_current_room(self.current_room.exits[3])
                #self.current_room = self.current_room.exits[3]
                door = 'nee'
            else:
                print("Je hebt een verkeerde weg gekozen of iets verkeerds ingevuld. \nProbeer het opnieuw.")
            

    def set_current_room(self, room):
        self.current_room = room
        item = self.current_room.describe()
        if item != 0:
            self.pick_up(item)


    def get_current_room(self, world, x, y):
        room = world.world[x][y]
        return(room)

    def pick_up(self, item):
        self.inventory.append(item)
        self.print_inv()

    def print_inv(self):
        print('Appels: '+ str(self.inventory.count(appel)))
        print('Brood: '+ str(self.inventory.count(brood)))
        print('Zwaarden: '+ str(self.inventory.count(zwaard)))
        print('Pijl en Boog: '+ str(self.inventory.count(boog)))
        print('Zilvere sleutels: '+ str(self.inventory.count(sleutel_zilver)))
        print('Goude sleutels: '+ str(self.inventory.count(sleutel_goud)))



class Controller:
    def __init__(self):
        self.play_game()

    def play_game(self):
        person = Player()
        mana = World("Mana")
        mana.create_world(person)
        keuze = 'L'
        while keuze != 'S':
            clear_screen()
            print('Je bent nu in de ' + person.current_room.name)
            print('\nLopen: L \nInventory bekijken: I \nHonger bekijken: H \nStoppen: S')
            keuze = input("Kies(L/I/H): ")
            clear_screen()
            if keuze == 'L':
                person.goto_room()
                print('')
            elif keuze == 'I':
                person.print_inv()
            elif keuze == 'H':
                print('H')
            
            




class Item:
    def __init__(self, _name, _itemtype):
        self.item_name = _name
        self.item_type = _itemtype


def clear_screen():
    #os.system("cls" if os.name == "nt" else "clear")
    print('\n\n\n\n\n\n\n\n\n\n\n') #Tijdelijke oplossing



#Items in het spel
appel = Item('Appel', 'eten')
brood = Item('Brood', 'eten')
zwaard = Item('Zwaard', 'wapen')
boog = Item('Pijl en Boog', 'wapen')
sleutel_goud = Item('Gouden Sleutel', 'sleutel')
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel')

speel = Controller()

import random

class Room:
    def __init__(self, _room_name, _world, _item):
        self.exits = []
        self.items = []
        #self.items.append(_item)
        self.world = _world
        self.name = _room_name
        self.x = 0
        self.y = 0
        self.add_item(_item)
        
    def add_item(self, item):
        self.items.append(item)
        


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
        #print(len(self.items))
        if len(self.items) >= 1:
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
            if keuze == 'Z':
                print('De kamer is nog steeds leeg')
            return(0)






class World: #Maakt een random wereld
    def __init__(self, _name):

        self.world = [['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.'],
                      ['.','.','.','.']]
        self.name = _name
        self.poss_items = []
        self.rooms = []

    def create_world(self, person):
        
        for a in range(6):
            self.poss_items.append(appel)
        for b in range(6):
            self.poss_items.append(brood)
        self.poss_items.append(zwaard)
        self.poss_items.append(boog)
        self.poss_items.append(sleutel_goud)
        self.poss_items.append(sleutel_zilver)
        
        
        
        
        #Voegt alle kamers toe
        #Zorg dat hight * width even is als het aantal kamers
        item = self.random_item()
        keuken = Room('keuken', self, item)
        self.add_room(keuken)
        item = self.random_item()
        woonkamer = Room('woonkamer', self, item)
        self.add_room(woonkamer)
        item = self.random_item()
        eetkamer = Room('eetkamer', self, item)
        self.add_room(eetkamer)
        item = self.random_item()
        badkamer = Room('badkamer', self, item)
        self.add_room(badkamer)
        item = self.random_item()
        gang = Room('gang', self, item)
        self.add_room(gang)
        item = self.random_item()
        balkon = Room('balkon', self, item) #!
        self.add_room(balkon)
        item = self.random_item()
        tuin = Room('tuin', self, item)
        self.add_room(tuin)
        item = self.random_item()
        bibliotheek = Room('bibliotheek', self, item)
        self.add_room(bibliotheek)
        item = self.random_item()
        slaapkamer = Room('slaapkamer', self, item)
        self.add_room(slaapkamer)
        item = self.random_item()
        hobbykamer = Room('hobbykamer', self, item)
        self.add_room(hobbykamer)
        item = self.random_item()
        fitnessruimte = Room('fitnessruimte', self, item)
        self.add_room(fitnessruimte)
        item = self.random_item()
        studeerkamer = Room('studeerkamer', self, item)
        self.add_room(studeerkamer)
        item = self.random_item()
        serre = Room('serre', self, item)
        self.add_room(serre)
        item = self.random_item()
        garage = Room('garage', self, item)
        self.add_room(garage)
        item = self.random_item()
        kelder = Room('kelder', self, item) #!
        self.add_room(kelder)
        item = self.random_item()
        zolder = Room('zolder', self, item) #!
        self.add_room(zolder)
        

        for i in range(hight):
            for j in range(width):
                room = random.choice(self.rooms)
                self.world[i][j] = room
                room.x = i
                room.y = j
                self.rooms.remove(room)

        self.first_room(person)
        
    def random_item(self):
        item = random.choice(self.poss_items)
        self.poss_items.remove(item)
        return(item)


    def add_room(self, _new_room):
        self.rooms.append(_new_room)


    def first_room(self, person):
        x = random.randint(0, width-1)
        y = random.randint(0, hight-1)

        firstroom = self.world[x][y]
        person.set_current_room(firstroom)



class Player: #Lopen en de inventory
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
                self.kijken_lopen()
                door = 'nee'
            elif lopen == 'A' and self.current_room.exits[1] != 'Muur':
                self.set_current_room(self.current_room.exits[1])
                self.kijken_lopen()
                door = 'nee'
            elif lopen == 'S' and self.current_room.exits[2] != 'Muur':
                self.set_current_room(self.current_room.exits[2])
                self.kijken_lopen()
                door = 'nee'
            elif lopen == 'D' and self.current_room.exits[3] != 'Muur':
                self.set_current_room(self.current_room.exits[3])
                self.kijken_lopen()
                door = 'nee'
            else:
                print("Je hebt een verkeerde weg gekozen of iets verkeerds ingevuld. \nProbeer het opnieuw.")
            

    def set_current_room(self, room):
        self.current_room = room
        
                
    def kijken_lopen(self):
        print('Wil je in deze kamer voor spullen kijken(K) of verder lopen(L): ')
        door = input('(K/L): ')
        if door == 'K':
            item = self.current_room.describe()
            if item != 0:
                self.pick_up(item)


    def get_current_room(self, world, x, y):
        room = world.world[x][y]
        return(room)

    def pick_up(self, item):
        self.inventory.append(item)
        #self.print_inv()

    def print_inv(self):
        print('Appels: '+ str(self.inventory.count(appel)))
        print('Brood: '+ str(self.inventory.count(brood)))
        print('Zwaarden: '+ str(self.inventory.count(zwaard)))
        print('Pijl en Boog: '+ str(self.inventory.count(boog)))
        print('Zilvere sleutels: '+ str(self.inventory.count(sleutel_zilver)))
        print('Goude sleutels: '+ str(self.inventory.count(sleutel_goud)))
        verder = input('Klik enter om verder te gaan...')



class Controller: # Begint het spel en laat het menu zien
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
            print('\nLopen: L \nInventory bekijken: I \nKamer bekijken: K \nHonger bekijken: H \nStoppen: S')
            keuze = input("Kies(L/I/K/H/S): ")
            clear_screen()
            if keuze == 'L':
                person.goto_room()
                print('')
            elif keuze == 'I':
                person.print_inv()
            elif keuze == 'K':
                person.kijken_lopen()
            elif keuze == 'H':
                print('H')
            elif keuze == 'S':
                print('Doei doei')
            else:
                print('Je hebt iets verkeerd getypt, probeer het opnieuw.')
            
            if sleutel_goud in person.inventory:
                keuze = 'S'
                print("Je hebt de goude sleutel gevonden! Je hebt gewonnen")
                    




class Item: #Geeft de items een naam en een soort
    def __init__(self, _name, _itemtype):
        self.item_name = _name
        self.item_type = _itemtype


def clear_screen(): #Maakt het scherm leeg
    #os.system("cls" if os.name == "nt" else "clear")
    print('\n\n\n\n\n\n\n\n\n\n\n') #Tijdelijke oplossing



#Items in het spel


#Hoogte en Breedte van de wereld
hight = 4
width = 4

#Maakt de Items
appel = Item('Appel', 'eten')
brood = Item('Brood', 'eten')
zwaard = Item('Zwaard', 'wapen')
boog = Item('Pijl en Boog', 'wapen')
sleutel_goud = Item('Gouden Sleutel', 'sleutel')
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel')

#Start het spel
speel = Controller()

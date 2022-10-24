import random

class Room:
    def __init__(self, _room_name, _world, _item, _monster):
        self.exits = []
        self.items = []
        #self.items.append(_item)
        self.world = _world
        self.name = _room_name
        self.x = 0
        self.y = 0
        self.add_item(_item)
        self.locked = self.locked_Room()
        self.monster = _monster
        print(self.monster)
        
    def locked_Room(self):
        if random.randint(0, 15) == 3:
            return True
        else:
            return True
        
    def add_item(self, item):
        self.items.append(item)
        
    def add_Enemy(self):
        #kies = random.randint(0, 1)
        monster = random.choice(MONSTERS)
        return(monster)
        #if kies == 0:
         #   return(Enemy())
            #self.monster = Enemy()
        #else:
         #   return(Enemy_Fire())
            #self.monster = Enemy_Fire()
        #print(self.monster)

    def add_exit(self):
        if self.x-1 >= 0:
            self.exits.append(self.world.world[self.x-1][self.y])
            print_header('Voor(W): '+ self.exits[len(self.exits)-1].name)
        else:
            print_header("Voor(W): Muur")
            self.exits.append("Muur")
        if self.y-1 >= 0:
            self.exits.append(self.world.world[self.x][self.y-1])
            print_regel('Links(A): '+ self.exits[len(self.exits)-1].name)
        else:
            print_regel("Links(A): Muur")
            self.exits.append("Muur")
        if self.x+1 <= hight-1:
            self.exits.append(self.world.world[self.x+1][self.y])
            print_regel('Achter(S): '+ self.exits[len(self.exits)-1].name)
        else:
            print_regel("Achter(S): Muur")
            self.exits.append("Muur")
        if self.y+1 <= width-1:
            self.exits.append(self.world.world[self.x][self.y+1])
            print_footer('Rechts(D): '+ self.exits[len(self.exits)-1].name)
        else:
            print_footer("Rechts(D): Muur")
            self.exits.append("Muur")

        
    
    def describe(self):
        if self.locked == True:
            print_header('De deur zit op slot je hebt een zilvere sleutel nodig om hem te openen.')
            if sleutel_zilver in person.inventory:
                print_footer_los()
                door = input('Wil je de zilvere sleutel gebruiken(y/n): ')
                if door == 'y':
                    self.locked = False
                    print_regel('De kamer is open!')
                    enter()
            else:
                print_footer('Je hebt geen zilvere sleutels, vindt er eentje!')
                enter()
                    
        if len(self.items) >= 1 and self.locked == False:
            print_header('Je ziet in de ' + self.name + ' een '+ self.items[0].item_name + ' liggen.')# Maak grammatica correct bij alle kamers!
            print_regel('Er staat een ' + self.monster.name + ' voor.')
            print_regel('')
            print_footer('Monster: '+ str(self.monster.life) + ' - Jij: ' + str(person.life))
            #print(self.monster.life)
            vraag = input('Wil je het '+ self.monster.name +' aanvallen(y/n): ')
            door = 'a'
            
            if vraag == 'y':
                while self.monster.life > 0 and person.life > 0 and door != 'v':
                    self.monster.attack()
                    if self.monster.life > 0 and person.life > 0:
                        vraag = input('Wil je verder met aanvallen(a) of wil je vluchten(v) (a/v): ')
                        if vraag == 'a':
                            clear_screen()
                            #return(0)
                        elif vraag == 'v':
                            door = 'v'
                if person.life <= 0:
                    
                    print_regel_los('Je bent dood')
                    #print_footer_los()
                    #print(Controller.keuze)
                    #Controller.keuze = 'S'
                    return('S')
                
                elif self.monster.life <= 0:
                    print_regel_los('Je hebt het monster verslagen!')
                    #print_footer_los()
                    #enter()
                    vraag2 = input('Wil je een ' + self.items[0].item_name + ' meenemen(y/n): ')
                    if vraag2 == 'y':
                        item = self.items[0]
                        self.items.remove(self.items[0])
                        return(item)
                    else:
                        return(0)

            else:
                return(0)
        elif len(self.items) <= 0:
            print_regel_los('Je bent nu in de ' + self.name + '. De kamer lijkt leeg. Wil je verder(V) gaan of nog even zoeken(Z)')
            #print_footer()
            keuze = input('(V/Z): ')
            if keuze == 'Z':
                print_regel_los('De kamer is nog steeds leeg')
            return(0)
            
            



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

    def create_world(self):
        
        for i in range(5):
            self.poss_items.append(appel)
        for i in range(5):
            self.poss_items.append(brood)
        self.poss_items.append(zwaard)
        self.poss_items.append(boog)
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
        monster8 = Enemy_Fire()
        monster9 = Enemy_Fire()
        monster10 = Enemy_Fire()
        monster11 = Enemy_Water()
        monster12 = Enemy_Water()
        monster13 = Enemy_Water()
        monster14 = Enemy_Plant()
        monster15 = Enemy_Plant()
        monster16 = Enemy_Plant()
        
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
        item = self.random_item()
        monster = self.random_enemy()
        keuken = Room('keuken', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        woonkamer = Room('woonkamer', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        eetkamer = Room('eetkamer', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        badkamer = Room('badkamer', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        gang = Room('gang', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        balkon = Room('balkon', self, item, monster) #!
        item = self.random_item()
        monster = self.random_enemy()
        tuin = Room('tuin', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        bibliotheek = Room('bibliotheek', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        slaapkamer = Room('slaapkamer', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        hobbykamer = Room('hobbykamer', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        fitnessruimte = Room('fitnessruimte', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        studeerkamer = Room('studeerkamer', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        serre = Room('serre', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        garage = Room('garage', self, item, monster)
        item = self.random_item()
        monster = self.random_enemy()
        kelder = Room('kelder', self, item, monster) #!
        item = self.random_item()
        monster = self.random_enemy()
        zolder = Room('zolder', self, item, monster) #!
        
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
        self.add_room(fitnessruimte)
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

        self.first_room()
        
    def random_item(self):
        item = random.choice(self.poss_items)
        self.poss_items.remove(item)
        return(item)
    
    def random_enemy(self):
        enemy = random.choice(self.poss_Enemy)
        self.poss_Enemy.remove(enemy)
        return(enemy)


    def add_room(self, _new_room):
        self.rooms.append(_new_room)


    def first_room(self):
        x = random.randint(0, width-1)
        y = random.randint(0, hight-1)

        firstroom = self.world[x][y]
        person.set_current_room(firstroom)



class Player: #Lopen en de inventory
    def __init__(self):
        self.inventory = [sleutel_zilver]
        self.current_room = 'I'
        self.life = LEVENS_SPELER
        self.name =  input("Hoe heet je: ")
        print_header("Hoi "+ self.name + '!')
        

    def goto_room(self):
        self.current_room.add_exit()
        door = 'ja'
        while door == 'ja':
            lopen = input("Waar wil je heen(W/A/S/D): ")
            if lopen == 'W' and self.current_room.exits[0] != 'Muur':
                self.set_current_room(self.current_room.exits[0])
                #self.kijken_lopen()
                door = 'nee'
            elif lopen == 'A' and self.current_room.exits[1] != 'Muur':
                self.set_current_room(self.current_room.exits[1])
                #self.kijken_lopen()
                door = 'nee'
            elif lopen == 'S' and self.current_room.exits[2] != 'Muur':
                self.set_current_room(self.current_room.exits[2])
                #self.kijken_lopen()
                door = 'nee'
            elif lopen == 'D' and self.current_room.exits[3] != 'Muur':
                self.set_current_room(self.current_room.exits[3])
                #self.kijken_lopen()
                door = 'nee'
            else:
                print_regel_los("Je hebt een verkeerde weg gekozen of iets verkeerds ingevuld. \nProbeer het opnieuw.")
            

    def set_current_room(self, room):
        self.current_room = room
        
                
    def kijken(self):
        item = self.current_room.describe()
        if item == 'S':
            return('S')
        else: #item != 0
            self.pick_up(item)
            return('K')


    def get_current_room(self, world, x, y):
        room = world.world[x][y]
        return(room)

    def pick_up(self, item):
        self.inventory.append(item)

    def print_inv(self):
        print_header('Appels: '+ str(self.inventory.count(appel)))
        print_regel('Brood: '+ str(self.inventory.count(brood)))
        print_regel('Zwaarden: '+ str(self.inventory.count(zwaard)))
        print_regel('Pijl en Boog: '+ str(self.inventory.count(boog)))
        print_regel('Zilvere sleutels: '+ str(self.inventory.count(sleutel_zilver)))
        print_footer('Goude sleutels: '+ str(self.inventory.count(sleutel_goud)))
        enter()
        
    def print_life(self):
        print_regel_los('Je hebt nog ' + str(self.life) + ' levens!')
        enter()



class Controller: # Begint het spel en laat het menu zien
    def __init__(self):
        self.keuze = 'L'

    def play_game(self):
        mana = World("Mana")
        mana.create_world()
        while self.keuze != 'S':
            clear_screen()
            #print(self.keuze)
            print_menu()
            #print('Je bent nu in de ' + person.current_room.name)
            #print('\nLopen: L \nInventory bekijken: I \nKamer bekijken: K \nHonger bekijken: H \nStoppen: S')
            self.keuze = input("Kies(K/L/I/E/S): ")
            clear_screen()
            if self.keuze == 'L':
                person.goto_room()
                print('')
            elif self.keuze == 'I':
                person.print_inv()
            elif self.keuze == 'K':
                self.keuze = person.kijken()
            elif self.keuze == 'E':
                person.print_life()
            elif self.keuze == 'S':
                print_regel_los('Doei doei')
            else:
                print_regel_los('Je hebt iets verkeerd getypt, probeer het opnieuw.')
            
            if person.inventory.count(sleutel_goud) == 3: #Als je 3 sleutels hebt dan win je
                self.keuze = 'S'
                print_regel_los("Je hebt de goude sleutel gevonden! Je hebt gewonnen")
                    




class Item: #Geeft de items een naam en een soort
    def __init__(self, _name, _itemtype, _damage):
        self.item_name = _name
        self.item_type = _itemtype
        self.damage = _damage
        

class Enemy:
    def __init__(self):
        self.life = LEVENS_MONSTER
        self.max_schade = DAMAGE_MONSTER
        self.name = 'Monster'

    def attack(self):
        #print("Ouch!")
        self.attacked()
        
        schade_person = random.randint(0,self.max_schade)
        print_regel('Jij: -' + str(schade_person))
        person.life -= schade_person
        #self.attacked()
        print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(person.life))
        #print('Je hebt er nog '+ str(person.life) + ' over.')
        #print("Je valt het monster aan. Hij heeft nog " + str(self.life) + " levens over")
        
    def attacked(self):
        wapen = self.wapen()
        #if wapen == zwaard:
        if wapen == 0:
            self.life -= 3
            print_header('Monster: -3')
        else:
            self.life -= wapen.damage
            print_header('Monster: -' + str(wapen.damage))
        
            
    def wapen(self):
        if zwaard in person.inventory:
            keuze = input('Wil je het zwaard gebruiken om aan te vallen(y/n): ')
            if keuze == 'y':
                print('Oke laten we aan vallen met het zwaard')
                return(zwaard)
            if boog in person.inventory:
                keuze = input('Wil je de pijl en boog gebruiken om aan te vallen(y/n): ')
                if keuze == 'y':
                    print('Oke laten we aan vallen met de pijl en boog')
                    return(boog)
                else:
                    print('Je gaat je vuisten gebruiken')
                    return(0)
            else:
                print('Je gaat je vuisten gebruiken')
                return(0)
        elif boog in person.inventory:
            keuze = input('Wil je de pijl en boog gebruiken om aan te vallen(y/n): ')
            if keuze == 'y':
                print('Oke laten we aan vallen met de pijl en boog')
                return(boog)
            else:
                print('Je gaat je vuisten gebruiken')
                return(0)
        else:
            print('Je gaat je vuisten gebruiken')
            return(0)
        

    def checklife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " lifes left.")

    def heal(self):
        self.life += 2
    
    
class Enemy_Fire(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.life = LEVENS_VUURMONSTER
        self.max_schade = DAMAGE_VUURMONSTER
        self.name = 'Vuur Monster'
        
    def attack(self):
        if random.randint(0, 3) == 1:
            print('Het monster spuwt vuur naar je toe, het kost je 6 levens.')
            #schade_person = 6
            person.life -= 6
            Enemy.attacked(self)
            print_regel('Jij: -6')
            print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(person.life))
        
        else:
            Enemy.attack(self)
            
class Enemy_Water(Enemy):
    def __init__(self):
        #super.__init__
        Enemy.__init__(self)
        self.life = LEVENS_VUURMONSTER
        self.max_schade = DAMAGE_VUURMONSTER
        self.name = 'Water Monster'
        
    def attack(self):
        if random.randint(0, 3) == 1:
            print('Het monster maakt een waterkolk om je heen dit kost je 6 levens.')
            #schade_person = 6
            person.life -= 6
            Enemy.attacked(self)
            print_regel('Jij: -6')
            print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(person.life))
        
        else:
            Enemy.attack(self)
            
class Enemy_Plant(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.life = LEVENS_VUURMONSTER
        self.max_schade = DAMAGE_VUURMONSTER
        self.name = 'Plant Monster'
        
    def attack(self):
        if random.randint(0, 3) == 1:
            print('Het monster geeft je een klap met een tak dit kost je 6 levens.')
            #schade_person = 6
            person.life -= 6
            Enemy.attacked(self)
            print_regel('Jij: -6')
            print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(person.life))
        
        else:
            Enemy.attack(self)
            
def print_footer(zin):
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(zin))
    print("="*(SCHERMBREEDTE))
    
def print_footer_los():
    print("="*(SCHERMBREEDTE))
    
def print_header(zin):
    print("="*(SCHERMBREEDTE))
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(zin))

  
def print_menu():
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    print_regel("Huidige locatie: " + person.current_room.name)
    #print_regel("Je gebruikt nu de woordenlijst: " + woordenlijst)
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    print_regel("Kamer bekijken -- K")
    print_regel("Lopen -- L")
    print_regel("Inventory bekijken -- I")
    print_regel("Levens bekijken -- E")
    print_regel("Stoppen -- S")
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    
def print_regel(regel):
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))

def print_regel_los(regel):
    print("="*(SCHERMBREEDTE))
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))
    print("="*(SCHERMBREEDTE))


def clear_screen(): #Maakt het scherm leeg
    #os.system("cls" if os.name == "nt" else "clear")
    print('\n\n\n\n\n\n\n\n\n\n\n') #Tijdelijke oplossing

def enter():
    verder = input('Klik enter om verder te gaan...')


#Hoogte en Breedte van de wereld
hight = 4
width = 4
LEVENS_SPELER = 20
LEVENS_MONSTER = 10
LEVENS_VUURMONSTER = 15
DAMAGE_MONSTER = 4
DAMAGE_VUURMONSTER = 6
SCHERMBREEDTE = 80
HELFT_SCHERMBREEDTE = SCHERMBREEDTE/2
MAX_WOORD_LENGTE = 20

MONSTERS = [Enemy_Plant(), Enemy_Water(), Enemy_Fire(), Enemy()]

#Maakt de Items
appel = Item('Appel', 'eten', 0)
brood = Item('Brood', 'eten', 0)
zwaard = Item('Zwaard', 'wapen', 6)
boog = Item('Pijl en Boog', 'wapen', 8)
sleutel_goud = Item('Gouden Sleutel', 'sleutel', 0)
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel', 0)

#Maakt speler en start het spel
person = Player()
speel = Controller()
speel.play_game()



#Ideeën
# - Meerdere Enemys verschilende krachten -
#		Normaal, Vuur, Water, Plant
# - Levens Potion
# - 


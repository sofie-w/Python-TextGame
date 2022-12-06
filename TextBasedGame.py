import random

class Room:
    def __init__(self, _room_name, _world, _item = 'None', _monster = 'None'):
        self.exits = []
        self.items = []
        self.world = _world
        self.name = _room_name
        self.x = 0
        self.y = 0
        self.add_item(_item)
        self.locked = self.locked_Room()
        self.monster = _monster
        
    def locked_Room(self):
        if random.randint(0, 15) == 3:
            return True
        else:
            return False
        
    def add_item(self, item):
        self.items.append(item)
        
    def add_Enemy(self):
        monster = random.choice(MONSTERS)
        return(monster)

    def add_exit(self):

        if self.x-1 >= 0:
            self.exits.append(self.world.world[self.x-1][self.y])
        else:
            self.exits.append(self.world.muur)
        if self.y-1 >= 0:
            self.exits.append(self.world.world[self.x][self.y-1])
        else:
            self.exits.append(self.world.muur)
        if self.x+1 <= hight-1:
            self.exits.append(self.world.world[self.x+1][self.y])
        else:
            self.exits.append(self.world.muur)
        if self.y+1 <= width-1:
            self.exits.append(self.world.world[self.x][self.y+1])
        else:
            self.exits.append(self.world.muur)

        
    
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
            vraag = input('Wil je het '+ self.monster.name +' aanvallen(y/n): ')
            door = 'a'
            
            if vraag == 'y':
                while self.monster.life > 0 and person.life > 0 and door != 'v':
                    self.monster.attack()
                    if self.monster.life > 0 and person.life > 0:
                        vraag = input('Wil je verder met aanvallen(a) of wil je vluchten(v) (a/v): ')
                        if vraag == 'a':
                            clear_screen()
                        elif vraag == 'v':
                            door = 'v'
                if person.life <= 0:
                    
                    print_regel_los('Je bent dood')
                    return('S')
                
                elif self.monster.life <= 0:
                    print_regel_los('Je hebt het monster verslagen! Je hebt ' + str(self.monster.waarde) + ' coins verdiend.')
                    person.geld += self.monster.waarde
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
        self.muur = Room('muur', self)

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
                
        for i in range(hight):
            for j in range(width):
                self.world[i][j].add_exit()
                

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
        self.inventory = []
        self.current_room = 'I'
        self.life = LEVENS_SPELER
        self.geld = 30
        #self.name =  input("Hoe heet je: ")
        #print_header("Hoi "+ self.name + '!')
        

    def goto_room(self):
        door = 'ja'
        while door == 'ja':
            print_world_rand()
            lopen = input("Waar wil je heen(W/A/S/D): ")
            if lopen == 'W' or lopen == 'w':
                if self.current_room.exits[0].name != 'muur':
                    self.set_current_room(self.current_room.exits[0])
                    door = 'nee'
                else:
                    clear_screen()
                    print_regel_los("Er zit een muur...")
                
            elif lopen == 'A' or lopen == 'a':
                if self.current_room.exits[1].name != 'muur':
                    self.set_current_room(self.current_room.exits[1])
                    door = 'nee'
                else:
                    clear_screen()
                    print_regel_los("Er zit een muur...")
                    
            elif lopen == 'S' or lopen == 's':
                if self.current_room.exits[2].name != 'muur':
                    self.set_current_room(self.current_room.exits[2])
                    door = 'nee'
                else:
                    clear_screen()
                    print_regel_los("Er zit een muur...")
            
            elif lopen == 'D' or lopen == 'd':
                if self.current_room.exits[3].name != 'muur':
                    self.set_current_room(self.current_room.exits[3])
                    door = 'nee'
                else:
                    clear_screen()
                    print_regel_los("Er zit een muur...")
            else:
                clear_screen()
                print_regel_los("Je hebt iets verkeerds ingevuld. Probeer het opnieuw.")
            

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
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        print_regel_inv('Eten', 'Aantal', 'Wapens', 'Aantal')
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        for i in range(int(len(spullen)/2)):
            print_regel_inv(spullen[i].item_name, str(self.inventory.count(spullen[i])), spullen[i+5].item_name, str(self.inventory.count(spullen[i+5])))
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        enter()
        
    
    def eten(self):
        print_header('Je hebt nu ' + str(person.life) + ' levens.')
        print_regel_inv('Eten', 'Aantal', 'Levens', 'Letter')
        for i in range(int(len(spullen)/2)):
            print_regel_inv(spullen[i].item_name, str(self.inventory.count(spullen[i])), str(spullen[i].damage_levens) + ' levens', spullen[i].letter)
        print_footer_los()
        
        keuze = input('Wat wil je eten: ')
        for i in range(int(len(spullen)/2)):
            if keuze == spullen[i].letter:
                if self.inventory.count(spullen[i]) > 0:
                    self.inventory.remove(spullen[i])
                    self.life = self.life + spullen[i].damage_levens
                else:
                    clear_screen()
                    print_regel_los('Je hebt geen ' + spullen[i].item_name.lower() + '.')
                    enter()

        
class Winkel:      
    def laten_zien(self):
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        print_regel_winkel("Wat", "Letter", "Prijs")
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        appel.print_kopen()
        brood.print_kopen()
        taart.print_kopen()
        soep.print_kopen()
        ijs.print_kopen()
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        zwaard.print_kopen()
        boog.print_kopen()
        mes.print_kopen()
        knuppel.print_kopen()
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        keuze = input("Jouw geld: " + str(person.geld) + " \nWat wil je kopen: ")
        for i in range(len(spullen)):
            if spullen[i].letter == keuze:
                if spullen[i].prijs <= person.geld:
                    self.kopen(spullen[i])
                else:
                    print('Je hebt niet genoeg geld.')
                print(spullen[i].item_name)
            
    def kopen(self, item):
        person.geld -= item.prijs
        person.pick_up(item)
        
        
        


class Controller: # Begint het spel en laat het menu zien
    def __init__(self):
        self.keuze = 'L'

    def play_game(self):
        mana = World("Mana")
        mana.create_world()
        while self.keuze != 'S':
            clear_screen()
            print_menu()
            self.keuze = input("Kies(K/L/I/E/W/S): ")
            clear_screen()
            if self.keuze == 'L' or self.keuze == 'l':
                person.goto_room()
                print('')
            elif self.keuze == 'I' or self.keuze == 'i':
                person.print_inv()
            elif self.keuze == 'K' or self.keuze == 'k':
                self.keuze = person.kijken()
            elif self.keuze == 'E' or self.keuze == 'e':
                person.eten()
            elif self.keuze == 'W' or self.keuze == 'w':
                winkel.laten_zien()
            elif self.keuze == 'S' or self.keuze == 's':
                print_regel_los('Doei doei')
            else:
                print_regel_los('Je hebt iets verkeerd getypt, probeer het opnieuw.')
            
            if person.inventory.count(sleutel_goud) == 3: #Als je 3 sleutels hebt dan win je
                self.keuze = 'S'
                print_regel_los("Je hebt de goude sleutel gevonden! Je hebt gewonnen")
                    




class Item: #Geeft de items een naam en een soort
    def __init__(self, _name, _itemtype, _damage_levens, _letter, _prijs):
        self.item_name = _name
        self.item_type = _itemtype
        self.damage_levens = _damage_levens
        self.letter = _letter
        self.prijs = _prijs
        
    def print_kopen(self):
        print_regel_winkel(self.item_name + " +" + str(self.damage_levens), self.letter, str(self.prijs))
        

class Enemy:
    def __init__(self):
        self.life = LEVENS_MONSTER
        self.max_schade = DAMAGE_MONSTER
        self.waarde = WAARDE_MONSTER
        self.name = 'Monster'

    def attack(self):
        self.attacked()
        
        schade_person = random.randint(0,self.max_schade)
        print_regel('Jij: -' + str(schade_person))
        person.life -= schade_person
        print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(person.life))
        
    def attacked(self):
        wapen = self.wapen()
        if wapen == 0:
            self.life -= 3
            print_header('Monster: -3')
        else:
            self.life -= wapen.damage_levens
            print_header('Monster: -' + str(wapen.damage_levens))
        
            
    def wapen(self):
        if zwaard in person.inventory:
            keuze = input('Wil je het zwaard gebruiken om aan te vallen(y/n): ')
            if keuze == 'y':
                print('Wapen: Zwaard')
                return(zwaard)
            if boog in person.inventory:
                keuze = input('Wil je de pijl en boog gebruiken om aan te vallen(y/n): ')
                if keuze == 'y':
                    print('Wapen: Pijl en boog')
                    return(boog)
                else:
                    #print('Je gaat je vuisten gebruiken')
                    return(0)
            else:
                #print('Je gaat je vuisten gebruiken')
                return(0)
        elif boog in person.inventory:
            keuze = input('Wil je de pijl en boog gebruiken om aan te vallen(y/n): ')
            if keuze == 'y':
                print('Wapen: Pijl en boog')
                return(boog)
            else:
                #print('Je gaat je vuisten gebruiken')
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
        self.life = LEVENS_SPECIAALMONSTER
        self.max_schade = DAMAGE_SPECIAALMONSTER
        self.waarde = WAARDE_SPECIAALMONSTER
        self.name = 'Vuur Monster'
        
    def attack(self):
        if random.randint(0, 3) == 1:
            print('Het monster spuwt vuur naar je toe, het kost je 6 levens.')
            person.life -= 6
            Enemy.attacked(self)
            print_regel('Jij: -6')
            print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(person.life))
        
        else:
            Enemy.attack(self)
            
class Enemy_Water(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.life = LEVENS_SPECIAALMONSTER
        self.max_schade = DAMAGE_SPECIAALMONSTER
        self.waarde = WAARDE_SPECIAALMONSTER
        self.name = 'Water Monster'
        
    def attack(self):
        if random.randint(0, 3) == 1:
            print('Het monster maakt een waterkolk om je heen dit kost je 6 levens.')
            person.life -= 6
            Enemy.attacked(self)
            print_regel('Jij: -6')
            print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(person.life))
        
        else:
            Enemy.attack(self)
            
class Enemy_Plant(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.life = LEVENS_SPECIAALMONSTER
        self.max_schade = DAMAGE_SPECIAALMONSTER
        self.waarde = WAARDE_SPECIAALMONSTER
        self.name = 'Plant Monster'
        
    def attack(self):
        if random.randint(0, 3) == 1:
            print('Het monster geeft je een klap met een tak dit kost je 6 levens.')
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
    print(("| {:" + str(int(SCHERMBREEDTE*(1/2)) - 3)+ "}  {:^" + str(int(SCHERMBREEDTE*(1/4)) - 2)+ "} {:^" + str(int(SCHERMBREEDTE*(1/4)) - 2)+ "} |").format("Huidige locatie: " + person.current_room.name, "Levens: " + str(person.life), 'Geld: ' + str(person.geld)))
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    print_regel("Kamer bekijken -- K")
    print_regel("Lopen -- L")
    print_regel("Inventory bekijken -- I")
    print_regel("Eten -- E")
    print_regel("Winkel -- W")
    print_regel("Stoppen -- S")
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    
def print_regel(regel):
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))

def print_regel_los(regel):
    print("="*(SCHERMBREEDTE))
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))
    print("="*(SCHERMBREEDTE))
    
def print_regel_dubbel(zin1, zin2):
    print(("| {:"+ str(int((SCHERMBREEDTE/2))-2) +"}{:^"+ str(int((SCHERMBREEDTE/2))-1) +"}|").format(zin1, zin2))
    
def print_regel_winkel(regel1, regel2, regel3):
    print(("| {:" + str(int(SCHERMBREEDTE*(1/2)) - 3)+ "} | {:^" + str(int(SCHERMBREEDTE*(1/4)) - 4)+ "} |{:^" + str(int(SCHERMBREEDTE*(1/4)) - 2)+ "} |").format(regel1, regel2, regel3))
    
def print_regel_inv(regel1, regel2, regel3, regel4):
    print(("| {:" + str(int(SCHERMBREEDTE*(1/3)) - 1)+ "}|{:^" + str(int(SCHERMBREEDTE*(1/6)) - 1)+ "}| {:" + str(int(SCHERMBREEDTE*(1/3)) - 2)+ "}|{:^" + str(int(SCHERMBREEDTE*(1/6)) - 1)+ "}|").format(regel1, regel2, regel3, regel4))

def print_world_rand():
    print(16*' ' + '+' + 15*'-' + '+')
    print((16*' ' + "|{:^" + str(15)+ "}|").format(person.current_room.exits[0].name))
    print('+' + 15*'-' + '+' + 6*'-' + ' ↑ ' + 6*'-' + '+' + 15*'-' + '+')
    print( ("|{:^" + str(15)+ "}←{:^" + str(15)+ "}→{:^" + str(15)+ "}|").format(person.current_room.exits[1].name, person.current_room.name, person.current_room.exits[3].name)  )
    print('+' + 15*'-' + '+' + 6*'-' + ' ↓ ' + 6*'-' + '+' + 15*'-' + '+')
    print((16*' ' + "|{:^" + str(15)+ "}|").format(person.current_room.exits[2].name))
    print(16*' ' + '+' + 15*'-' + '+\n')


def clear_screen(): #Maakt het scherm leeg
    #os.system("cls" if os.name == "nt" else "clear")
    print('\n\n\n\n\n\n\n\n\n\n\n') #Tijdelijke oplossing

def enter():
    verder = input('Klik enter om verder te gaan...')


#Hoogte en Breedte van de wereld
hight = 4
width = 4
LEVENS_SPELER = 50
LEVENS_MONSTER = 10
LEVENS_SPECIAALMONSTER = 15
DAMAGE_MONSTER = 4
DAMAGE_SPECIAALMONSTER = 6
WAARDE_MONSTER = 5
WAARDE_SPECIAALMONSTER = 10
SCHERMBREEDTE = 80
HELFT_SCHERMBREEDTE = SCHERMBREEDTE/2
MAX_WOORD_LENGTE = 20

MONSTERS = [Enemy_Plant(), Enemy_Water(), Enemy_Fire(), Enemy()]

#Maakt de Items
appel = Item('Appel', 'eten', 3, 'A', 4)
brood = Item('Brood', 'eten', 7, 'B', 7)
taart = Item('Taart', 'eten', 10, 'T', 10)
soep = Item('Soep', 'eten', 15, 'S', 14)
ijs = Item('Ijs', 'eten', 20, 'I', 17)
handschoen = Item('Handschoen', 'wapen', 4, 'H', 8)
zwaard = Item('Zwaard', 'wapen', 6, 'Z', 15)
boog = Item('Pijl en Boog', 'wapen', 8, 'B', 20)
mes = Item('Mes', 'wapen', 15, 'M', 30)
knuppel = Item('Knuppel', 'wapen', 20, 'K', 45)


spullen = [appel, brood, taart, soep, ijs, handschoen, zwaard, boog, mes, knuppel]

sleutel_goud = Item('Gouden Sleutel', 'sleutel', 0, 'G', 0)
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel', 0, 'G', 0)

#Maakt speler en start het spel
winkel = Winkel()
person = Player()
speel = Controller()
speel.play_game()
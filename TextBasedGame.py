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
        #self.monster  = self.add_Enemy()
        
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
            if sleutel_zilver in persoon.inventory:
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
            print_regel('Er staat een ' + self.monster.soort + ' voor.')
            print_regel('')
            print_footer('Monster: '+ str(self.monster.life) + ' - Jij: ' + str(persoon.life))
            vraag = input('Wil je het '+ self.monster.soort +' aanvallen(y/n): ')
            door = 'a'
            
            if vraag == 'y':
                while self.monster.life > 0 and persoon.life > 0 and door != 'v':
                    self.monster.attack()
                    if self.monster.life > 0 and persoon.life > 0:
                        vraag = input('Wil je verder met aanvallen(a) of wil je vluchten(v) (a/v): ')
                        if vraag == 'a':
                            clear_screen()
                        elif vraag == 'v':
                            door = 'v'
                if persoon.life <= 0:
                    
                    print_regel_los('Je bent dood')
                    return('S')
                
                elif self.monster.life <= 0:
                    print_regel_los('Je hebt het monster verslagen! Je hebt ' + str(self.monster.waarde) + ' coins verdiend.')
                    persoon.geld += self.monster.waarde
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
        self.poss_items.append(pijl_boog)
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
        persoon.set_current_room(firstroom)
        

class Player: #Lopen en de inventory
    def __init__(self):
        self.inventory = []
        self.current_room = 'I'
        self.life = LEVENS_SPELER
        self.geld = BEGIN_GELD
        

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
        
        print_regel('Als je extra informatie wilt over het item type dan de eerste letter.')
        keuze = input('| Klik anders op enter... ')
        for i in range(len(spullen)):
            if keuze == spullen[i].letter:
                print('\n')
                spullen[i].uitleg_item()
                enter()
    
    def eten(self):
        print_header('Je hebt nu ' + str(persoon.life) + ' levens.')
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
        pijl_boog.print_kopen()
        mes.print_kopen()
        knuppel.print_kopen()
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        keuze = input("Jouw geld: " + str(persoon.geld) + " \nWat wil je kopen: ")
        for i in range(len(spullen)):
            if spullen[i].letter == keuze:
                if spullen[i].prijs <= persoon.geld:
                    self.kopen(spullen[i])
                else:
                    print('Je hebt niet genoeg geld.')
                print(spullen[i].item_name)
            
    def kopen(self, item):
        persoon.geld -= item.prijs
        persoon.pick_up(item)
        
        
        


class Controller: # Begint het spel en laat het menu zien
    def __init__(self):
        self.keuze = 'L'

    def play_game(self):
        mana = World("Mana")
        mana.create_world()
        self.uitleg()
        while self.keuze != 'S':
            clear_screen()
            print_menu()
            self.keuze = input("Kies(K/L/I/E/W/S): ")
            clear_screen()
            if self.keuze == 'L' or self.keuze == 'l':
                persoon.goto_room()
                print('')
            elif self.keuze == 'I' or self.keuze == 'i':
                persoon.print_inv()
            elif self.keuze == 'K' or self.keuze == 'k':
                self.keuze = persoon.kijken()
            elif self.keuze == 'E' or self.keuze == 'e':
                persoon.eten()
            elif self.keuze == 'W' or self.keuze == 'w':
                winkel.laten_zien()
            elif self.keuze == 'S' or self.keuze == 's':
                print_regel_los('Doei doei')
            else:
                print_regel_los('Je hebt iets verkeerd getypt, probeer het opnieuw.')
            
            if persoon.inventory.count(sleutel_goud) == 3: #Als je 3 sleutels hebt dan win je
                self.keuze = 'S'
                print_regel_los("Je hebt de goude sleutel gevonden! Je hebt gewonnen")
    
    def uitleg(self):
        print_header('Welkom bij ... ik zal je even uitleggen hoe dit spel werkt.')
        print_regel(' ')
        print_regel('Je komt in een huis terecht. In dit huis liggen 3 gouden sleutels verstopt.')
        print_regel('Je kan door het huis lopen, in elke kamer zal je een monster aantreffen.')
        print_regel('Het monster kan je verslaan door het gebruiken van je vuisten.')
        print_regel('Je kan ook betere wapens kopen.')
        print_regel('Hierdoor zal het verslaan van de monsters makkelijker worden.')
        print_regel('Door het vermoorden van de monsters kan je geld verdienden.')
        print_regel('Met dit geld kan je wapens en eten kopen.')
        print_regel('Door te eten zal je meer levens krijgen.')
        print_regel('Ook zijn er een paar kamers die op slot zitten.')
        print_regel('Daarvoor zal je een zilvere sleutel moeten vinden.')
        print_regel('Die liggen ook verstopt in het huis.')
        print_regel('')
        print_footer('- Veel succes!')
        enter()




class Item: #Geeft de items een naam en een soort
    def __init__(self, _name, _itemtype, _damage_levens, _letter, _prijs, _uitleg):
        self.item_name = _name
        self.item_type = _itemtype
        self.damage_levens = _damage_levens
        self.letter = _letter
        self.prijs = _prijs
        self.uitleg = _uitleg
        
    def print_kopen(self):
        print_regel_winkel(self.item_name + " +" + str(self.damage_levens), self.letter, str(self.prijs))
        
    def uitleg_item(self):
        print_regel(self.uitleg)



class Enemy:
    def __init__(self):
        self.life = LEVENS_MONSTER
        self.max_schade = DAMAGE_MONSTER
        self.waarde = WAARDE_MONSTER
        self.soort = 'monster'

    def attack(self):
        self.attacked()
        if random.randint(0,4) == 1:
            self.struikelen()
            print_regel('Hierdoor gaat zijn aanval fout.')
        else:
            schade_persoon = random.randint(0,self.max_schade)
            print_regel('Jij: -' + str(schade_persoon))
            persoon.life -= schade_persoon
        print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(persoon.life))
        
    def attacked(self):
        wapen = self.wapen()
        self.life -= wapen.damage_levens
        print_header('Monster: -' + str(wapen.damage_levens))
        
    def struikelen(self):
        fouten = ('Het monster probeert je aan te vallen maar hij struikeld over een bananenschil.',
                  'Terwijl het monster je aanvalt wordt hij afgeleid door een raar geluid.',
                  'Het monster schrikt zo van je dat hij omvalt.')
        print_regel(fouten[random.randint(0,len(fouten))])
        
            
    def wapen(self):
        clear_screen()
        wapens_inv = [vuisten]
        for i in range(len(wapens)):
            if wapens[i] in persoon.inventory:
                wapens_inv.append(wapens[i])
                
        print_header('Jouw wapens: ')
        for i in range(len(wapens_inv)):
            print_regel(wapens_inv[i].item_name + '(' + wapens_inv[i].letter + '): -' + str(wapens_inv[i].damage_levens))
        print_regel('')
        keuze = input('| Welke wil je gebruiken: ')
        clear_screen()
        for i in range(len(wapens_inv)):
            if keuze == wapens_inv[i].letter:
                return(wapens_inv[i])
            
            
class Special_Enemy(Enemy):
    def __init__(self, _soort, _aanval):
        Enemy.__init__(self)
        self.life = LEVENS_SPECIAALMONSTER
        self.max_schade = DAMAGE_SPECIAALMONSTER
        self.waarde = WAARDE_SPECIAALMONSTER
        self.soort = _soort
        self.aanval = _aanval
        
    def attack(self):
        if random.randint(0, 3) == 1:
            persoon.life -= 6
            Enemy.attacked(self)
            print_regel(self.aanval)
            print_regel('Jij: -6')
            print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(persoon.life))
        
        else:
            Enemy.attack(self)
           
def print_footer(zin):
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(zin))
    #print("="*(SCHERMBREEDTE))
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    
def print_footer_los():
    #print("="*(SCHERMBREEDTE))
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    
def print_header(zin):
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    #print("="*(SCHERMBREEDTE))
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(zin))

  
def print_menu():
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    print(("| {:" + str(int(SCHERMBREEDTE*(1/2)) - 3)+ "}  {:^" + str(int(SCHERMBREEDTE*(1/4)) - 2)+ "} {:^" + str(int(SCHERMBREEDTE*(1/4)) - 2)+ "} |").format("Huidige locatie: " + persoon.current_room.name, "Levens: " + str(persoon.life), 'Geld: ' + str(persoon.geld)))
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    print(("| {:" + str(int(SCHERMBREEDTE*(1/2)) - 2)+ "}{:>" + str(int(SCHERMBREEDTE*(1/2)) - 5)+ "}    |").format("Kamer bekijken -- K", "Gouden sleutels: " + str(persoon.inventory.count(sleutel_goud)) + "/3"))
    print(("| {:" + str(int(SCHERMBREEDTE*(1/2)) - 2)+ "}{:>" + str(int(SCHERMBREEDTE*(1/2)) - 5)+ "}    |").format("Lopen -- L", "Zilvere sleutels: " + str(persoon.inventory.count(sleutel_zilver))))
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
    print((16*' ' + "|{:^" + str(15)+ "}|").format(persoon.current_room.exits[0].name))
    print('+' + 15*'-' + '+' + 6*'-' + ' ↑ ' + 6*'-' + '+' + 15*'-' + '+')
    print( ("|{:^" + str(15)+ "}←{:^" + str(15)+ "}→{:^" + str(15)+ "}|").format(persoon.current_room.exits[1].name, persoon.current_room.name, persoon.current_room.exits[3].name)  )
    print('+' + 15*'-' + '+' + 6*'-' + ' ↓ ' + 6*'-' + '+' + 15*'-' + '+')
    print((16*' ' + "|{:^" + str(15)+ "}|").format(persoon.current_room.exits[2].name))
    print(16*' ' + '+' + 15*'-' + '+\n')


def clear_screen(): #Maakt het scherm leeg
    #os.system("cls" if os.name == "nt" else "clear")
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n') #Tijdelijke oplossing

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
SCHERMBREEDTE = 100
HELFT_SCHERMBREEDTE = SCHERMBREEDTE/2
MAX_WOORD_LENGTE = 20
BEGIN_GELD = 0

#Maakt de Items
appel = Item('Appel', 'eten', 3, 'A', 4, 'Wat een mooie rode appel, misschien is hij wel iets te rood...')
brood = Item('Brood', 'eten', 7, 'B', 7, 'Dit brood was ooit het symbool van het dorp, tot een dwerg hem ooit stal.')
taart = Item('Taart', 'eten', 10, 'T', 10, 'Deze taart is zelf gemaakt door de beste bakker je zult er zeker niet aan dood gaan.')
soep = Item('Soep', 'eten', 15, 'S', 14, 'Zo de soep ziet er wel erg heet uit, misschien even wachten met eten.')
ijs = Item('Ijs', 'eten', 20, 'I', 17, 'Pas op dat een brainfreeze je niet je leven kost.')
handschoen = Item('Handschoen', 'wapen', 4, 'H', 8, 'Deze magische handschoenen zorgen er voor dat je handen mooi blijven.')
zwaard = Item('Zwaard', 'wapen', 6, 'Z', 15, 'Misschien was dit wel het zwaard van koning Arthur, wie zal het zeggen.')
pijl_boog = Item('Pijl en Boog', 'wapen', 8, 'P', 20, 'Met deze boog heeft ooit iemand een appel van zijn zoons hoofd geschoten.')
mes = Item('Mes', 'wapen', 15, 'M', 30, 'Dit lijkt misschien wel een klein mes maar... nee dit is gewoon een klein mes.')
knuppel = Item('Knuppel', 'wapen', 20, 'K', 45, 'Deze knuppel kan erg hard aankomen, pas op dat je hem niet op je eigen hoofd laat vallen.')

vuisten = Item('Vuisten', 'wapen', 3, 'V', 0, 'nvt')

eten = [appel, brood, taart, soep, ijs]
wapens = [handschoen, zwaard, pijl_boog, mes, knuppel]
spullen = [appel, brood, taart, soep, ijs, handschoen, zwaard, pijl_boog, mes, knuppel]

sleutel_goud = Item('Gouden Sleutel', 'sleutel', 0, 'G', 0, 'nvt')
sleutel_zilver = Item('Zilvere Sleutel', 'sleutel', 0, 'G', 0, 'nvt')

#Maakt speler en start het spel
winkel = Winkel()
persoon = Player()
speel = Controller()
speel.play_game()
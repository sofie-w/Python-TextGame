import random
from gegevens import hight, width
from print_functies import print_header, print_regel, print_footer, print_footer_los, print_regel_los, clear_screen, enter
from items import sleutel_zilver

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

        
    
    def describe(self, persoon):
        if self.locked == True:
            print_header('De deur zit op slot je hebt een zilvere sleutel nodig om hem te openen.')
            if sleutel_zilver in persoon.inventory:
                print_footer_los()
                gebruiken = 'a'
                while gebruiken != 'y' or gebruiken != 'Y' or gebruiken != 'n' or gebruiken != 'N':
                    gebruiken = input('Wil je de zilvere sleutel gebruiken(y/n): ')
                    if gebruiken == 'y' or gebruiken == 'Y':
                        self.locked = False
                        print_regel('De kamer is open!')
                        enter()
                        clear_screen()
                    elif gebruiken != 'n' or gebruiken != 'N':
                        print_regel('Je hebt iets verkeerd getypt.')
                    
            else:
                print_footer('Je hebt geen zilvere sleutels, vindt er eentje!')
                enter()
                    
        if len(self.items) >= 1 and self.locked == False:
            print_header('Je ziet in de ' + self.name + ' een '+ self.items[0].item_name + ' liggen.')# Maak grammatica correct bij alle kamers!
            print_regel('Er staat een ' + self.monster.soort + ' voor.')
            print_regel('')
            print_footer('Monster: '+ str(self.monster.life) + ' - Jij: ' + str(persoon.life))
            vraag = 'a'
            door = 'a'
            while vraag != 'y' and vraag != 'Y' and vraag != 'n' and vraag != 'N' and door != 'v':
                vraag = input('Wil je het '+ self.monster.soort +' aanvallen(y/n): ')
                
                
                if vraag == 'y' or vraag == 'Y':
                    while self.monster.life > 0 and persoon.life > 0 and door != 'v':
                        self.monster.attack(persoon)
                        if self.monster.life > 0 and persoon.life > 0:
                            vraag = 'g'
                            while vraag != 'A' and vraag != 'a' and vraag != 'V' and vraag != 'v':
                                vraag = input('Wil je verder met aanvallen(a) of wil je vluchten(v) (a/v): ')
                                if vraag == 'a' or vraag == 'A':
                                    clear_screen()
                                elif vraag == 'v' or vraag == 'V':
                                    door = 'v'
                                    clear_screen()
                                else:
                                    print_regel_los('Je hebt iets verkeerd ingevuld.')
                    if persoon.life <= 0:
                        
                        print_regel_los('Je bent dood')
                        return('S')
                    
                    elif self.monster.life <= 0:
                        #clear_screen()
                        print_regel_los('Je hebt het monster verslagen! Je hebt ' + str(self.monster.waarde) + ' coins verdiend.')
                        enter()
                        persoon.geld += self.monster.waarde
                        item = self.items[0]
                        self.items.remove(self.items[0])
                        return(item)

                elif vraag == 'n' or vraag == 'N':
                    clear_screen()
                    return(0)
                else:
                    clear_screen()
                    print_regel_los('Je hebt iets verkeerd ingevuld.')
                    
                    
        elif len(self.items) <= 0:
            print_regel_los('Je bent nu in de ' + self.name + '. De kamer lijkt leeg. Je hebt hier al geweest.')
            return(0)
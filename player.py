from gegevens import LEVENS_SPELER, BEGIN_GELD, SCHERMBREEDTE
from print_functies import print_header, print_regel_los, print_regel, enter, clear_screen, print_footer_los
from items import sleutel_zilver, spullen

class Player: #Lopen en de inventory
    def __init__(self):
        self.inventory = [sleutel_zilver]
        self.current_room = 'I'
        self.life = LEVENS_SPELER
        self.geld = BEGIN_GELD
        

    def goto_room(self):
        door = 'ja'
        while door == 'ja':
            self.print_world_rand()
            lopen = input("Waar wil je heen(W/A/S/D): ")
            clear_screen()
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
            

    def print_world_rand(self):
        print(16*' ' + '+' + 15*'-' + '+')
        print((16*' ' + "|{:^" + str(15)+ "}|").format(self.current_room.exits[0].name))
        print('+' + 15*'-' + '+' + 6*'-' + ' ↑ ' + 6*'-' + '+' + 15*'-' + '+')
        print( ("|{:^" + str(15)+ "}←{:^" + str(15)+ "}→{:^" + str(15)+ "}|").format(self.current_room.exits[1].name, self.current_room.name, self.current_room.exits[3].name)  )
        print('+' + 15*'-' + '+' + 6*'-' + ' ↓ ' + 6*'-' + '+' + 15*'-' + '+')
        print((16*' ' + "|{:^" + str(15)+ "}|").format(self.current_room.exits[2].name))
        print(16*' ' + '+' + 15*'-' + '+\n')

    def set_current_room(self, room):
        self.current_room = room
        
                
    def kijken(self):
        item = self.current_room.describe(self)
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

    def print_inv(self, spullen):
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        self.print_regel_inv('Eten', 'Aantal', 'Wapens', 'Aantal')
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        for i in range(int(len(spullen)/2)):
            self.print_regel_inv(spullen[i].item_name, str(self.inventory.count(spullen[i])), spullen[i+5].item_name, str(self.inventory.count(spullen[i+5])))
        print("+" + "-"*(SCHERMBREEDTE-2) + "+")
        
        print_regel('Als je extra informatie wilt over het item type dan de eerste letter.')
        keuze = input('| Klik anders op enter... ')
        teller = 0
        for i in range(len(spullen)):
            if keuze == spullen[i].letter:
                print('\n')
                spullen[i].uitleg_item()
                enter()
            else:
                teller += 1
        if teller == len(spullen):
            clear_screen()
                
    def print_regel_inv(self, regel1, regel2, regel3, regel4):
        print(("| {:" + str(int(SCHERMBREEDTE*(1/3)) - 1)+ "}|{:^" + str(int(SCHERMBREEDTE*(1/6)) - 1)+ "}| {:" + str(int(SCHERMBREEDTE*(1/3)) - 2)+ "}|{:^" + str(int(SCHERMBREEDTE*(1/6)) - 1)+ "}|").format(regel1, regel2, regel3, regel4))
    
    def eten(self, persoon):
        print_header('Je hebt nu ' + str(persoon.life) + ' levens.')
        self.print_regel_inv('Eten', 'Aantal', 'Levens', 'Letter')
        for i in range(int(len(spullen)/2)):
            self.print_regel_inv(spullen[i].item_name, str(self.inventory.count(spullen[i])), str(spullen[i].damage_levens) + ' levens', spullen[i].letter)
        print_footer_los()
        
        keuze = input('Wat wil je eten: ')
        keuze = keuze.capitalize()
        fout = True
        for i in range(int(len(spullen)/2)):
            if keuze == spullen[i].letter:
                fout = False
                if self.inventory.count(spullen[i]) > 0:
                    self.inventory.remove(spullen[i])
                    self.life = self.life + spullen[i].damage_levens
                else:
                    clear_screen()
                    print_regel_los('Je hebt geen ' + spullen[i].item_name.lower() + '.')
                    enter()
        if fout:
            clear_screen()
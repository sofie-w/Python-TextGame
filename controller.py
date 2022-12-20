from world import World
from winkel import Winkel
from player import Player
from print_functies import print_regel, print_header, print_footer, print_regel_los, enter, clear_screen
from items import sleutel_goud, sleutel_zilver, spullen, alle_spullen
from gegevens import SCHERMBREEDTE

class Controller: # Begint het spel en laat het menu zien
    def __init__(self):
        self.keuze = 'L'

    def play_game(self):
        winkel = Winkel()
        persoon = Player()
        mana = World("Mana")
        mana.create_world(persoon)
        self.uitleg()
        while self.keuze != 'S' and self.keuze != 's':
        #or self.keuze != 's':
            self.print_menu(persoon)
            self.keuze = input("Kies(K/L/I/E/W/S): ")
            clear_screen()
            if self.keuze == 'L' or self.keuze == 'l':
                persoon.goto_room()
                print('')
            elif self.keuze == 'I' or self.keuze == 'i':
                persoon.print_inv(spullen)
            elif self.keuze == 'K' or self.keuze == 'k':
                self.keuze = persoon.kijken()
            elif self.keuze == 'E' or self.keuze == 'e':
                persoon.eten()
            elif self.keuze == 'W' or self.keuze == 'w':
                winkel.laten_zien(persoon)
            elif self.keuze == 'S' or self.keuze == 's':
                print_regel_los('Doei doei')
            else:
                print_regel_los('Je hebt iets verkeerd getypt, probeer het opnieuw.')
            
            if persoon.inventory.count(sleutel_goud) == 3: #Als je 3 sleutels hebt dan win je
                self.keuze = 'S'
                print_regel_los("Je hebt de goude sleutel gevonden! Je hebt gewonnen")
    
    def print_menu(self, persoon):
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
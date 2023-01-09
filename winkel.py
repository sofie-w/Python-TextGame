from gegevens import SCHERMBREEDTE, hight, width
from print_functies import clear_screen, print_regel_los
from items import appel, brood, taart, soep, ijs, handschoen, zwaard, pijl_boog, mes, knuppel, sleutel_zilver, sleutel_goud, spullen

class Winkel:      
    def laten_zien(self, persoon):
        door = ja
        while door == ja:
            print("+" + "-"*(SCHERMBREEDTE-2) + "+")
            self.print_regel_winkel("Wat", "Letter", "Prijs")
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
        
            keuze = input("Jouw geld: " + str(persoon.geld) + " \nWat wil je kopen, klik anders op enter: ")
            keuze = keuze.capitalize()
            clear_screen()
            teller = 0
            for i in range(len(spullen)):
                if spullen[i].letter == keuze:
                    if spullen[i].prijs <= persoon.geld:
                        self.kopen(spullen[i], persoon)
                        print_regel_los('Je hebt een ' + spullen[i].item_name + ' gekocht.')
                    else:
                        clear_screen()
                        print_regel_los('Je hebt niet genoeg geld.')
                    door = nee
                else:
                    teller += 1
            if teller == len(spullen):
                clear_screen()
                if keuze != '':
                    print_regel_los('Dit item bestaan niet.')
                else:
                    door = nee
                
                
    def print_regel_winkel(self, regel1, regel2, regel3):
        print(("| {:" + str(int(SCHERMBREEDTE*(1/2)) - 3)+ "} | {:^" + str(int(SCHERMBREEDTE*(1/4)) - 4)+ "} |{:^" + str(int(SCHERMBREEDTE*(1/4)) - 2)+ "} |").format(regel1, regel2, regel3))
            
    def kopen(self, item, persoon):
        persoon.geld -= item.prijs
        persoon.pick_up(item)
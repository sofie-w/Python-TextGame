from gegevens import LEVENS_MONSTER, LEVENS_SPECIAALMONSTER, DAMAGE_MONSTER, DAMAGE_SPECIAALMONSTER, WAARDE_MONSTER, WAARDE_SPECIAALMONSTER
from print_functies import clear_screen, print_header, print_regel, print_footer
from items import wapens, vuisten
import random


class Enemy:
    def __init__(self):
        self.life = LEVENS_MONSTER
        self.max_schade = DAMAGE_MONSTER
        self.waarde = WAARDE_MONSTER
        self.soort = 'monster'

    def attack(self, persoon):
        self.attacked(persoon)
        if random.randint(0,4) == 1:
            self.struikelen()
            print_regel('Hierdoor gaat zijn aanval fout.')
        else:
            schade_persoon = random.randint(0,self.max_schade)
            print_regel('Jij: -' + str(schade_persoon))
            persoon.life -= schade_persoon
        print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(persoon.life))
        
    def attacked(self, persoon):
        wapen = self.wapen(persoon)
        self.life -= wapen.damage_levens
        print_header('Monster: -' + str(wapen.damage_levens))
        
    def struikelen(self):
        fouten = ('Het monster probeert je aan te vallen maar hij struikeld over een bananenschil.',
                  'Terwijl het monster je aanvalt wordt hij afgeleid door een raar geluid.',
                  'Het monster schrikt zo van je dat hij omvalt.')
        print_regel(fouten[random.randint(0,len(fouten))])
        
            
    def wapen(self, persoon):
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
        
    def attack(self, persoon):
        if random.randint(0, 3) == 1:
            persoon.life -= 6
            Enemy.attacked(self, persoon)
            #print_regel('Hahjbdeouhfvoefvefogv')
            print_regel(self.aanval)
            print_regel('Jij: -6')
            print_footer('Monster: '+ str(self.life) + ' - Jij: ' + str(persoon.life))
        
        else:
            Enemy.attack(self, persoon)           
            
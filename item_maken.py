from gegevens import SCHERMBREEDTE

class Item: #Geeft de items een naam en een soort
    def __init__(self, _name, _itemtype, _damage_levens, _letter, _prijs, _uitleg):
        self.item_name = _name
        self.item_type = _itemtype
        self.damage_levens = _damage_levens
        self.letter = _letter
        self.prijs = _prijs
        self.uitleg = _uitleg
        
    def print_kopen(self):
        print(("| {:" + str(int(SCHERMBREEDTE*(1/2)) - 3)+ "} | {:^" + str(int(SCHERMBREEDTE*(1/4)) - 4)+ "} |{:^" + str(int(SCHERMBREEDTE*(1/4)) - 2)+ "} |").format(self.item_name + " +" + str(self.damage_levens), self.letter, str(self.prijs)))
        #print_regel_winkel(self.item_name + " +" + str(self.damage_levens), self.letter, str(self.prijs))
        
    def uitleg_item(self):
        print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(self.uitleg))
        #print_regel(self.uitleg)
        

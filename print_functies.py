from gegevens import SCHERMBREEDTE

def clear_screen(): #Maakt het scherm leeg
    #os.system("cls" if os.name == "nt" else "clear")
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n') #Tijdelijke oplossing

def enter():
    verder = input('Klik enter om verder te gaan...')
    clear_screen()


def print_footer(zin):
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(zin))
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    
def print_footer_los():
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    
def print_header(zin):
    print("+" + "-"*(SCHERMBREEDTE-2) + "+")
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(zin))

    
def print_regel(regel):
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))

def print_regel_los(regel):
    print("="*(SCHERMBREEDTE))
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))
    print("="*(SCHERMBREEDTE))
    
def print_regel_dubbel(zin1, zin2):
    print(("| {:"+ str(int((SCHERMBREEDTE/2))-2) +"}{:^"+ str(int((SCHERMBREEDTE/2))-1) +"}|").format(zin1, zin2))
    

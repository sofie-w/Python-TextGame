from item_maken import Item

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

alle_spullen = [appel, brood, taart, soep, ijs, handschoen, zwaard, pijl_boog, mes, knuppel, sleutel_zilver, sleutel_goud]
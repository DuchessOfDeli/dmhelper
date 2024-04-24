import random

for i in range(1, 999):
    
    warehouse = random.choice(["Empty or abandoned","Heavily guarded, expensive","Cheap goods","Bulk goods","Live animals","Weapons/armor","Goods from a distant land","Secret smuggler's den"])
    
    religious = random.choice(["Temple to a good or neutral deity","Temple to a false deity (run by charlatan priests)","Home of ascetics","Abandoned shrine","Library dedicated to religious study","Hidden shrine to a fiend or an evil deity"])
    current_calamity = random.choice(["Suspected vampire infestation","New cult seeks converts","Important figure died (murder suspected)","War between rival thieves' guilds","Plague or famine","Corrupt officials","Marauding monsters","Powerful wizard has moved into town","Economic depression(trade disrupted)","Flooding","Undead stirring in cemeteries","Prophecy of doom","Brink of war","Internal strife(leads to anarchy)","Besieged by enemies","Scandal threatens powerful families","Dungeon discovered (adventurers flock to town)","Religious sects struggle for power"])
    known_for = random.choice(["Delicious cuisine","Rude people","Greedy merchants","Artists and writers","Great hero/savior","Flowers","Hordes of beggars","Tough warriors","Dark magic","Decadence","Piety","Gambling","Godlessness","Education","Wines","High fashion","Political intrigue","Powerful guilds","Strong drink","Patriotism"])
    notable_traits = random.choice(["Canals in place of streets","Massive statue or monument","Grand temple","Large fortress","Verdant parks and orchards","River divides town","Major trade center","Headquarters of a powerful family or guild","Population mostly wealthy","Destitute, rundown","Awful smell(tanneries, open sewers, etc.)","Center of trade for one specific good","Site of many battles","Site of mythic or magical event","Important library or archive","Worship of all gods banned","Sinister reputation","Notable library or academy","Site of important tomb or graveyard","Built atop ancient ruins"])
    ruler_status = random.choice(["Respected, fair, and just","Feared tyrant","Weakling manipulated by others","Illegitimate ruler, simmering civil war","ruled or controlled by a powerful monster","Mysterious, anonymous cabal","Contested leadership, open fighting","Cabal seized power openly","Doltish lout","On deathbed, claimants compete for power","iron-willed but respected","Religious leader"])
    race_relations = random.choice(["Harmony","Tension or rivalry","Racial majority are conquerors","Racial minority are rulers","Racial minority are refugees","Racial majority oppresses minority","Racial minority oppresses majority"])
    input("Press 'Enter' for a random settlements.")
    print(' ')
    print("Settlement #" + str(i))
    print("...........................")
    print("Race_relations: " + race_relations)
    print("Ruler status: " + ruler_status)
    print("Notable traits: " + notable_traits)
    print("Known_for: " + known_for)
    print("Current calamity: " + current_calamity)
    print(" ")
    print("Buildings below")
    print("...........................")

    for i in range(5):
        building_type = random.choice(["Residence","Religious","Tavern","Warehouse","Shop"])
        shop = random.choice(["Pawnshop","Herbs/incense","Fruits/vegetables","Dried meats","Pottery","Undertaker","Books","Moneylender","Weapons/armor","Chandler","Smithy","Carpenter","Weaver","Jeweler","Baker","Mapmaker","Tailor","Ropemaker","Mason","Scribe"])
        residence = random.choice(["Abandoned squat","Middle-class home","Upper-class home","Crowded tenement","Orphanage","Hidden thieves' den","Front for a secret cult","Lavish, guarded mansion"])
        tavern1 = random.choice(["The Silver ", "The Golden ", "The Staggering ", "The Laughing ", "The Prancing ", "The Gilded ", "The Running ","The Howling ","The Slaughtered ","The Leering ","The Drunken ","The Leaping ","The Roadring ","The Frowning ","The Lonely ","The Wandering ","The Mysterious ","The Barking ","The Black ","The Gleaming "])
        tavern2 = random.choice(["Eel","Dophin","Dwarf","Pegasus","Pony","Rose","Stag","Wolf","Lamb","Demon","Goat","Spirit","Horde","Jester","Mountain","Eagle","Satyr","Dog","Spider","Star"])
        tavern_array = random.choice(["Quiet, low-key bar","Raucous dive","Thieves' guild hangout","Gathering place for a secret society","Upper-class dining club","Gambling den","Caters to specific guild","Members-only club","Music venue"])
        
        if building_type == str("Residence"):
            print("Residence: " + residence)
        if building_type == str("Tavern"):
            print ("Tavern: " + (tavern1 + tavern2))
            print ("Vibe: " + tavern_array)
        if building_type == str("Religious"):
            print("Religious: " + religious)
        if building_type == str("Warehouse"):
            print("Warehouse: " + warehouse)
        if building_type == str("Shop"):
            print("Shop: " + shop)
    print(" ")
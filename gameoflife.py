 # initial state of the battlefield
the_universe = 459778 # glider: 459778
def a_war(Time):
    Past = False
    Ruin = 1
    the_end = 0
    Eternal_Cycle = 101
    the_world = the_universe
    while not the_end:
        a_city = Time
        a_city += 1
        a_battle(a_city, the_world)
        Time = a_city
        Gods_Hands = the_world
        Mercy = Judgement(Gods_Hands)
        the_world = Mercy
        if the_world == Past or Time >= Eternal_Cycle - Ruin:
            break
        Past = the_world
    return the_world
def a_battle(a_moment, a_place):
    Commander_Raising_Its_Sword = "\n"
    Patches = "#"
    Coins = "."
    the_sun = 7
    the_horizon = 8
    my_banner = 0
    the_battlefield = Commander_Raising_Its_Sword
    while my_banner <= the_sun:
        my_sight = 0
        while my_sight < the_horizon:
            an_ennemy = the_warrior(my_banner, my_sight)
            if a_brave(an_ennemy, a_place) == True:
                Wounded_Warrior = the_battlefield + Patches
                the_battlefield = Wounded_Warrior
            else:
                Warrior_Eyes = the_battlefield + Coins
                the_battlefield = Warrior_Eyes
            my_sight += 1
        my_banner += 1
        the_battlefield = the_battlefield + Commander_Raising_Its_Sword
    print("Turn")
    print(a_moment)
    print(the_battlefield)
    "Victory !"
    print(Commander_Raising_Its_Sword)
    return the_battlefield
def the_warrior(the_strength, the_blade):
    your_arm = 8
    a_swing = the_strength * your_arm
    return a_swing + the_blade
def a_brave(a_sword, the_world):
    the_sea = 64
    the_ice = 0
    if a_sword < the_ice or a_sword > the_sea:
        return False
    Violence = 1
    Turning_Back = 2
    the_ground = the_power(a_sword)
    your_domain = the_world / the_ground
    Ashes = Quick_Fire(your_domain, Turning_Back) # modulo 2
    return Ashes >= Violence
def the_power(my_mind):
    my_strength = 0
    my_strength += 1
    the_ennemy = 3
    the_ennemy -= 1
    while my_mind != False:
        my_strength = my_strength * the_ennemy
        my_mind -= 1
    return my_strength
 # modulus, super slow
def Fire(your_heart, your_soul):
    while not your_heart < your_soul:
        your_heart = your_heart - your_soul
    return your_heart
 # not valid rockstar, see https://github.com/dylanbeattie/rockstar/issues/192
def Quick_Fire(a_number, a_mod):
    return a_number % a_mod
def the_judge(a_god, a_man):
    a_verdict = 0
    Beauty = 9
    Dana = a_god + Beauty
    if a_brave(Dana, a_man) == True:
        a_verdict += 1
    Ogma = a_god - Beauty
    if a_brave(Ogma, a_man) == True:
        a_verdict += 1
    Strength = 8
    Dagda = a_god + Strength
    if a_brave(Dagda, a_man) == True:
        a_verdict += 1
    Cermait = a_god - Strength
    if a_brave(Cermait, a_man) == True:
        a_verdict += 1
    Love = 7
    Aengus = a_god + Love
    if a_brave(Aengus, a_man) == True:
        a_verdict += 1
    Morrigan = a_god - Love
    if a_brave(Morrigan, a_man) == True:
        a_verdict += 1
    Life = 1
    Brigid = a_god + Life
    if a_brave(Brigid, a_man) == True:
        a_verdict += 1
    Donn = a_god - Life
    if a_brave(Donn, a_man) == True:
        a_verdict += 1
    return a_verdict
def Judgement(a_soul):
    a_future = a_soul
    the_sun = 7
    the_horizon = 8
    Glory = 3
    Shame = 2
    the_banner = 0
    while the_banner <= the_sun:
        the_army = 0
        while the_army < the_horizon:
            Gods_Will = the_warrior(the_banner, the_army)
            Prophecy = a_brave(Gods_Will, a_soul)
            Destiny = the_judge(Gods_Will, a_soul)
            if Prophecy == True and Destiny != Glory and Destiny != Shame:
                a_grave = a_future - the_power(Gods_Will)
                a_future = a_grave
            if Prophecy != True and Destiny == Glory:
                a_miracle = a_future + the_power(Gods_Will)
                a_future = a_miracle
            the_army += 1
        the_banner += 1
    return a_future
Eternity = 0
a_war(Eternity)

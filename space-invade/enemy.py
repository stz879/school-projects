#listen for variable to be true
#enemies spawn when variable set to true

#reset enemy hp and damage
    #basic enemy starting hp = 1
basic_enemy_hp = 1
    #basic enemy starting damage = 1
basic_enemy_dmg = 1

    #stronger enemy starting hp = 3
strong_enemy_hp = 3
    #stronger enemy starting damage = 2
strong_enemy_dmg = 2

#enemies start moving, but wait 2 seconds to start shooting
#player also has to wait 2 seconds to start shooting, but only 0.5 to start moving

#enemies get n pixels closer when they reach the end of the screen
    #TODO: figure out how many pixels enemies should travel

#if all enemies are dead
    #respawn enemies with a 0.5x boost to damage
    # +1 to level count
lvl = +1
    # +2 to player max health
player_hp += 2
    # +n to pixels traveled by enemies

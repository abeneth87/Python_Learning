#Non-Block Scope with exampl

game_level = 3
# enemies = ["Skeleteon", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

def create_new_enemy():
    enemies = ["Skeleteon", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_new_enemy()

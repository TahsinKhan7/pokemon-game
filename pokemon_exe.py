from pokemon_oop_sql_game import *


# Class instance:
# pokemonNames package test
# p = PokemonNames()
# print('Random Pokemon:', p.get_random_name())

player_instance = Player()  #Set a player name! (set to default 'Ash Ketchum' and 'Pallet town' if left empty)

print(f'Welcome {player_instance.name}, to your pokemon journey!')
print(f'You leave {player_instance.city} and eventually find yourself in front of a forest with a large sign in front of it which states...')
print('"WARNING: highly inhabited poke-area"')
poke_search = input('Enter forest and search for pokemon? (Y/N)')

while True:
    if poke_search.strip().capitalize() == 'Y':
        player_instance.search_for_pokemon()

    elif poke_search.strip().capitalize() == 'N':
        print('You ran away')
        break
    else:
        print('Please state Y or N')

    ##################
    capture_decision = input(f'Attempt to capture?')
    if capture_decision.strip().capitalize() == 'Y':
        player_instance.try_catch_pokemon()

    elif poke_search.strip().capitalize() == 'N':
        print('You ran away')
        continue
    else:
        print('Please select Y or N')


    ###################
    search_decision = input('Continue searching? (Y/N)')

    if search_decision.strip().capitalize() == 'Y':
        player_instance.search_for_pokemon()

    elif search_decision.strip().capitalize() == 'N':
        print('You ran away')
        break
    else:
        print('Please state Y or N')
    ##################
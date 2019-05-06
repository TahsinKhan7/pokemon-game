from pokemon_oop_sql_game import *

# poke_conn = PokeConnection()
# poke_conn.cursor.execute()
# pokemonNames package test
# p = PokemonNames()
# print('Random Pokemon:', p.get_random_name())
''
# User input for player name:
player_name = input('Enter Player name: ')
player_city = input('Enter Player hometown: ')

#Creating instances:
player_instance = Player(player_name, player_city)  #Set a player name! (set to default 'Ash Ketchum' and 'Pallet town' if left empty)
poke_gen = PokemonNames()

print(f'\nWelcome {player_instance.name}, to your pokemon journey!')
print(f'You leave {player_instance.city} and eventually find yourself in front of a forest with a large sign in front of it.')
print('The sign reads: "WARNING!!!: highly inhabited pokemon-area"')
print('You curiously enter the forest...')


while True:
    poke_search = input('\nSearch for pokemon? (Y/N): ')

    if poke_search.strip().capitalize() == 'Y':
        generated_pokemon = poke_gen.get_random_name()
        poke_instance = Pokemon(generated_pokemon)
        player_instance.search_for_pokemon(poke_instance)

        print('')
        poke_instance.pokemon_tackle()
        poke_instance.pokemon_cry()
        poke_instance.pokemon_rest()
        print('')

        while True:
            capture_decision = input(f'Attempt to capture? (Y/N): ')
            if capture_decision.strip().capitalize() == 'Y':
                player_instance.try_catch_pokemon(poke_instance)
                player_instance.save_player_and_pokemon_to_db(player_instance)
                poke_instance.save_pokemon_encounter_to_pokedex_db(poke_instance)
                break
            elif poke_search.strip().capitalize() == 'N':
                print('You ran away')
                break
            else:
                print('Please select Y or N')
                continue

    elif poke_search.strip().capitalize() == 'N':
        print('You ran back home')
        break
    else:
        print('Please state Y or N')
        continue


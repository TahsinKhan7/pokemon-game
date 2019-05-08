from pokemon_oop_sql_game import *
print("pokemon_exe is:", __name__,'\n')

# poke_conn = PokeConnection()
# poke_conn.cursor.execute()
# pokemonNames package test
# p = PokemonNames()
# print('Random Pokemon:', p.get_random_name())

# User input for player name:
print('Welcome to Pokemon Super Adventure 9000!')
player_name = input('Enter Player name: ')
player_city = input('Enter Player hometown: ')

# Creating instances:
player_instance = Player(player_name, player_city)
poke_gen = PokemonNames()

# Printing story setting:
print(f'\nWelcome {player_instance.name}, to your pokemon journey!')
print(f'You leave {player_instance.city} and eventually find yourself in front of a forest with a large sign in front of it.')
print('The sign reads: "WARNING!!!: highly inhabited pokemon-area"')
print('You curiously enter the forest...')

#Search for pokemon loop:
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

        #Capturing pokemon loop
        while True:
            capture_decision = input(f'Attempt to capture? (Y/N): ')

            if capture_decision.strip().capitalize() == 'Y':
                player_instance.try_catch_pokemon(poke_instance)
                player_instance.save_player_and_pokemon_to_db(player_instance)
                break
            elif capture_decision.strip().capitalize() == 'N':
                print('\nYou ran away...')
                break
            else:
                print('\nPlease select Y or N.\n')
                continue

        #Saving any pokemon enounter to pokedex:
        poke_instance.save_pokemon_encounter_to_pokedex_db(poke_instance)

        #Loading stored player or pokemon data via input loops:
        while True:
            db_check = input('\nLoad saved player data? (Y/N): ')
            if db_check.strip().capitalize() == 'Y':
                player_instance.load_player_from_db()
                break
            elif db_check.strip().capitalize() == 'N':
                break
            else:
                print('please state "Y" or "N"')
                continue
        while True:
            pokedex_check = input('\nSee encountered pokemon in pokedex? (Y/N): ')
            if pokedex_check.strip().capitalize() == 'Y':
                poke_instance.load_pokedex_data_from_db()
                break
            elif pokedex_check.strip().capitalize() == 'N':
                break
            else:
                print('please state "Y" or "N"')
                continue

    elif poke_search.strip().capitalize() == 'N':
        print('\nYou ran back home')
        break
    else:
        print('\nPlease state Y or N')
        continue
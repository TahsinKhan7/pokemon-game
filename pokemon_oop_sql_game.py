from pokemon_sql_db_connection import *
from pokemonNames.pokemonNames import *
import random

class Player:
    def __init__(self, name='Ash Ketchum', city='Pallet Town'):
        self.name = name
        self.city = city
        self.inventory = ''
        self.pokemon = ''
        self.pokemon_caught_list = []

    def search_for_pokemon(self, pokemon=''):
        poke_instance = PokemonNames()
        pokemon = poke_instance.get_random_name()
        print(f'A {pokemon} appeared!')

    def try_catch_pokemon(self):
        while True:
            print(f'{self.name}: "Poke-ball go!"')
            print('The pokemon is warped into the pokeball...')
            catch_rate = random.randint(0, 1)

            if catch_rate == 1:
                print('You captured a {pokemon}!, congrats!, \n saving {pokemon}"s data to pokedex...')
                self.pokemon_caught_list.append()
                search_decision = print(input('Continue search?'))
            else:
                print('The pokemon burst free out of your pokeball!')
                capture_decision = print(input('Throw another? (Y/N)'))
                if capture_decision.strip() == 'Y':
                    continue
                else:
                    print('You fled')
                    break


    def save_player_and_pokemon(self):
        #think insert into
        pass

    def load_previous_player(self):
        # Be able to retrieve/read previous stored players from a sql database
        # think fetch all
        pass


class Pokemon(Player):
    def __init__(self):
        super(Pokemon, self).__init__()
        self.pokemon_name = self.pokemon

    def pokemon_tackle(self):
        print(f'{self.pokemon_name} uses Tackle on you, ouch!')
        pass

    def pokemon_cry(self):
        print(f'{self.pokemon_name} makes its poke-noise')
        pass

    def rest_to_regain_health(self):
        print(f'{self.pokemon_name} eats a poke-snack and takes a nap...')
        print(f'{self.pokemon_name}"s health has been fully restored!')
        pass

    def save_pokemon_encounter_to_pokedex(self):

        pass

    def load_pokedex_data_from_db(self):
        pass
from pokemon_sql_db_connection import *
from pokemonNames.pokemonNames import *
import random

class Player:
    def __init__(self, name='Ash Ketchum', city='Pallet Town'):
        self.name = name
        self.city = city
        self.__pokemon_caught_list = []

    def search_for_pokemon(self, poke_instance):
        # poke_instance = PokemonNames()
        # pokemon = poke_instance.get_random_name()
        #self.pokemon_encounter = pokemon
        print(f'{self.name} brushes through the dense foliage of the forest')
        print(f'A {poke_instance.pokemon_name} appeared!')

    def try_catch_pokemon(self, poke_instance):
        while True:
            print(f'{self.name}: "Poke-ball go!"')
            print(f'{poke_instance.pokemon_name} is warped into the pokeball...')
            catch_rate = random.randint(0, 1)

            if catch_rate == 1:
                print(f'You captured a {poke_instance.pokemon_name}!, congrats!, \n saving {poke_instance.pokemon_name}"s data to pokedex...')
                self.__pokemon_caught_list.append(poke_instance)
                break
            else:
                print(f'{poke_instance.pokemon_name} burst free out of your pokeball!')
                throw_more = print(input('Throw another? (Y/N)'))
                if throw_more.strip().capitalize() == 'Y':
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

class Pokemon:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name

    def pokemon_tackle(self):
        print(f'{self.pokemon_name} uses Tackle on you, ouch!')
        pass

    def pokemon_cry(self):
        print(f'{self.pokemon_name} makes its poke-noise')
        pass

    def pokemon_rest(self):
        print(f'{self.pokemon_name} eats a poke-snack and takes a nap...')
        print(f'{self.pokemon_name}"s health has been fully restored!')
        pass

    def save_pokemon_encounter_to_pokedex(self):
        pass

    def load_pokedex_data_from_db(self):
        pass
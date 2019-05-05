from pokemon_sql_db_connection import *
from pokemonNames.pokemonNames import *

class Player:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.pokemon_caught_list = []

    def search_for_pokemon(self):
        print(f'Welcome {self.name}, to your pokemon journey')
        #input('press any key to continue')
        #Psuedo code:
        # Generate random pokemon
        # prompt user to capture or not
        # call a private encapsulated method to capture pokemon

        pass


    def __try_catch_pokemon(self):
        # if successful append to pokemon list
            # pokemon_list.append(pokemon_captured)
            #think appending oop python objects to list
        pass

    def save_player_and_pokemon(self):
        #think insert into
        pass

    def load_previous_player(self):
        # Be able to retrieve/read previous stored players from a sql database
        # think fetch all
        pass


class Pokemon:
    def __init__(self):
        self.pokemon_name = ''

    def pokemon_tackle(self):
        pass

    def pokemon_cry(self):
        pass

    def rest_at_poke_center(self):
        pass

    def save_pokemon(self):
        pass

    def load_pokemon(self):
        pass

p = PokemonNames()
p.get_random_name()



class PokeConnection:
    def __init__(self):
        #self.connection = 'Microsoft SQL Server'
        self.server = 'localhost,1433'
        self.database = 'Pokemon_Game_Db'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_db_instance = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cursors = self.docker_db_instance.cursor()
from pokemon_oop_sql_game import *
import unittest

def search_for_pokemon_test():
    assert search_for_pokemon_test()

def catch_pokemon_test():
    assert try_catch_pokemon()


def
    def save_player_and_pokemon_to_db(self, player_instance, poke_instance):
        query = (f"INSERT INTO PlayerSave(Name, City, CaughtPokemon) VALUES('{player_instance.name}','{player_instance.city}', '{poke_instance.pokemon_name}')")
        cursor.execute(query)
        docker_Pokemon_Game_Db.commit()
        print('\nInventory data successfully saved!')
def
    def load_player_from_db(self):
        query = 'SELECT * FROM PlayerSave;'
        cursor.execute(query)
        player_results = cursor.fetchall()
        print('\nDisplaying player data:')

        for player in player_results:
            print(Player(player.Name, player.City), player.CaughtPokemon)

def
    def save_pokemon_encounter_to_pokedex_db(self, poke_instance):
        query = (f"INSERT INTO Pokedex(PokemonName) VALUES ('{poke_instance.pokemon_name}')")
        cursor.execute(query)
        docker_Pokemon_Game_Db.commit()
        print('Pokemon encounter successfully updated on pokedex!')
def
    def load_pokedex_data_from_db(self):
        query = 'SELECT * FROM Pokedex;'
        cursor.execute(query)
        poke_results = cursor.fetchall()
        print('Loading Pokedex data...')

        for pokemon in poke_results:
            load_poke = Pokemon(pokemon.PokemonName)
            print(load_poke.pokemon_name)
        print('\nPokedex data successfully loaded.')
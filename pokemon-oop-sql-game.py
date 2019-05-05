from pokemonNames.pokemonNames import PokemonNames

class Player:

    def __init__(self):
        self.name = 'Ash Ketchum'
        self.city = 'Pallet Town'
        self.pokemon = []

    def search_for_pokemon(self):
        pass


    def __try_catch_pokemon(self):
        pass


    def save_player_and_pokemon(self):
        pass


    def load_previous_player(self):
        pass


class Pokemon(Player):
    def __init__(self):
        super().__init__()

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

import aiohttp
import random

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.img = None
        self.name = None

    async def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['forms'][0]['name']
                else:
                    return "Pikachu"

    async def info(self):
        if not self.name:
            self.name = await self.get_name()
        return f"O nome do seu Pokémon é: {self.name}"

    async def show_img(self):
        # Um método assíncrono para obter o nome de um Pokémon pela PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:  # Abrindo uma sessão HTTP
            async with session.get(url) as response:  # Enviando uma solicitação GET para obter os dados do Pokémon
                if response.status == 200:
                    data = await response.json()  # Recebendo a resposta JSON
                    img_url = data['sprites']['front_default']  # Obtendo a URL de um Pokémon
                    return img_url  # Returning the image's URL
                else:
                    return None  # Retornando None se a solicitação falhar

from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
    
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.HP = self.get_HP()
        self.attack = self.get_attack()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

     # Метод для получения здоровья покемона через API
    def get_HP(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]['base_stat'])
        else:
            return "Я не знаю его HP"
        
     # Метод для получения силы атаки покемона через API
    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][1]['base_stat'])
        else:
            return "Видимо он бессильный"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name} \nHP: {self.HP} \nСила атаки: {self.attack}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    # Метод класса для получения здоровья покемона
    def show_HP(self):
        return self.HP
    
    # Метод класса для получения силы атаки покемона
    def show_attack(self):
        return self.attack
    
    




from ..models.animal import *
from .databasemanager import *

def row_to_animal(row):
    return Animal(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

class AnimalManager(object):
    @staticmethod
    def register(animal):
        if not isinstance(animal, Animal):
            raise TypeError("L'objet n'est pas un Animal")
        DatabaseManager.register_animal(animal.get_numero(), animal.get_nom(), animal.get_sexe(), animal.get_race(), animal.get_date_naissance(), \
                                                animal.get_pere(), animal.get_mere(), animal.get_jumeau(), animal.get_pays(), animal.get_cheptel())

    @staticmethod
    def delete(animal):
        if not isinstance(animal, Animal):
            raise TypeError("L'objet n'est pas de type Animal")
        DatabaseManager.delete_animal(animal.get_numero())

    @staticmethod
    def get_all_animals():
        animals = []
        data = DatabaseManager.select_all_animals()
        for row in data:
            animals.append(row_to_animal(row))
        return animals

    @staticmethod
    def get_animal_by_numero(numero):
        animals = []
        row = DatabaseManager.select_animal_by_numero(numero)
        if row: 
            animals.append(row_to_animal(row))
            return animals
        return []

    @staticmethod
    def get_animal_by_nom(nom):
        animals = []
        row = DatabaseManager.select_animal_by_nom(nom)
        if row:
            animals.append(row_to_animal(row))
            return animals
        return []

    @staticmethod
    def get_animals_by_sexe(sexe):
        animals = []
        data = DatabaseManager.select_animals_by_sexe(sexe)
        for row in data:
            animals.append(row_to_animal(row))
        return animals

    @staticmethod
    def get_animals_by_date_naissance(date_naissance):
        animals = []
        data = DatabaseManager.select_animals_by_date_naissance(date_naissance)
        for row in data:
            animals.append(row_to_animal(row))
        return animals

    @staticmethod
    def get_animals_by_pere(pere):
        animals = []
        data = DatabaseManager.select_animals_by_pere(pere)
        for row in data:
            animals.append(row_to_animal(row))
        return animals

    @staticmethod
    def get_animals_by_mere(mere):
        animals = []
        data = DatabaseManager.select_animals_by_mere(mere)
        for row in data:
            animals.append(row_to_animal(row))
        return animals

    @staticmethod
    def get_animals_by_pays(pays):
        animals = []
        data = DatabaseManager.select_animals_by_pays(pays)
        for row in data:
            animals.append(row_to_animal(row))
        return animals

    @staticmethod
    def get_animals_by_race(race):
        animals = []
        data = DatabaseManager.select_animals_by_race(race)
        for row in data:
            animals.append(row_to_animal(row))
        return animals

    @staticmethod
    def get_animals_by_cheptel(cheptel):
        animals = []
        data = DatabaseManager.select_animals_by_cheptel(cheptel)
        for row in data:
            animals.append(row_to_animal(row))
        return animals

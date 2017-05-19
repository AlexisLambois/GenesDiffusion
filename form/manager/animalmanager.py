from ..models.animal import Animal
from .databasemanager import DatabaseManager

def row_to_animal(row):
    return Animal(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],row[10],row[11])

class AnimalManager(object):
    @staticmethod
    def register(animal):
        if not isinstance(animal, Animal):
            raise TypeError("L'objet n'est pas un Animal")
        DatabaseManager.register_animal(animal.get_numero(), animal.get_nom(), animal.get_sexe(), animal.get_race(), animal.get_date_naissance(), \
                                                animal.get_pere(), animal.get_mere(), animal.get_jumeau(), animal.get_pays(), animal.get_cheptel(),animal.get_ordre(),animal.get_date_insertion())

    ##@staticmethod
    #def delete(animal):
    #    if not isinstance(animal, Animal):
    #        raise TypeError("L'objet n'est pas de type Animal")
    #   DatabaseManager.delete_animal(animal.get_numero())

    @staticmethod
    def get_animal_by_alpha(tosql):
        animals = []
        data = DatabaseManager.select_animal_by_alpha(tosql)
        for row in data:
            animals.append(row_to_animal(row))
        return animals
    
    @staticmethod
    def get_animal_by_beta(tosql):
        animals = []
        data = DatabaseManager.select_animal_by_beta(tosql)
        for row in data:
            animals.append(row_to_animal(row))
        return animals
    
    @staticmethod
    def get_all_animals():
        animals = []
        data = DatabaseManager.select_all_animals()
        for row in data:
            animals.append(row_to_animal(row))
        return animals

    @staticmethod
    def get_animal_by_gamma(tosql,sous_requete):
        no_sous_requete = True
        requete = "(SELECT numero from form_animal WHERE "
        if tosql:
            for cle, valeur in tosql.items():
                requete += str(cle + "='" + str(valeur) + "' AND ")
        for cle, valeur in sous_requete.items():
            if str(valeur) != "":
                no_sous_requete = False
                break
        if not tosql and no_sous_requete : return ""
        if not no_sous_requete :
            for cle, valeur in sous_requete.items():
                if str(valeur) != "":
                    requete += str(cle + "=" + str(valeur) + " AND ")
        requete = requete[0:-5]
        requete += ")"
        return requete
'''
Created on 19 juin 2017

@author: alexis
'''
from form.models.user import User
from .databasemanager import DatabaseManager

def row_to_user(row):
    return User(row[0], row[1], row[2])

class UserManager(object):
    @staticmethod
    def register(user):
        if not isinstance(user, User):
            raise TypeError("L'objet n'est pas un User")
        DatabaseManager.register_user(user.get_id(),user.get_mdp(),user.get_droit_insertion())


    @staticmethod
    def get_user(id):
        object = DatabaseManager.select_user(id)
        if len(object) != 0 :
            return row_to_user(object[0])
        return None
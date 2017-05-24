#! /usr/bin/python
#-*- coding:UTF8 -*-

from ..models.preleveur import Preleveur
from .databasemanager import DatabaseManager

def row_to_preleveur(row):
    return Preleveur(row[0], row[1])

class PreleveurManager(object):

    @staticmethod
    def register(preleveur):
        if not isinstance(preleveur, Preleveur):
            raise TypeError("L'objet n'est pas un Preleveur")
        DatabaseManager.register_preleveur(preleveur.get_numero(), preleveur.get_nom())

    #@staticmethod
    #def delete(preleveur):
    #    if not isinstance(preleveur, Preleveur):
    #        raise TypeError("L'objet n'est pas de type Preleveur")
    #    DatabaseManager.delete_preleveur(preleveur.get_numero())

    @staticmethod
    def get_preleveur_by_alpha(tosql):
        preleveur = []
        data = DatabaseManager.select_preleveur_by_alpha(tosql)
        for row in data:
            preleveur.append(row_to_preleveur(row))
        return preleveur
    
    @staticmethod
    def get_preleveur_by_beta(tosql):
        preleveur = []
        data = DatabaseManager.select_preleveur_by_beta(tosql)
        for row in data:
            preleveur.append(row_to_preleveur(row))
        return preleveur
    
    @staticmethod
    def get_all_preleveur():
        preleveur = []
        data = DatabaseManager.select_all_preleveurs()
        for row in data:
            preleveur.append(row_to_preleveur(row))
        return preleveur
    
    @staticmethod
    def get_preleveur_by_gamma(tosql):
        return DatabaseManager.select_preleveur_by_gamma(tosql)

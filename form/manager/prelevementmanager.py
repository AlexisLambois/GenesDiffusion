#! /usr/bin/python
#-*- coding:UTF8 -*-

from ..models.prelevement import *
from .databasemanager import *

def row_to_prelevement(row):
    return Prelevement()

class PrelevementManager(object):
    @staticmethod
    def register(prelevement):
        if not isinstance(prelevement, Prelevement):
            raise TypeError("L'objet n'est pas un Prelevement")
        DatabaseManager.register_prelevement()

    @staticmethod
    def delete(prelevement):
        if not isinstance(prelevement, Prelevement):
            raise TypeError("L'objet n'est pas de type Prelevement")
        DatabaseManager.delete_prelevement()

    @staticmethod
    def get_all_prelevements():
        prelevements = []
        data = DatabaseManager.select_all_prelevements()
        for row in data:
            prelevements.append(row_to_prelevement(row))
        return prelevements

    @staticmethod
    def get_prelevements_by_plaque(plaque):
        prelevements = []
        data = DatabaseManager.select_prelevements_by_plaque(plaque)
        for row in data:
            prelevements.append(row_to_prelevement(row))
        return prelevements

    @staticmethod
    def get_prelevements_by_position(position):
        prelevements = []
        data = DatabaseManager.select_prelevements_by_position(position)
        for row in data:
            prelevements.append(row_to_prelevement(row))
        return prelevements

    @staticmethod
    def get_prelevements_by_plaque_and_position(plaque, position):
        prelevements = []
        data = DatabaseManager.select_prelevements_by_plaque_and_position(plaque, position)
        for row in data:
            prelevements.append(row_to_prelevement(row))
        return prelevements

    @staticmethod
    def get_prelevements_by_date_reception(date_reception):
        prelevements = []
        data = DatabaseManager.select_prelevements_by_date_reception(date_reception)
        for row in data:
            prelevements.append(row_to_prelevement(row))
        return prelevements

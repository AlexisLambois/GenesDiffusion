#! /usr/bin/python
#-*- coding:UTF8 -*-

from ..models.preleveur import *
from .databasemanager import *

def row_to_preleveur(row):
    return Preleveur(row[0], row[1])

class PreleveurManager(object):

    @staticmethod
    def register(preleveur):
        if not isinstance(preleveur, Preleveur):
            raise TypeError("L'objet n'est pas un Preleveur")
        DatabaseManager.register_preleveur(preleveur.get_numero(), preleveur.get_nom())

    @staticmethod
    def delete(preleveur):
        if not isinstance(preleveur, Preleveur):
            raise TypeError("L'objet n'est pas de type Preleveur")
        DatabaseManager.delete_preleveur(preleveur.get_numero())

    @staticmethod
    def get_all_preleveurs():
        preleveurs = []
        data = DatabaseManager.select_all_preleveurs()
        for row in data:
            preleveurs.append(row_to_preleveur(row))
        return preleveurs

    @staticmethod
    def get_preleveurs_by_nom(nom):
        preleveurs = []
        data = DatabaseManager.select_preleveur_by_nom(nom)
        for row in data:
            preleveurs.append(row_to_preleveur(row))
        return preleveurs

    @staticmethod
    def get_preleveur_by_numero(numero):
        data = DatabaseManager.select_preleveur_by_numero(numero)
        if data:
            return row_to_preleveur(data)
        return None


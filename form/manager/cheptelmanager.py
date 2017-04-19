#! /usr/bin/python
#-*- coding:UTF8 -*-

from ..models.cheptel import *
from .databasemanager import *

def row_to_cheptel(row):
    return Cheptel(row[0], row[1])

class CheptelManager(object):

    @staticmethod
    def register(cheptel):
        if not isinstance(cheptel, Cheptel):
            raise TypeError("L'objet n'est pas un Cheptel")
        DatabaseManager.register_cheptel(cheptel.get_numero(), cheptel.get_detenteur())

    @staticmethod
    def delete(cheptel):
        if not isinstance(cheptel, Cheptel):
            raise TypeError("L'objet n'est pas de type Cheptel")
        DatabaseManager.delete_cheptel(cheptel.get_numero())

    @staticmethod
    def get_all_cheptels():
        cheptels = []
        data = DatabaseManager.select_all_cheptels()
        for row in data:
            cheptels.append(row_to_cheptel(row))
        return data

    @staticmethod
    def get_cheptel_by_detenteur(detenteur):
        cheptels = []
        data = DatabaseManager.select_cheptel_by_detenteur(detenteur)
        for row in data:
            cheptels.append(row_to_cheptel(row))
        return cheptels

    @staticmethod
    def get_cheptel_by_numero(numero):
        cheptels = []
        row = DatabaseManager.select_cheptel_by_numero(numero)
        if row:
            cheptels.append(row_to_cheptel(row))
            return cheptels
        return []

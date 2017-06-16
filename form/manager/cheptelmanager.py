#! /usr/bin/python
#-*- coding:UTF8 -*-

from form.models.cheptel import Cheptel
from form.manager.databasemanager import DatabaseManager

""" Methode conversion données brutes en objet Cheptel """

def row_to_cheptel(row):
    return Cheptel(row[0], row[1])

class CheptelManager(object):

    @staticmethod
    def register(cheptel):
        if not isinstance(cheptel, Cheptel):
            raise TypeError("L'objet n'est pas un Cheptel")
        DatabaseManager.register_cheptel(cheptel.get_numero(), cheptel.get_detenteur())

    @staticmethod
    def get_all_cheptels():
        cheptels = []
        data = DatabaseManager.select_all_cheptels()
        for row in data:
            cheptels.append(row_to_cheptel(row))
        return data

    @staticmethod
    def get_cheptel_by(tosql):
        cheptels = []
        data = DatabaseManager.select_cheptel_by(tosql)
        for row in data:
            cheptels.append(row_to_cheptel(row))
        return cheptels
    
    @staticmethod
    def get_cheptel_sous_requete(tosql):
        return DatabaseManager.select_cheptel_sous_requete(tosql)
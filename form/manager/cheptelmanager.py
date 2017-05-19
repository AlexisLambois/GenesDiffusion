#! /usr/bin/python
#-*- coding:UTF8 -*-

from ..models.cheptel import Cheptel
from .databasemanager import DatabaseManager

def row_to_cheptel(row):
    return Cheptel(row[0], row[1])

class CheptelManager(object):

    @staticmethod
    def register(cheptel):
        if not isinstance(cheptel, Cheptel):
            raise TypeError("L'objet n'est pas un Cheptel")
        DatabaseManager.register_cheptel(cheptel.get_numero(), cheptel.get_detenteur())

    #@staticmethod
    #def delete(cheptel):
    #    if not isinstance(cheptel, Cheptel):
    #        raise TypeError("L'objet n'est pas de type Cheptel")
    #    DatabaseManager.delete_cheptel(cheptel.get_numero())

    @staticmethod
    def get_all_cheptels():
        cheptels = []
        data = DatabaseManager.select_all_cheptels()
        for row in data:
            cheptels.append(row_to_cheptel(row))
        return data

    @staticmethod
    def get_cheptel_by_alpha(tosql):
        cheptels = []
        data = DatabaseManager.select_cheptel_by_alpha(tosql)
        for row in data:
            cheptels.append(row_to_cheptel(row))
        return cheptels
    
    @staticmethod
    def get_cheptel_by_beta(tosql):
        cheptels = []
        data = DatabaseManager.select_cheptel_by_beta(tosql)
        for row in data:
            cheptels.append(row_to_cheptel(row))
        return cheptels
    
    @staticmethod
    def get_cheptel_by_gamma(tosql):
        if not tosql : return ""
        requete = "(SELECT numero from form_cheptel WHERE "
        for cle, valeur in tosql.items():
            requete += str(cle + "='" + str(valeur) + "' AND ")
        requete = requete[0:-5]
        requete += ")"
        return requete
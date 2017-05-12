#! /usr/bin/python
#-*- coding:UTF8 -*-

from form.models.prelevement import Prelevement
from form.manager.databasemanager import DatabaseManager

def row_to_prelevement(row):
    return Prelevement(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])

class PrelevementManager(object):
    @staticmethod
    def register(prelevement):
        if not isinstance(prelevement, Prelevement):
            raise TypeError("L'objet n'est pas un Prelevement")
        DatabaseManager.register_prelevement(prelevement.get_plaque(),prelevement.get_position(),prelevement.get_date_enregistrement(),prelevement.get_date_demande(),prelevement.get_date_extraction(),prelevement.get_date_reception_lille(),prelevement.get_type_materiel(),prelevement.get_dosage(),prelevement.get_conformite_dosage(),prelevement.get_code_barre(),prelevement.get_nombre_extraction(),prelevement.get_echec_extraction(),prelevement.get_statut_vcg(),prelevement.get_date_insertion(),prelevement.get_animal(),prelevement.get_preleveur())

    """@staticmethod
    def delete(prelevement):
        if not isinstance(prelevement, Prelevement):
            raise TypeError("L'objet n'est pas de type Prelevement")
        DatabaseManager.delete_prelevement()"""
    
    @staticmethod
    def get_prelevement_by_alpha(tosql):
        prelevements = []
        data = DatabaseManager.select_prelevement_by_alpha(tosql)
        for row in data:
            prelevements.append(row_to_prelevement(row))
        return prelevements
    
    @staticmethod
    def get_prelevement_by_beta(tosql):
        prelevements = []
        data = DatabaseManager.select_prelevement_by_beta(tosql)
        for row in data:
            prelevements.append(row_to_prelevement(row))
        return prelevements
    
    @staticmethod
    def get_all_prelevements():
        prelevements = []
        data = DatabaseManager.select_all_prelevements()
        for row in data:
            prelevements.append(row_to_prelevement(row))
        return prelevements

    
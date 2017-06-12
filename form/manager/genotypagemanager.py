'''
Created on 12 mai 2017

@author: alexis
'''
from form.models.genotypage import Genotypage
from form.manager.databasemanager import DatabaseManager
 
def row_to_genotypage(row):
    return Genotypage(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9])

class GenotypageManager(object):
    
    @staticmethod
    def register(genotypage):
        if not isinstance(genotypage, Genotypage):
            raise TypeError("L'objet n'est pas un Genotypage")
        DatabaseManager.register_genotypage(genotypage.get_plaque(), genotypage.get_position(), genotypage.get_format_puce(),genotypage.get_date_debut(),genotypage.get_date_scan(),genotypage.get_callrate(),genotypage.get_link_to_file(),genotypage.get_note(),genotypage.get_prelevement())
    
    @staticmethod
    def get_genotypage_by(tosql):
        genotypages = []
        data = DatabaseManager.select_genotypage_by(tosql)
        for row in data:
            genotypages.append(row_to_genotypage(row))
        return genotypages
    
    @staticmethod
    def get_all_genotypages():
        genotypages = []
        data = DatabaseManager.select_all_genotypages()
        for row in data:
            genotypages.append(row_to_genotypage(row))
        return genotypages
    
    @staticmethod
    def get_genotypage_sous_requete(tosql,sous_requete):
        return DatabaseManager.select_genotypage_sous_requete(tosql, sous_requete)
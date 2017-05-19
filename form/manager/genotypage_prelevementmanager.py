'''
Created on 18 mai 2017

@author: alexis
'''
from form.manager.databasemanager import DatabaseManager
from form.models.genotypage_prelevement import Genotypage_Prelevement

def row_to_fusion(row):
    return Genotypage_Prelevement(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19],row[20],row[21],row[22],row[23])

class Genotypage_PrelevementManager(object):
    
    @staticmethod
    def get_fusion():
        fusion = []
        data = DatabaseManager.fusion()
        for row in data:
            fusion.append(row_to_fusion(row))
        return fusion
    
    @staticmethod
    def get_fusion_by(tosql_genotype,tosql_prelevement):
        fusion = []
        data = DatabaseManager.get_fusion_by(tosql_genotype,tosql_prelevement)
        for row in data:
            fusion.append(row_to_fusion(row))
        return fusion

    
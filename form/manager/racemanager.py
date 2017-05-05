#! /usr/bin/python
#-*- coding:UTF8 -*-

from ..models.race import Race
from .databasemanager import DatabaseManager

def row_to_race(row):
    return Race(row[0], row[1])

class RaceManager(object):

    @staticmethod
    def register(race):
        if not isinstance(race, Race):
            raise TypeError("L'objet n'est pas un Race")
        DatabaseManager.register_race(race.get_numero(), race.get_nom())

    #@staticmethod
    #def delete(race):
    #    if not isinstance(race, Race):
    #        raise TypeError("L'objet n'est pas de type Race")
    #    DatabaseManager.delete_race(race.get_numero())

    @staticmethod
    def get_all_races():
        races = []
        data = DatabaseManager.select_all_races()
        for row in data:
            races.append(row_to_race(row))
        return races

    @staticmethod
    def get_race_by_alpha(tosql):
        races = []
        data = DatabaseManager.select_race_by_alpha(tosql)
        for row in data:
            races.append(row_to_race(row))
        return races
    
    @staticmethod
    def get_race_by_beta(tosql):
        races = []
        data = DatabaseManager.select_race_by_beta(tosql)
        for row in data:
            races.append(row_to_race(row))
        return races
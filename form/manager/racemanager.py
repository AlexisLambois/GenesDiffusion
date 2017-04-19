#! /usr/bin/python
#-*- coding:UTF8 -*-

from ..models.race import *
from .databasemanager import *

def row_to_race(row):
    return Race(row[0], row[1])

class RaceManager(object):

    @staticmethod
    def register(race):
        if not isinstance(race, Race):
            raise TypeError("L'objet n'est pas un Race")
        DatabaseManager.register_race(race.get_numero(), race.get_nom())

    @staticmethod
    def delete(race):
        if not isinstance(race, Race):
            raise TypeError("L'objet n'est pas de type Race")
        DatabaseManager.delete_race(race.get_numero())

    @staticmethod
    def get_all_races():
        races = []
        data = DatabaseManager.select_all_races()
        for row in data:
            races.append(row_to_race(row))
        return races

    @staticmethod
    def get_race_by_nom(nom):
        races = []
        data = DatabaseManager.select_race_by_nom(nom)
        for row in data:
            races.append(row_to_race(row))
        return races

    @staticmethod
    def get_race_by_numero(numero):
        races = []
        row = DatabaseManager.select_race_by_numero(numero)
        if row:
            races.append(row_to_race(row))
            return races
        return []

from FietsSysteem import *

import json


class Beheer():
    def __init__(self):
        self.gebruikers = {}
        self.fietsen = {}
        self.stations = {}

    def stationToevoegen(self, naam: str, aantal_plaatsen: int, latitude: str, longitude: str):
        self.stations[len(self.stations) + 1] = FietsStation(naam, len(self.stations) + 1, aantal_plaatsen, latitude,
                                                             longitude)

    def stationsInladen(self, filePath):
        with open(filePath, "r") as bestand:
            geojson = json.load(bestand)
        for nieuw_station in geojson["features"]:
            self.stationToevoegen(naam=nieuw_station["properties"]["Straatnaam"],
                                  aantal_plaatsen=nieuw_station["properties"]["Aantal_plaatsen"],
                                  latitude=nieuw_station["geometry"]["coordinates"][0],
                                  longitude=nieuw_station["geometry"]["coordinates"][1])


oBeheerder = Beheer()

oBeheerder.stationsInladen("./data/velo.geojson")

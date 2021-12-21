from FietsSysteem import *

import json


class Beheer():
    def __init__(self):
        self.gebruikers = {}
        self.fietsen = {}
        self.stations = {}
        self.transporteurs = {}
        self.abonnementen = []
        self.abonnementen.append(JaarKaart)
        self.abonnementen.append(Weekpas)
        self.abonnementen.append(Dagpas)

    def gebruikerToevoegen(self, voornaam: str, achternaam: str, email: str, abonnement_type: Abonnement) -> Klant:
        """
        Voeg Klant toe aan de gebruikers dictionary.
        :param voornaam: str Voornaam van de gebruiker.
        :param achternaam: str Achternaam van de gebruiker.
        :param email: str Email van de gebruiker.
        :param abonnement_type: Abonnement Welk abonnement de gebruiker heeft aangevraagd.
        :return: Klant object
        """
        nieuwe = Klant(len(self.gebruikers) + 1, voornaam, achternaam, email, abonnement_type)
        self.gebruikers[len(self.stations) + 1] = nieuwe
        return nieuwe

    def stationToevoegen(self, naam: str, aantal_plaatsen: int, latitude: str, longitude: str) -> FietsStation:
        """
        Voeg Station toe aan de gebruikers dictionary.
        :param naam: str Naam van het station.
        :param aantal_plaatsen: int Totaal aantal plaatsen in het station.
        :param latitude: str Latitude voor coordinaten.
        :param longitude: str Longitude voor coordinaten.
        :return: Station object
        """
        nieuwe = FietsStation(naam, len(self.stations) + 1, aantal_plaatsen, latitude,
                              longitude)
        self.stations[len(self.stations) + 1] = nieuwe
        return nieuwe

    def fietsToevoegen(self, fiets_type: int) -> Fiets:
        """
        Voeg Fiets toe aan de gebruikers dictionary.
        :param fiets_type: int Nummer dat verwijst naar het type fiets.
        :return: Fiets object
        """
        nieuwe = Fiets(len(self.fietsen) + 1, fiets_type)
        self.fietsen[len(self.stations) + 1] = nieuwe
        return nieuwe

    def transporteurToevoegen(self, kenteken: str, aantal_plaatsen: int) -> Transporteur:
        """
        Voeg Transporteur toe aan de gebruikers dictionary.
        :param kenteken: str Kenteken van de wagen waarmee de transporteur rijdt.
        :param aantal_plaatsen: int Totaal aantal plaaten in wagen.
        :return: Transporteur object
        """
        nieuwe = Transporteur(kenteken, aantal_plaatsen)
        self.transporteurs[len(self.transporteurs) + 1] = nieuwe
        return nieuwe

    def stationsInladen(self, filePath: str, report=None):
        """
        Laadt Stations in vanuit GeoJSON afkomstig van stad Antwerpen.
        :param filePath: str Pad naar het GeoJSON bestand. Absoluut of relatief.
        :param report: (Optioneel) Eventueel het VeloView object om de print() functie te kunnen gebruiken.
                        Elk geïmporteerde station kan zo weergegeven worden in de GUI.
        """
        with open(filePath, "r") as bestand:
            geojson = json.load(bestand)
        for nieuw_station in geojson["features"]:
            nieuwe = self.stationToevoegen(naam=nieuw_station["properties"]["Straatnaam"],
                                           aantal_plaatsen=nieuw_station["properties"]["Aantal_plaatsen"],
                                           latitude=nieuw_station["geometry"]["coordinates"][0],
                                           longitude=nieuw_station["geometry"]["coordinates"][1])
            if report is not None:
                report.print(nieuwe)


if __name__ == '__main__':
    oBeheerder = Beheer()
    oBeheerder.stationsInladen("./data/velo.geojson")

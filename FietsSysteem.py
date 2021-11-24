from Klant import *


class FietsStation():
    def __init__(self, naam, ID, aantal_plaatsen, latitude, longitude):
        self.naam = naam
        self.ID = ID
        self.aantal_plaatsen = aantal_plaatsen
        self.fietsen = []
        for i in range(aantal_plaatsen):
            self.fietsen.append({
                'SLOT': i + 1,
                'fiets': None
            })
        self.aantal_plaatsen_vrij = aantal_plaatsen
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Dit is station {self.ID}-{self.naam} ({self.longitude};{self.latitude}) " \
               f"Er zijn nog {self.aantal_plaatsen_vrij} van de {self.aantal_plaatsen} plaatsen vrij."

    def voeg_fiets_toe(self, nieuwe_fiets):
        for fiets in self.fietsen:
            if fiets['fiets'] is None:
                fiets['fiets'] = nieuwe_fiets
                self.aantal_plaatsen_vrij -= 1
                break

    def ontleen_fiets(self, klant):
        if not isinstance(klant, Klant):
            raise Exception("Enkel een Klant kan een fiets ontlenen.")
        if klant.fiets is not None:
            raise Exception("U heeft al een fiets ontleend")

        if self.aantal_plaatsen_vrij == 0:
            print("Het spijt ons, dit station is leeg.")
            return

        for fiets in self.fietsen:
            if fiets['fiets'] is not None:
                klant.fiets = fiets['fiets']
                print(f"Beste {klant.voornaam}, neem uw fiets uit slot {fiets['SLOT']}")
                self.aantal_plaatsen_vrij += 1
                fiets['fiets'] = None
                break

    def plaats_fiets_terug(self, klant):
        if not isinstance(klant, Klant):
            raise Exception("Enkel een Klant kan een fiets ontlenen.")

        # Uiteraard zet je bij de echte stations je fiets eerst in het station.
        if self.aantal_plaatsen_vrij == 0:
            print("Het spijt ons, dit station is vol.")
            return

        for fiets in self.fietsen:
            if fiets['fiets'] is None:
                fiets['fiets'] = klant.fiets
                klant.fiets = None
                self.aantal_plaatsen_vrij -= 1
                print(f"Beste {klant.voornaam}, uw fiets werd correct teruggeplaatst")
                break


class Fiets():
    def __init__(self, ID, fiets_type):
        self.ID = ID
        self.fiets_type = fiets_type

from __future__ import annotations

from Klant import *


class Fiets():
    def __init__(self, ID: int, fiets_type: int):
        """
        :param ID: Unieke ID voor de Fiets
        :param fiets_type: Het type fiets
        """
        self.ID = ID
        self.fiets_type = fiets_type
        self.onderhoud = ""
        self.zadel_achterstevoren = False

    def __str__(self):
        return f"Fiets {self.ID}, Type: {self.fiets_type}, Onderhoud geschiedenis: {'leeg' if self.onderhoud == '' else self.onderhoud}"

    def fiets_kapot(self) -> None:
        """
        Als de fiets kapot is zal een gebruiker deze methode moeten roepen
        """
        self.zadel_achterstevoren = True

    def onderhoud_toevoegen(self, log) -> None:
        """
        Een Transporteur kan een onderhoud toevoegen aan de fiets als de fiets stuk is
        :param log: Het onderhoud dat de Transporteur heeft toegevoegd
        :return: None
        """
        self.onderhoud += "- " + log + "\n"
        self.zadel_achterstevoren = False


class Transporteur():
    def __init__(self, kenteken: str, aantal_plaatsen: int):
        self.kenteken = kenteken
        self.aantal_plaatsen = aantal_plaatsen
        self.fietsen = []
        self.aantal_plaatsen_vrij = aantal_plaatsen

    def __str__(self):
        return f"Transporteur: Kenteken: {self.kenteken}, Nog {self.aantal_plaatsen_vrij} plaatsen vrij"

    def station_legen(self, station: FietsStation, aantal: int) -> None:
        """
        Transporteur kan een bepaald FietsStation legen
        :param station: FitsStation dat de Transporteur wil legen
        :param aantal: Aantal fietsen die er uit het station moeten gehaald worden
        :return: None
        """
        if not isinstance(station, FietsStation):
            raise Exception("Een transporteur kan enkel een Station legen")
        if aantal > self.aantal_plaatsen_vrij:
            aantal = self.aantal_plaatsen_vrij

        for i in range(aantal):
            station.ontleen_fiets(self)

        self.aantal_plaatsen_vrij = self.aantal_plaatsen - len(self.fietsen)

    def station_bijvullen(self, station: FietsStation, aantal: int) -> None:
        """
        Transporteur kan een bepaald FietsStation weer bijvullen
        :param station: FietsStation dat een Transporteur wil bijvullen
        :param aantal: Aantal fietsen die er moeten geplaatst worden
        :return: None
        """
        if not isinstance(station, FietsStation):
            raise Exception("Een transporteur kan enkel een Station bijvullen")
        if aantal > (self.aantal_plaatsen - self.aantal_plaatsen_vrij):
            aantal = self.aantal_plaatsen - self.aantal_plaatsen_vrij

        for i in range(aantal):
            station.plaats_fiets_terug(self)

        self.aantal_plaatsen_vrij = self.aantal_plaatsen - len(self.fietsen)

    def fietsen_fixen(self):
        """
        Geeft een transporteur de mogelijkheid om kapotte fietsen in zijn wagen te vinden
        """
        for fiets in self.fietsen:
            if fiets.zadel_achterstevoren:
                fiets.onderhoud_toevoegen(input("Uitgevoerd onderhoud: "))
                print(fiets)


class FietsStation():
    def __init__(self, naam: str, ID: int, aantal_plaatsen: int, latitude: str, longitude: str):
        """
        Fietsstation
        :param naam: Naam van het station, meestal een herkenbare locatie
        :param ID: Uniek identificatienummer van het Fietsstation
        :param aantal_plaatsen: Aantal vrije plaatsen voor fietsen
        :param latitude: Latitude coördinaat
        :param longitude: Longitude coördinaat
        """
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
        return f"Dit is station {str(self.ID).zfill(3)}-{self.naam} ({self.longitude};{self.latitude}) " \
               f"Er zijn nog {self.aantal_plaatsen_vrij} van de {self.aantal_plaatsen} plaatsen vrij."

    def voeg_fiets_toe(self, *nieuwe_fiets: Fiets) -> None:
        """
        Voegt een fiets toe aan het Fietsstation
        :param nieuwe_fiets: Fiets objecten om mee in de lijst te zetten
        """
        for enkeling in nieuwe_fiets:
            for fiets in self.fietsen:
                if fiets['fiets'] is None:
                    fiets['fiets'] = enkeling
                    self.aantal_plaatsen_vrij -= 1
                    break

    def ontleen_fiets(self, klant: Klant | Transporteur):
        """
        Krijg een fiets toegewezen uit het station
        :param klant: Klant of Transporteur kunnen een fiets toegewezen krijgen
        :return: Info over de ontlening
        """
        if not isinstance(klant, Klant) and not isinstance(klant, Transporteur):
            raise Exception("Enkel een Klant of Transporteur kan een fiets ontlenen.")
        if isinstance(klant, Klant):
            if klant.fiets is not None:
                print("U heeft al een fiets ontleend")
                return

            if self.aantal_plaatsen_vrij == self.aantal_plaatsen:
                print("Het spijt ons, dit station is leeg.")
                return
        if isinstance(klant, Transporteur):
            for fiets in self.fietsen:
                if fiets['fiets'] is not None:
                    if fiets['fiets'].zadel_achterstevoren:
                        klant.fietsen.append(fiets['fiets'])
                        print(
                            f"\tFiets uit slot {fiets['SLOT']} is stuk en kan worden meegenomen")
                        self.aantal_plaatsen_vrij += 1
                        fiets['fiets'] = None

        for fiets in self.fietsen:
            if fiets['fiets'] is not None:
                if isinstance(klant, Klant):
                    klant.fiets = fiets['fiets']
                    print(
                        f"\tBeste {klant.voornaam}, neem uw fiets uit slot {fiets['SLOT']}")
                if isinstance(klant, Transporteur):
                    klant.fietsen.append(fiets['fiets'])
                    print(f"\tFiets uit slot {fiets['SLOT']} kan worden meegenomen")
                self.aantal_plaatsen_vrij += 1
                fiets['fiets'] = None
                break

    def plaats_fiets_terug(self, klant: Klant | Transporteur):
        """
        Plaatst fiets terug in het Fietsstation
        :param klant: Klant of Transporteur kunnen een fiets terugplaatsen
        :return: Info over de terugplaatsing
        """
        if not isinstance(klant, Klant) and not isinstance(klant, Transporteur):
            raise Exception("Enkel een Klant kan een fiets ontlenen.")

        # Uiteraard zet je bij de echte stations je fiets eerst in het station.
        if self.aantal_plaatsen_vrij == 0:
            print("Het spijt ons, dit station is vol.")
            return

        for fiets in self.fietsen:
            if fiets['fiets'] is None:
                if isinstance(klant, Klant):
                    fiets['fiets'] = klant.fiets
                    klant.fiets = None
                    print(
                        f"\tBeste {klant.voornaam}, uw fiets werd correct teruggeplaatst")
                if isinstance(klant, Transporteur):
                    fiets['fiets'] = klant.fietsen.pop()
                self.aantal_plaatsen_vrij -= 1
                break

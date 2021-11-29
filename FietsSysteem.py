from Klant import *


class FietsStation():
    __kleur = '\033[31m'
    __kleur_reset = '\033[0m'

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
        return f"{self.__kleur}Dit is station {str(self.ID).zfill(3)}-{self.naam} ({self.longitude};{self.latitude}) " \
               f"Er zijn nog {self.aantal_plaatsen_vrij} van de {self.aantal_plaatsen} plaatsen vrij.{self.__kleur_reset}"

    def voeg_fiets_toe(self, *nieuwe_fiets):
        for enkeling in nieuwe_fiets:
            for fiets in self.fietsen:
                if fiets['fiets'] is None:
                    fiets['fiets'] = enkeling
                    self.aantal_plaatsen_vrij -= 1
                    break

    def ontleen_fiets(self, klant):
        if not isinstance(klant, Klant) and not isinstance(klant, Transporteur):
            raise Exception("Enkel een Klant of Transporteur kan een fiets ontlenen.")
        if isinstance(klant, Klant):
            if klant.fiets is not None:
                print(self.__kleur + "U heeft al een fiets ontleend" + self.__kleur_reset)
                return

            if self.aantal_plaatsen_vrij == self.aantal_plaatsen:
                print(self.__kleur + "Het spijt ons, dit station is leeg." +
                      self.__kleur_reset)
                return
        if isinstance(klant, Transporteur):
            for fiets in self.fietsen:
                if fiets['fiets'] is not None:
                    if fiets['fiets'].zadel_achterstevoren:
                        klant.fietsen.append(fiets['fiets'])
                        print(
                            f"{self.__kleur}\tFiets uit slot {fiets['SLOT']} is stuk en kan worden meegenomen{self.__kleur_reset}")
                        self.aantal_plaatsen_vrij += 1
                        fiets['fiets'] = None

        for fiets in self.fietsen:
            if fiets['fiets'] is not None:
                if isinstance(klant, Klant):
                    klant.fiets = fiets['fiets']
                    print(
                        f"{self.__kleur}\tBeste {klant.voornaam}, neem uw fiets uit slot {fiets['SLOT']}{self.__kleur_reset}")
                if isinstance(klant, Transporteur):
                    klant.fietsen.append(fiets['fiets'])
                    print(f"{self.__kleur}\tFiets uit slot {fiets['SLOT']} kan worden meegenomen{self.__kleur_reset}")
                self.aantal_plaatsen_vrij += 1
                fiets['fiets'] = None
                break

    def plaats_fiets_terug(self, klant):
        if not isinstance(klant, Klant) and not isinstance(klant, Transporteur):
            raise Exception("Enkel een Klant kan een fiets ontlenen.")

        # Uiteraard zet je bij de echte stations je fiets eerst in het station.
        if self.aantal_plaatsen_vrij == 0:
            print(self.__kleur + "Het spijt ons, dit station is vol." + self.__kleur_reset)
            return

        for fiets in self.fietsen:
            if fiets['fiets'] is None:
                if isinstance(klant, Klant):
                    fiets['fiets'] = klant.fiets
                    klant.fiets = None
                    print(
                        f"{self.__kleur}\tBeste {klant.voornaam}, uw fiets werd correct teruggeplaatst{self.__kleur_reset}")
                if isinstance(klant, Transporteur):
                    fiets['fiets'] = klant.fietsen.pop()
                self.aantal_plaatsen_vrij -= 1
                break


class Transporteur():
    def __init__(self, kenteken, aantal_plaatsen):
        self.kenteken = kenteken
        self.aantal_plaatsen = aantal_plaatsen
        self.fietsen = []
        self.aantal_plaatsen_vrij = aantal_plaatsen

    def __str__(self):
        return f"Transporteur: Kenteken: {self.kenteken}, Nog {self.aantal_plaatsen_vrij} plaatsen vrij"

    def station_legen(self, station, aantal):
        if not isinstance(station, FietsStation):
            raise Exception("Een transporteur kan enkel een Station legen")
        if aantal > self.aantal_plaatsen_vrij:
            aantal = self.aantal_plaatsen_vrij

        for i in range(aantal):
            station.ontleen_fiets(self)

        self.aantal_plaatsen_vrij = self.aantal_plaatsen - len(self.fietsen)

    def station_bijvullen(self, station, aantal):
        if not isinstance(station, FietsStation):
            raise Exception("Een transporteur kan enkel een Station bijvullen")
        if aantal > (self.aantal_plaatsen - self.aantal_plaatsen_vrij):
            aantal = self.aantal_plaatsen - self.aantal_plaatsen_vrij

        for i in range(aantal):
            station.plaats_fiets_terug(self)

        self.aantal_plaatsen_vrij = self.aantal_plaatsen - len(self.fietsen)

    def fietsen_fixen(self):
        for fiets in self.fietsen:
            if fiets.zadel_achterstevoren:
                fiets.onderhoud_toevoegen(input("Uitgevoerd onderhoud: "))
                print(fiets)


class Fiets():
    def __init__(self, ID, fiets_type):
        self.ID = ID
        self.fiets_type = fiets_type
        self.onderhoud = ""
        self.zadel_achterstevoren = False

    def __str__(self):
        return f"Fiets {self.ID}, Type: {self.fiets_type}, Onderhoud geschiedenis: {self.onderhoud}"

    def fiets_kapot(self):
        self.zadel_achterstevoren = True

    def onderhoud_toevoegen(self, log):
        self.onderhoud += "- " + log + "\n"

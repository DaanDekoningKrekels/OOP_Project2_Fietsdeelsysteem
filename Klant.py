from datetime import timedelta
import random


class Klant():
    def __init__(self, lid_nr, voornaam, achternaam, email, abonnement_type):
        self.lid_nr = lid_nr
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.email = email
        self.abonnement_type = abonnement_type
        self.fiets = None


class Abonnement():
    def __init__(self, start_datum):
        self.start_datum = start_datum


class JaarKaart(Abonnement):
    PRIJS = 55

    def __init__(self, start_datum):
        super(JaarKaart, self).__init__(start_datum)
        self.eind_datum = start_datum + timedelta(days=365)


class Weekpas(Abonnement):
    PRIJS = 11

    def __init__(self, start_datum):
        super(Weekpas, self).__init__(start_datum)
        self.eind_datum = start_datum + timedelta(days=7)
        self.pincode = random.randint(1000, 9999)


class Dagpas(Weekpas):
    PRIJS = 5

    def __init__(self, start_datum):
        super(Dagpas, self).__init__(start_datum)
        self.eind_datum = start_datum + timedelta(hours=24)

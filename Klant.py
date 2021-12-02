from datetime import timedelta, datetime
import random


class Abonnement():
    def __init__(self, start_datum: datetime):
        """
        Maakt een basis Abonnement aan
        :param start_datum: Startdatum van het abonnement
        """
        self.start_datum = start_datum


class JaarKaart(Abonnement):
    PRIJS = 55

    def __init__(self, start_datum: datetime):
        """
        Jaarkaart klasse en een Abonnement
        :param start_datum: Startdatum van de jaarkaart, doorgegeven aan Superklasse
        """
        super(JaarKaart, self).__init__(start_datum)
        self.eind_datum = start_datum + timedelta(days=365)


class Weekpas(Abonnement):
    PRIJS = 11

    def __init__(self, start_datum: datetime):
        """
        Weekpas klasse en een Abonnement heeft ook een pincode
        :param start_datum: Startdatum van de weekpas, doorgegeven aan Superklasse
        """
        super(Weekpas, self).__init__(start_datum)
        self.eind_datum = start_datum + timedelta(days=7)
        self.pincode = random.randint(1000, 9999)


class Dagpas(Weekpas):
    PRIJS = 5

    def __init__(self, start_datum: datetime):
        """
        Dagpas klasse en een Abonnement heeft ook een pincode via Superklasse Weekpas
        :param start_datum: Startdatum van de weekpas, doorgegeven aan Superklasse
        """
        super(Dagpas, self).__init__(start_datum)
        self.eind_datum = start_datum + timedelta(hours=24)


class Klant():
    def __init__(self, lid_nr: int, voornaam: str, achternaam: str, email: str, abonnement_type: Abonnement):
        """
        Maakt een Klant object aan.
        :param lid_nr: Unieke nummer van het lid
        :param voornaam: Voornaam van het lid
        :param achternaam: Achternaam van het lid
        :param email: Email van het lid
        :param abonnement_type: Abonnement type object
        """
        self.lid_nr = lid_nr
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.email = email
        self.abonnement_type = abonnement_type
        self.fiets = None

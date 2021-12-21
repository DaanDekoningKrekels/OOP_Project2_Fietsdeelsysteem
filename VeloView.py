import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QFileDialog

from Beheer import *
from Windows import MainWindow, NieuweObjecten


class VeloView(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, beheerder: Beheer, parent=None, ):
        super(VeloView, self).__init__(parent)
        self.beheerder = beheerder
        self.setupUi(self)
        self.Vragen = NieuweObjecten.NieuweObjecten()
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widget.setLayout(self.vbox)  # Layout instellen in de widget
        self.scrollArea.setWidget(self.widget)  # De widget aan de scrollarea toevoegen
        # self.vbox.addWidget(QLabel("tekstje")) # Manier om tekst aan de scrollarea toe te voegen
        self.stationsVenster = NieuweObjecten.NieuwVenster()
        self.fietsenVenster = NieuweObjecten.NieuwVenster()
        self.gebruikersVenster = NieuweObjecten.NieuwVenster()
        self.transporteursVenster = NieuweObjecten.NieuwVenster()

    def print(self, content: str):
        """
        Voegt content toe aan het MainWindow. Bv. bij het aanmaken van een Station.
        :param content: Content om toe te voegen aan het MainWindow
        """
        tekst = QLabel(str(content))
        # Ervoor zorgen dat nieuwe text aan de bovenkant wordt toegevoegd
        self.vbox.insertWidget(0, tekst)

    def nieuwStation(self):
        """
        Voegt een nieuw station toe aan de Beheerder via InputDialogs in de GUI.
        """
        try:
            naam, ID, aantal_plaatsen, latitude, longitude = self.Vragen.VraagStationInfo()
            ok = self.beheerder.stationToevoegen(naam, aantal_plaatsen, latitude, longitude)
            print(naam, ID, aantal_plaatsen, latitude, longitude)
        except:
            self.Vragen.ToonAnnulatie("station")
            ok = False
        if type(ok) == FietsStation:
            print("gelukt")
            self.print("Station toegevoegd: " + str(ok))

    def nieuwFiets(self):
        """
        Voegt een nieuwe fiets toe aan de Beheerder via InputDialogs in de GUI.
        """
        try:
            fiets_type = self.Vragen.VraagFietsInfo()
            ok = self.beheerder.fietsToevoegen(fiets_type)
        except:
            self.Vragen.ToonAnnulatie("fiets")
            ok = False
        if ok:
            self.print("Fiets toegevoegd: " + str(ok))

    def nieuwGebruiker(self):
        """
        Voegt een nieuwe gebruiker toe aan de Beheerder via InputDialogs in de GUI.
        """
        try:
            voornaam, achternaam, email, abonnement_type = self.Vragen.VraagGebruikerInfo(
                ["Jaarabonnement", "Weekpas", "Dagpas"])
            if abonnement_type == "Jaarabonnement":
                abonnement = JaarKaart(datetime.now())
            elif abonnement_type == "Weekpas":
                abonnement = Weekpas(datetime.now())
            else:
                abonnement = Dagpas(datetime.now())
            ok = self.beheerder.gebruikerToevoegen(voornaam, achternaam, email, abonnement)
        except:
            self.Vragen.ToonAnnulatie("gebruiker")
            ok = False
        if type(ok) == Klant:
            self.print("Gebruiker toegevoegd: " + str(ok))

    def nieuwTransporteur(self):
        """
        Voegt een nieuwe transporteur toe aan de Beheerder via InputDialogs in de GUI.
        """
        try:
            kenteken, aantal_plaatsen = self.Vragen.VraagTransporteurInfo()
            ok = self.beheerder.transporteurToevoegen(kenteken, aantal_plaatsen)
        except:
            self.Vragen.ToonAnnulatie("transporteur")
            ok = False
        if type(ok) == Transporteur:
            self.print("Transporteur toegevoegd: " + str(ok))

    def importStations(self):
        """
        Importeert Stations vanuit een GeoJSON bestand. Via een FileDialog in de GUI.
        """
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Geojson files (*.geojson)")
        if fname[0] != '':
            self.print("Start importeren")
            self.beheerder.stationsInladen(fname[0], self)
            self.print("Klaar met importeren")
        else:
            self.print("Importeren is geannuleerd")

    def vensterStations(self):
        """
        Toont een venster met alle Stations die de Beheerder bezit.
        """
        if self.stationsVenster.isVisible():
            self.stationsVenster.hide()
        else:
            self.stationsVenster.setWindowTitle("Alle stations")
            self.stationsVenster.show()
            for station in self.beheerder.stations:
                inhoud = QLabel(str(self.beheerder.stations[station]))
                self.stationsVenster.vbox.addWidget(inhoud)

    def vensterFietsen(self):
        """
        Toont een venster met alle Fietsen die de Beheerder bezit.
        """
        if self.fietsenVenster.isVisible():
            self.fietsenVenster.hide()
        else:
            self.fietsenVenster.setWindowTitle("Alle fietsen")
            self.fietsenVenster.show()
            for fiets in self.beheerder.fietsen:
                inhoud = QLabel(str(self.beheerder.fietsen[fiets]))
                self.fietsenVenster.vbox.addWidget(inhoud)

    def vensterGebruikers(self):
        """
        Toont een venster met alle Gebruikers die de Beheerder bezit.
        """
        if self.gebruikersVenster.isVisible():
            self.gebruikersVenster.hide()
        else:
            self.gebruikersVenster.setWindowTitle("Alle gebruikers")
            self.gebruikersVenster.show()
            for gebruiker in self.beheerder.gebruikers:
                inhoud = QLabel(str(self.beheerder.gebruikers[gebruiker]))
                self.gebruikersVenster.vbox.addWidget(inhoud)

    def vensterTransporteurs(self):
        """
        Toont een venster met alle Transporteurs die de Beheerder bezit.
        """
        if self.transporteursVenster.isVisible():
            self.transporteursVenster.hide()
        else:
            self.transporteursVenster.setWindowTitle("Alle transporteurs")
            self.transporteursVenster.show()
            for transporteur in self.beheerder.transporteurs:
                inhoud = QLabel(str(self.beheerder.transporteurs[transporteur]))
                self.transporteursVenster.vbox.addWidget(inhoud)

    def exportStations(self):
        """
        Zou Stations kunnen exporteren naar GeoJSON of een Picle bestand.
        Nog niet geïmplementeerd.
        """
        self.Vragen.ToonNotImplemented()

    def exportFietsen(self):
        """
        IDEM exportStations()
        """
        self.Vragen.ToonNotImplemented()

    def exportGebruikers(self):
        """
        IDEM exportStations()
        """
        self.Vragen.ToonNotImplemented()

    def exportTransporteurs(self):
        """
        IDEM exportStations()
        """
        self.Vragen.ToonNotImplemented()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    oBeheerder = Beheer()
    form = VeloView(oBeheerder)
    form.show()
    app.exec()

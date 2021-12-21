import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QInputDialog, QWidget, QApplication, QMessageBox, QVBoxLayout, QScrollArea, QMainWindow


class NieuweObjecten(QWidget):
    def __init__(self):
        super().__init__()

    def VraagStationInfo(self) -> tuple:
        naam, ok = QInputDialog.getText(self, 'Station toevoegen', 'Stationsnaam')
        if ok and naam:
            ID, ok = QInputDialog.getInt(self, 'Station toevoegen', 'StationID', 0, 0)
            if ok:
                aantal_plaatsen, ok = QInputDialog.getInt(self, 'Station toevoegen', 'Aantal plaatsen', 0, 0)
                if ok:
                    latitude, ok = QInputDialog.getText(self, 'Station toevoegen', 'Latitude')
                    if ok and latitude:
                        longitude, ok = QInputDialog.getText(self, 'Station toevoegen', 'Longitude')
                        if ok and longitude:
                            return naam, ID, aantal_plaatsen, latitude, longitude

    def VraagFietsInfo(self) -> int:
        fietsType, ok = QInputDialog.getInt(self, 'Fiets toevoegen', 'Geef het type fiets in', 0, 0, 100, 1)
        if ok:
            return fietsType

    def VraagGebruikerInfo(self, abonnementen: list) -> tuple:
        voornaam, ok = QInputDialog.getText(self, 'Gebruiker toevoegen', 'Voornaam')
        if ok and voornaam:
            achternaam, ok = QInputDialog.getText(self, 'Gebruiker toevoegen', 'Achternaam')
            if ok and achternaam:
                email, ok = QInputDialog.getText(self, 'Gebruiker toevoegen', 'Email')
                if ok and email:
                    abonnement_type, ok = QInputDialog.getItem(self, 'Gebruiker toevoegen',
                                                               'Selecteer het type abonnement', abonnementen, 0,
                                                               False)
                    if ok:
                        return voornaam, achternaam, email, abonnement_type

    def VraagTransporteurInfo(self) -> tuple:
        kenteken, ok = QInputDialog.getText(self, 'Transporteur toevoegen', 'Kenteken')
        if ok and kenteken:
            aantal_plaatsen, ok = QInputDialog.getInt(self, 'Transporteur toevoegen', 'Aantal plaatsen', 0, 0)
            if ok:
                return kenteken, aantal_plaatsen

    def ToonAnnulatie(self, wat: str) -> None:
        QMessageBox.information(self, "Annulatie", f"Er werd geen {wat} aangemaakt.")

    def ToonNotImplemented(self) -> None:
        QMessageBox.warning(self, "Aiai", "Aiai, deze functie is (nog) niet geïmplementeerd ;)")


class NieuwVenster(QMainWindow):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widget.setLayout(self.vbox)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        # Schakel close button uit want je hebt toch het menu via de main window
        self.setWindowFlag(QtCore.Qt.WindowType.WindowCloseButtonHint, False)
        # self.setGeometry(600, 100, 1000, 900)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NieuweObjecten()
    sys.exit(app.exec())

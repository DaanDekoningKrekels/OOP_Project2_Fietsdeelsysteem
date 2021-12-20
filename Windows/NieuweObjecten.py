import sys

from PyQt6.QtWidgets import QInputDialog, QLineEdit, QWidget, QApplication, QMessageBox


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
                                                               'Selecteer het type abonnement', abonnementen, 0, False)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NieuweObjecten()
    sys.exit(app.exec())

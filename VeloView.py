import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from Windows import MainWindow, NieuweObjecten


class VeloView(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VeloView, self).__init__(parent)
        self.setupUi(self)
        self.Vragen = NieuweObjecten.NieuweObjecten()
        # print(parent.actions())
        # .actionFiets.triggered.connect(lambda: self.printButtonPressed())

    def nieuwStation(self):
        try:
            naam, ID, aantal_plaatsen, latitude, longitude = self.Vragen.VraagStationInfo()
            print(naam, ID, aantal_plaatsen, latitude, longitude)
            ok = True
        except:
            self.Vragen.ToonAnnulatie("station")
            ok = False
        if ok:
            print("gelukt")

    def nieuwFiets(self):
        try:
            fietsType = self.Vragen.VraagFietsInfo()
            ok = True
        except:
            self.Vragen.ToonAnnulatie("fiets")
            ok = False
        if ok:
            print(fietsType)

    def nieuwGebruiker(self):
        try:
            gebruikerInfo = self.Vragen.VraagGebruikerInfo(["Jaarabonnement", "Weekpas"])
            ok = True
        except:
            self.Vragen.ToonAnnulatie("gebruiker")
            ok = False
        if ok:
            print(gebruikerInfo)

    def nieuwTransporteur(self):
        try:
            transporteurInfo = self.Vragen.VraagTransporteurInfo()
            ok = True
        except:
            self.Vragen.ToonAnnulatie("transporteur")
            ok = False
        if ok:
            print(transporteurInfo)

    def vensterStations(self):
        print("Geklikt2")

    def vensterFietsen(self):
        print("Geklikt2")

    def vensterGebruikers(self):
        print("Geklikt2")

    def vensterTransporteurs(self):
        print("Geklikt2")

    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')


def main():
    app = QApplication(sys.argv)
    form = VeloView()
    form.show()

    def doe():
        print("iets")

    # form.actionFiets.triggered.connect(doe())
    # if form.actionFiets.triggered():
    # for i in range(500):
    #     text = QLabel(f"Klik{i}")
    #     form.scrollArea.setWidget(text)

    app.exec()


if __name__ == '__main__':
    main()

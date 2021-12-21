import sys

from PyQt6.QtWidgets import QApplication

from Beheer import Beheer
from VeloView import VeloView

app = QApplication(sys.argv)
oBeheerder = Beheer()
form = VeloView(oBeheerder)
form.show()
app.exec()

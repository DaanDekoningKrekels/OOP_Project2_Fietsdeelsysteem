from datetime import datetime

from FietsSysteem import *

oFietsStation = FietsStation("Hier", 1, 10, 5, 4)
oFietsStation.voeg_fiets_toe(Fiets(1, 3))
print(oFietsStation)
oKlant = Klant(1, "Jan", "Janssen", "mailaders", JaarKaart(datetime.now()))
oFietsStation.ontleen_fiets(oKlant)
print(oFietsStation)
oFietsStation.plaats_fiets_terug(oKlant)
print(oFietsStation)

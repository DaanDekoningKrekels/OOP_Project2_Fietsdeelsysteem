from datetime import datetime

from FietsSysteem import *

oFietsStation1 = FietsStation("Centraal Station - Astrid", 1, 32, "51.21798654307154", "4.420624304044165")
oFietsStation2 = FietsStation("Centraal Station - Astrid 2", 2, 32, "51.21771096036532", "4.420667211070502")
oFietsStation3 = FietsStation("Centraal Station - Kievit 2", 3, 32, "51.213237097511296", "4.421803495141187")
oFietsStation1.voeg_fiets_toe(
    Fiets(1, 3),
    Fiets(2, 2)
)
oFietsStation1.voeg_fiets_toe(Fiets(3, 2))
print(oFietsStation1)

oTransporteur = Transporteur("AZE-123", 32)
oTransporteur.station_legen(oFietsStation1, 2)
print(oTransporteur)
oTransporteur.station_bijvullen(oFietsStation2, 1)
oTransporteur.station_bijvullen(oFietsStation3, 1)

oKlant1 = Klant(1, "Jan", "Janssen", "mailaders", JaarKaart(datetime.now()))
oKlant2 = Klant(2, "Roland", "Verbruggen", "mailaders", JaarKaart(datetime.now()))

oFietsStation1.ontleen_fiets(oKlant1)
print(oFietsStation1)
oFietsStation2.plaats_fiets_terug(oKlant1)
print(oFietsStation1)

oFietsStation2.ontleen_fiets(oKlant2)
oFietsStation3.plaats_fiets_terug(oKlant2)

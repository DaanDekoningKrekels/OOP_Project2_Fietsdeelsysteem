from FietsSysteem import *

oFietsStation1 = FietsStation("Centraal Station - Astrid", 1, 32, "51.21798654307154", "4.420624304044165")
oFietsStation2 = FietsStation("Centraal Station - Astrid 2", 2, 32, "51.21771096036532", "4.420667211070502")
oFietsStation3 = FietsStation("Centraal Station - Kievit 2", 3, 32, "51.213237097511296", "4.421803495141187")
oFietsStation1.voeg_fiets_toe(
    Fiets(1, 1),
    Fiets(2, 1),
    Fiets(3, 1),
    Fiets(4, 2),
    Fiets(5, 2),
    Fiets(6, 2),
    Fiets(7, 3),
    Fiets(8, 3)
)
oFietsStation1.voeg_fiets_toe(Fiets(3, 2))
print(oFietsStation1)

oTransporteur = Transporteur("AZE-123", 32)
oTransporteur.station_legen(oFietsStation1, 5)
print(oTransporteur)
oTransporteur.station_bijvullen(oFietsStation2, 2)
oTransporteur.station_bijvullen(oFietsStation3, 10)

print(oFietsStation1)
print(oFietsStation2)
print(oFietsStation3)

oKlant1 = Klant(1, "Jan", "Janssen", "mailaders", JaarKaart(datetime.now()))
oKlant2 = Klant(2, "Roland", "Verbruggen", "mailaders", JaarKaart(datetime.now()))
oKlant3 = Klant(3, "Lisse", "Gevers", "mailaders", Weekpas(datetime.now()))
oKlant4 = Klant(4, "Viktor", "Verbruggen", "mailaders", Dagpas(datetime.now()))
oKlant5 = Klant(5, "Stein", "Dekoning", "mailaders", Weekpas(datetime.now()))

oFietsStation1.ontleen_fiets(oKlant1)
oFietsStation2.ontleen_fiets(oKlant5)
oFietsStation2.ontleen_fiets(oKlant4)
oFietsStation2.ontleen_fiets(oKlant3)
oFietsStation2.ontleen_fiets(oKlant2)
oFietsStation2.plaats_fiets_terug(oKlant1)
oFietsStation2.ontleen_fiets(oKlant2)
print(oFietsStation1)

oFietsStation2.ontleen_fiets(oKlant2)
oFietsStation3.plaats_fiets_terug(oKlant2)
oFietsStation3.plaats_fiets_terug(oKlant3)
oFietsStation3.plaats_fiets_terug(oKlant4)
oKlant5.fiets.fiets_kapot()
oFietsStation3.plaats_fiets_terug(oKlant5)

oTransporteur.station_legen(oFietsStation3, 2)
oTransporteur.fietsen_fixen()

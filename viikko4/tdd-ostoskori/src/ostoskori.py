from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self.kori)

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.kori)

    def lisaa_tuote(self, lisattava: Tuote):
        for i in range(len(self.kori)):
            if self.kori[i].tuotteen_nimi() == lisattava.nimi():
                self.kori[i].muuta_lukumaaraa(1)
                return

        self.kori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on

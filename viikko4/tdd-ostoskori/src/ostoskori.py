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
        indeksi = self._etsi_indeksi(lisattava)
        if type(indeksi) is int:
            self.kori[indeksi].muuta_lukumaaraa(1)
            return

        self.kori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        indeksi = self._etsi_indeksi(poistettava)
        if type(indeksi) is int:
            self.kori[indeksi].muuta_lukumaaraa(-1)
            if self.kori[indeksi].lukumaara() == 0:
                self.kori.pop(indeksi)


    def tyhjenna(self):
        self.kori = []

    def ostokset(self):
        return self.kori

    def _etsi_indeksi(self, tuote: Tuote):
        for i in range(len(self.kori)):
            if self.kori[i].tuotteen_nimi() == tuote.nimi():
                return i
        return None

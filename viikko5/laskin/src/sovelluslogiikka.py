class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.arvolista = [0]  

    def nollaa(self):
        self.tulos = 0
        self.arvolista = [0]

    def aseta_arvo(self, arvo):
        self.tulos = arvo
        self.arvolista.append(arvo)

    def lisaa_syote(self, syote):
        self.syotelista.append(syote)

    def viimeisin_syote(self):
        return self.syotelista[-1]

    def viimeisin_arvo(self):
        return self.arvolista[-1]

    def palaa_taaksepain(self):
        if len(self.arvolista) >= 2:
            self.arvolista.pop()
            return self.arvolista.pop()
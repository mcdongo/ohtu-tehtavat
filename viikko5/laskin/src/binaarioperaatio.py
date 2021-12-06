class BinaariOperaatio:
    def __init__(self,sovellus,syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        return self.laske()

    def laske(self):
        return 0

class Summa(BinaariOperaatio):
    def __init__(self,io,syote):
        super().__init__(io,syote)

    def laske(self):
        self.sovellus.aseta_arvo(self.sovellus.viimeisin_arvo()+self.syote())

class Erotus(BinaariOperaatio):
    def __init__(self,io,syote):
        super().__init__(io,syote)

    def laske(self):
        self.sovellus.aseta_arvo(self.sovellus.viimeisin_arvo()-self.syote())

class Nollaus(BinaariOperaatio):
    def __init__(self,io,syote):
        super().__init__(io,syote)

    def laske(self):
        self.sovellus.nollaa()

class Kumoa(BinaariOperaatio):
    def __init__(self,io,syote):
        super().__init__(io,syote)

    def laske(self):
        self.sovellus.aseta_arvo(self.sovellus.palaa_taaksepain())
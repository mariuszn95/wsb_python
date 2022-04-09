class Samochod:
    def init(self, kolor, marka):
        self.kolor = kolor
        self.marka = marka
        self.paliwo = 0

    def zatankuj(self, ile):
        self.paliwo += ile

    def run(self):
        if self.paliwo < 15:
            print("Za malo paliwa")
        else:
            print(
                "Wszystko gotowe, jedziemy {} {}".format(
                    self.kolor, self.marka
                )
            )


s1 = Samochod()
s2 = Samochod()

s1.init("czerwony", "fiat")
s2.init("czarny", "bmw")

s1.zatankuj(20)

s1.run()
s2.run()

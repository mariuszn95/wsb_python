class Samochod:
    def init(self, kolor, marka):  # PEP8 określa nazwę pierwszego parametru
        self.kolor = kolor
        self.marka = marka

    def run(self):
        ...
        print("Wszystko gotowe, jedziemy {} {}".format(self.kolor, self.marka))


s1 = Samochod()
s2 = Samochod()

s1.init("czerwony", "fiat")
s2.init("czarny", "bmw")

s1.run()
s2.run()

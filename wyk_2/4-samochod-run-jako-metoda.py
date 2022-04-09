class Samochod:
    def init(sam, kolor, marka):
        sam.kolor = kolor
        sam.marka = marka

    def run(sam):
        ...
        print("Wszystko gotowe, jedziemy {} {}".format(sam.kolor, sam.marka))


s1 = Samochod()
s2 = Samochod()

s1.init("czerwony", "fiat")
s2.init("czarny", "bmw")

s1.run()
s2.run()

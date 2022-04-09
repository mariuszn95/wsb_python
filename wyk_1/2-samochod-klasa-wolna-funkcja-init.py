class Samochod:
    pass


def init(sam, kolor, marka):
    sam.kolor = kolor
    sam.marka = marka


def run(sam):
    ...
    print("Wszystko gotowe, jedziemy {} {}".format(sam.kolor, sam.marka))


s1 = Samochod()
s2 = Samochod()

init(s1, "czerwony", "fiat")
init(s2, "czarny", "bmw")

run(s1)
run(s2)

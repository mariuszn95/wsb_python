class Samochod:
    def __init__(self, kolor, marka):
        self.kolor = kolor
        self.marka = marka
        self._paliwo = 0  # PEP8, zmienna prywatna

    def zatankuj(self):
        if self._paliwo > 90:
            print("Nie tankujemy wiecej")
        else:
            self._paliwo += 10

    def run(self):
        print("Stan paliwa:", self._paliwo)
        if self._paliwo < 15:
            print("Za malo paliwa")
        else:
            print(
                "Wszystko gotowe, jedziemy {} {}".format(
                    self.kolor, self.marka
                )
            )


s1 = Samochod("czerwony", "fiat")
s2 = Samochod("czarny", "bmw")

s1.zatankuj()
s1.zatankuj()
s1.zatankuj()
s1.zatankuj()
s1.zatankuj()
s1.zatankuj()
s1.zatankuj()
s1.zatankuj()
s1.zatankuj()
s1.zatankuj()
s1.zatankuj()

s1._paliwo = 200

s1.run()
s2.run()

class Samochod:
    def __init__(self, kolor, marka):
        self.kolor = kolor
        self.marka = marka
        self.__paliwo = 0  # PEP8, zmienna prywatna, interpreter weryfikuje

    def zatankuj(self):
        if self.__paliwo > 90:
            print("Nie tankujemy wiecej")
        else:
            self.__paliwo += 10

    def run(self):
        print("Stan paliwa:", self.__paliwo)
        if self.__paliwo < 15:
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

# s1.__paliwo = 200
print("paliwo:", s1.__paliwo)

s1.run()
s2.run()

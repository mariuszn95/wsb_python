# PEP8


class Samochod:
    def __init__(self, kolor, marka):
        self.kolor = kolor
        self.marka = marka
        self.__paliwo = 0  # PEP8

    def __str__(self):
        text = "Samochod {} {}, stan paliwa: {}".format(
            self.kolor, self.marka, self.__paliwo
        )
        return text

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

print(s1)  # s1.__str__()
print(s2)  # s2.__str__()

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

# dir()
# print(dir(s1))
s1._Samochod__paliwo = 200
print("paliwo:", s1._Samochod__paliwo)

s1.run()
s2.run()

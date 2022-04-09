class Samochod:
    def __init__(self, kolor, marka):
        self.kolor = kolor
        self.marka = marka
        self._paliwo = 0

    def __str__(self):
        return "{}, {}, {}".format(self.kolor, self.marka, self._paliwo)

    def zatankuj(self, ile):
        self._paliwo += ile

    def run(self):
        if self._czy_mamy_paliwo():
            ...
            print('Wszytko gotowe, jedziemy', self.kolor, self.marka, self._paliwo)
        else:
            print('Za malo paliwa')

    def _czy_mamy_paliwo(self):
        raise NotImplementedError("Zaimplementuj metode czy_mamy_paliwo")


class SamochodBenzyna(Samochod): # polimorfizm dynamiczny
    def _czy_mamy_paliwo(self):
        return self._paliwo >= 15

class SamochodLpg(Samochod):
    def _czy_mamy_paliwo(self):
        return self._paliwo >= 30

class SamochodElektryczny(Samochod):
    def __init__(self, kolor, marka):
        super().__init__(kolor, marka)
        self._paliwo = 90

    def _czy_mamy_paliwo(self):
        return self._paliwo >= 25

_s1 = SamochodBenzyna(kolor='czerwony', marka='fiat') # --> s1.__init__(kolor='czerwony', ...)
_s2 = SamochodLpg(kolor='czarny', marka='bmw') # --> s2.__init__(kolor='czarny', ...)

_s1.zatankuj(20)

_s1.run()
_s2.run()

print(_s1)  # s1.__str__()
print(_s2)  # s2.__str__()

# s1.__paliwo = 0
# print(s1.__paliwo)

# print(s1._Samochod__paliwo)

#dir(s1)
#python3 -i wyklad.py #wykonamy skrypt i zostawi konsolę/interpreter do wpisywania kodu (-i)
#python -i wyklad.py

#lista = list()
#lista = [] #Syntactic Sugar
#dir(lista)
#lista.count()
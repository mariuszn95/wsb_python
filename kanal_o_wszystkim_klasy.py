# =========================
# 25. Kurs Python 3 - Klasy i Obiekty (OOP)

class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        

    imie = "Sebastian"

    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + ", mam na imię " + self.imie + " lat " + str(self.wiek) + "."

obiekt = Czlowiek("Sebastian", 24)

print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))
obiekt2 = Czlowiek("Adrian", 18)
print(obiekt2.przedstawSie())

# =========================
# 27. Kurs Python 3 - Klasy - magiczne metody

import math

class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.odleglosc = math.sqrt(x**2 + y**2)

    def __add__(self, drugi):
        return Punkt2D(self.x + drugi.x, self.y + drugi.y)

    def __lt__(self, drugi):
        return self.odleglosc < drugi.odleglosc

    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y

    def __len__(self):
        return int(round(self.odleglosc, 0))

p1 = Punkt2D(2, 5)
p2 = Punkt2D(4, 5)
p3 = p1 + p2
print(p3.x)
print(p3.y)
print(p1 < p2)
print(p1.odleglosc)
print(p2.odleglosc)
print(p3 < p2)
print(p1 == p2)
print(p2 == p2)
print(len(p3))
print(p3.odleglosc)

# =========================
# 29. Kurs Python 3 - Klasy - hermetyzacja (ukrywanie danych)

class Test:
    __lista = []
    def dodaj(self, arg):
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._Test__lista.append("X")
print(obj.zdejmij())
print(obj._Test__lista)

# =========================
# 30. Kurs Python 3 - Klasy - metody klas oraz statyczne

class Człowiek2:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print("Nazywam się " + self.imie)

    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)
        
    @staticmethod    
    def przywitaj(arg):
        print("Cześć " + arg)

cz1 = Człowiek2.nowy_czlowiek("Sebastian")
cz1.przedstaw()
cz2 = cz1.nowy_czlowiek("Adrian")
cz2.przedstaw()
Człowiek2.przywitaj("przyjacielu")
cz2.przywitaj("człowieku.")

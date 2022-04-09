
try:
    plik = open("test.txt", "r")
    plik.write("Hello")
    plik.close()
except FileNotFoundError as e:
    print("Plik nie istnieje, utwórz plik")
    print(e)
except Exception as e:
    print("Nieznany błąd")

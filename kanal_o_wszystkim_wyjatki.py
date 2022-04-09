x = 12
y = 2

try:
    lista = [3]
    print(lista[0])
    print(x / y)
    print(x + 4)
    print("Linijka po")
except (ZeroDivisionError, TypeError) as e:
    print("Wystąpił 1 z 2 błędów!")
except:
    print("Inny błąd!")
finally:
    print("FINALLY: Wykonam się i tak!")

print("Dalsze instrukcje ...")

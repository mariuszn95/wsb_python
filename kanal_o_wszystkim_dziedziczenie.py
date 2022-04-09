from telnetlib import DO


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print("How How")

class Wolf(Dog):
    def getVoice(self):
        print("Jestem wilkiem, ")
        super().voice()

class Cat(Animal):
    def getVoice(self):
        print("Meow Meow")

dog = Dog("Reksio", 10)

print(dog.name)
print(dog.age)
dog.voice()

cat = Cat("Buty", 8)
cat.getVoice()

wolf = Wolf("Geralt", 55)
wolf.getVoice()
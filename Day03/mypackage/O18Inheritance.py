
class Animal:
    def __init__(self):
        print("Animal Ctor......")
        self.a = 10

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def __init__(self):
        super().__init__()
        print("Bird Ctor.....")
        self.b = 20

    def fly(self):
        print("Birds fly......")


cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()
print(cuckoo.__dict__)      # variable that cuckoo object can access


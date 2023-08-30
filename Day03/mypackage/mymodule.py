
gname = "Sachin Tendulkar"

sports = ['cricket', 'tennis', 'soccer', 'hockey']

runs = {'test': 18000, 'ODI': 23000, 't20': 2300}

def greet(gname):
    print(f"Greeting Mr. {gname}, Welcome to the event......")

class Player:

    def __init__(self, name, age):
        self.name  = name
        self.age = age


    def get_playerDetails(self):
        print(f"Name of the player is :{self.name}\nAge of the player is {self.age}")


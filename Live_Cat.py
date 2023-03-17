import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.walk = 10
        self.eating = 50
        self.Drinking = 50
        self.alive = True
    def to_walk(self):
        print("Time walk")
        self.gladness += 2
        self.walk += 10
        self.eating -= 10
        self.Drinking -= 10
    def to_eating(self):
        print("I will eating")
        self.gladness -= 3
        self.eating += 10
        self.Drinking -= 2

    def to_drinking(self):
        print("I will eating")
        self.gladness -= 3
        self.eating -= 2
        self.Drinking += 10
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 5
        self.eating -= 2
        self.Drinking -= 2
    def is_alive(self):
        if self.eating <= 0:
            print("Dead...")
        if self.Drinking <= 5:
            print("Dead...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Eating = {self.eating}")
        print(f"Drinking = {self.Drinking}")
        print(f"Walk = {self.walk}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_walk()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 2:
            self.to_sleep()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 4:
            self.to_eating()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 5:
            self.to_drinking()
            self.end_of_day()
            self.is_alive()

Barsik = Cat(name="Barsik")

for day in range(365):
    if Barsik.alive == False:
        break
    Barsik.live(day)
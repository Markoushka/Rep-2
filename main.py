import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.golod = 25
        self.hotenie_igrat = 5
        self.otdih = 50
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.golod -= 15
        self.hotenie_igrat += 1

    def to_play(self):
        print("Time to play")
        self.hotenie_igrat -= 2
        self.otdih -= 7
        self.golod += 5

    def relax(self):
        print("Relax time")
        self.otdih += 5
        self.hotenie_igrat += 1.2

    def is_alive(self):
        if self.golod >= 50:
            print("game over")
            self.alive = False
        elif self.hotenie_igrat >= 50:
            print("game over")
            self.alive = False
        elif self.otdih <= 5:
            print("game over")
            self.alive = False
    def end_of_day(self):
        print("Golod:", self.golod)
        print("Hotenie igrat:", self.hotenie_igrat)
        print("Otdih:", self.otdih)

    def live(self, day):
        print("Day", str(day), "of", self.name, "life")
        num = random.randint(1, 3)
        if num == 1:
            self.to_eat()
        elif num == 2:
            self.to_play()
        elif num == 3:
            self.relax()

        self.end_of_day()
        self.is_alive()

felix = Cat("Felix")
for day in range(366):
    if felix.alive == False:
        break
    felix.live(day)




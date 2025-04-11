import random as r

class Student:
    def __init__(self, name):
        self.name = name
        self.happy = r.randint(10, 100)
        self.progress = r.randint(0, 10)
        self.money = r.randint(50, 300)
        self.alive = True

    def study(self):
        self.happy -= r.randint(10, 30)
        self.progress += r.randint(5, 15)

    def chill(self):
        self.happy += r.randint(20, 50)
        self.progress -= r.randint(3, 8)
        self.money -= r.randint(10, 30)

    def sleep(self):
        self.happy += r.randint(10, 30)
        self.progress -= r.randint(3, 8)

    def work(self):
        self.money += r.randint(20, 50)
        self.happy -= r.randint(5, 15)
        self.progress -= r.randint(3, 5)

    def isAlive(self):
        if self.progress < 3 or self.money <= 0 or self.happy <= 0:
            self.alive = False

    def studylife(self, day):
        if self.money <= 0:
            self.work()
        elif self.happy <= 0:
            self.chill()
        elif self.progress < 3:
            self.study()
        else:
            r.choice([self.study, self.chill, self.sleep, self.work])()
        self.isAlive()

st1 = Student('Олег')
for k in range(365):
    if not st1.alive:
        break
    st1.studylife(k)

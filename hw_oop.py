# симулятор студента

import random as r
class Student:
    def __init__(self, name):
        self.name = name
        self.happy =  r.randint(10, 100)
        self.progress = r.randint(0, 10)
        self.alive = True
    def study(self):
        print('Час для навчання')
        self.happy -= r.randint(1, 50)
        self.progress -= r.randint(1, 15)
    def chill(self):
        self.happy+=r.randint(50, 100)
        self.progress -= r.randint(5, 10)
    def sleep(self):
        self.happy += r.randint(40, 80)
        self.progress -= r.randint(5, 10)
    def isAlive(self):
        if 1 < self.progress < 5:
            print('Ти на грані відрахування. Починай навчатися')
            self.alive = False
        elif self.progress <= 1:
            print('Відрахування з інституту')
            self.alive = False
        elif self.progress >= 5:
            print('Відмінно навчаєшся')
            self.alive = True
    def everyday(self):
        print("Рівень щастя", self.happy)
        print("Прогресс навчання", self.progress)
    def studylife(self, day):
        day="День №" + str(day)
        print(day)
        res=r.randint(1, 3)
        if res == 1:
            self.study()
        elif res == 2:
            self.chill()
        elif res == 3:
            self.sleep()
        self.everyday()
        self.isAlive()

st1=Student('Олег')
# print(st1.progress)
print("Життя студента", st1.name)
for k in range(7):
    if st1.alive==False:
        break
    st1.studylife(k)

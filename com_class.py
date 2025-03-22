class Human:
    count = 0

    def __init__(self, name="Вася"):
        self.name = name
        Human.count += 1

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def add(self, *args):
        for n in args:
            self.passenger.append(n)

    def info(self):
        if not self.passenger:
            print("Пасажирів відсутні у", self.brand)
        else:
            print("Пасажири присутні у", self.brand, ":")
            for n in self.passenger:
                print(n.name)

pas1 = Human()
pas2 = Human("Маша")
pas3 = Human("Люда")
car1 = Auto("Богдан")
car1.add(pas1, pas2, pas3)
car1.info()
print(Human.count)

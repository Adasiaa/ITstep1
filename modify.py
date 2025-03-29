# class Animal:
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         return "гав"
#
# class Cat(Animal):
#     def sound(self):
#         return "мяу"
#
# class Cow(Animal):
#     def sound(self):
#         return "му"
#
# def speak(an):
#     print(an.sound())
#
# a1=Dog()
# a2=Cat()
# a3=Cow()
# speak(a1)
# speak(a2)
# speak(a3)


# class Pay:
#     def process(self, money):
#         pass
# class Credit(Pay):
#     def process(self, money):
#         return "Оплата "+str(money)+ "грн здійснена через кридитнку картку"
#
# class Cash(Pay):
#     def process(self, money):
#         return "Оплата " +str(money)+ "грн здійснена через готівку"
#
# class System(Pay):
#     def process(self, money):
#         return  "Оплата "+str(money)+"грн здійснена через онлайн систему"
#
# buy=[Credit(),Credit(),System()]
# num=int(input('Введіть суму покупки: '))
# for k in buy:
#     print(k.process(num))



# class Dog:
#     def __init__(self, name):
#         self.name = name
#
# dog1=Dog("Сінді")
# print(dog1.name)


# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 2
#     def info(self):
#         return self.__age
#
# dog1=Dog("Сінді")
# print(dog1.info())


# class Dog:
#     def __init__(self, name):
#         self._breed="бульдог"
# class D (Dog):
#     def info(self):
#         return "Це щеня породи "+self._breed
# dog1=D("Сінді")
# print(dog1.info())

# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary
#     def info(self):
#         print("Вітаю! Мене звати", self.name)
#         self._infoAge()
#         self.__infoSalary()
#     def _infoAge(self):
#             print('Мій вік', self.age)
#     def __infoSalary(self):
#         print('Моя ЗП', self.__salary)
# class Employee(Person):
#     def __init__(self, name, age, salary, pos):
#         super().__init__(name, age, salary)
#         self.pos=pos
#     def printInfo(self):
#         print('Моя посада', self.pos)
#         print('Мій вік', self.age)
#         # print('Моя ЗП', self.__salary) помилка у достуі захищенності
#
# human=Person('Олеся', 20, 2000)
# emp=Employee('Петро', 25, 45000, 'інженер')
# print(human.name)
# human.info()
# print(emp.name)
# emp.printInfo()
# print(emp.age)
# print(emp._Person__salary)


import random as r


class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = r.randint(0, 100)

    def infoName(self):
        return self.__name

    def infoHP(self):
        return self.__health

    def attack(self):
        pass

    def take_damage(self):
        self.__health -= r.randint(0, 10)

    def is_alive(self):
        return self.__health > 0

    def __str__(self):
        return self.__name + " моє здоров'я: " + str(self.__health)


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, r.randint(80, 120))

    def attack(self):
        return ". Я атакую мечем"


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, r.randint(30, 80))

    def attack(self):
        return ". Я атакую магією"


warrior = Warrior("Мене звати Артур")
mage = Mage("Мене звати Генадій")

print(str(warrior)+warrior.attack())
print(str(mage)+mage.attack())

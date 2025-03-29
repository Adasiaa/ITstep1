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


class Pay:
    def process(self, money):
        pass
class Credit(Pay):
    def process(self, money):
        return "Оплата "+str(money)+ "грн здійснена через кридитнку картку"

class Cash(Pay):
    def process(self, money):
        return "Оплата " +str(money)+ "грн здійснена через готівку"

class System(Pay):
    def process(self, money):
        return  "Оплата "+str(money)+"грн здійснена через онлайн систему"

buy=[Credit(),Credit(),System()]
num=int(input('Введіть суму покупки: '))
for k in buy:
    print(k.process(num))
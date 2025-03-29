# class Car:
#    def __init__(self, speed):
#       self.speed=speed
#   def info(self):
#       print(print("Швидкість авто: ",self.speed))

# sp=int(input('Максимальна швидкість авто: '))
# auto=Car(sp)
#auto.info()
#auto2=Car(180)
#auto2.info()


class Pupils:
    count=0
    def __init__(self,name,height):
        self.name = name
        self.height = height
        Pupils.count+=1
        def __str__(self):
            print("Ім'я учасника: ", self.name,"Зріст: ", self.height)
        def __bool__(self):
            return self.name!=None
        def __len__(self):
            return self.height

p1=Pupils("Саша", 160)
p1.__str__()
p2=Pupils("Соня", 150)
p2.__str__()
p3=Pupils("Ігор", 155)
print(p1.count,"учасника змагань")
print(bool(p2))
print(len(p3))


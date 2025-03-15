class Car:
    def __init__(self, speed):
        self.speed=speed
    def info(self):
        print(print("Швидкість авто: ",self.speed))

sp=int(input('Максимальна швидкість авто: '))
auto=Car(sp)
auto.info()
auto2=Car(180)
auto2.info()
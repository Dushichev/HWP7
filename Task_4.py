#Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
#speed, color, name, is_police (булево).
#А также публичные методы: go, stop, turn(direction),
#которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#Добавьте в базовый класс публичный метод show_speed,
#который должен показывать текущую скорость автомобиля.
#Для классов TownCar и WorkCar переопределите метод show_speed.
#При значении скорости свыше 60 (TownCar)
#и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
#Выполните доступ к атрибутам, выведите результат.
#Выполните вызов методов и также покажите результат.


class Car:
    speed = 0
    color = "grey"
    name = "cat"
    is_police = bool

    def __init__(self,color: str,name: str,speed: int,is_police: bool):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self,start):
        self.start = start                                         #сделал тумблер старт,где 1 == зажигание
        if start == 1:
            print(f"машина {self.color} {self.name} стартовала")
       

    def turn(self, direction):
        if self.start == 1:
            print(f'{self.name} движется {direction}')
        else:
            print(f"{self.name} неподвижна")


    def show_speed(self, speed):
        self.speed = speed
        if self.start == 1:
            print(f'Скорость движения {self.speed} км/ч')
        if self.speed  > 60 and not self.is_police :                             #пихнул проверку на скорость,что бы избежать
            print('Внимание! Превышение допустимой скорости,равной 60 км/ч')     #лишних действий в кдассах TownCar, SportCar
       


class Police_Car(Car):
    def __init__(self,color,name,speed,is_police):
        super().__init__(color, name, speed, is_police)
        print(f"автомобиль {self.color} {self.name} является полицейским")

class TownCar(Car):
   def __init__(self,color,name,speed,is_police):
        super().__init__(color, name, speed, is_police)
        print(f"автомобиль {self.color} {self.name} является городским")

class SportCar(Car):
   def __init__(self,color,name,speed,is_police):
        super().__init__(color, name, speed, is_police)
        print(f"автомобиль {self.color} {self.name} является спортивным")

class WorkCar(Car):
   def __init__(self,color,name,speed,is_police):
        super().__init__(color, name, speed, is_police)
        print(f"автомобиль {self.color} {self.name} является служебным") 

   def show_speed(self, speed):
        self.speed = speed
        if self.start == 1:
            print(f'Скорость движения {self.speed} км/ч')
        if self.speed  > 40:              
            print('Внимание! Превышение допустимой скорости равной 40 км/ч!')    
          
          

my_car = Car("черный","поло седан",100,False)
my_car.go(1)
my_car.turn("прямо")
my_car.show_speed(90)
print("-------------------------------------------------")
police_car = Police_Car("сине-белый","форд-фокус",100,True)
police_car.go(1)
police_car.turn("назад")
police_car.show_speed(70)
print("-------------------------------------------------")
work_car = WorkCar("красно_белый","газель",100,False)
work_car.go(1)
work_car.turn("вперёд")
work_car.show_speed(50)
print("-------------------------------------------------")
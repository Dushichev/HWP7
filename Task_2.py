#Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
#length (длина в метрах), width (ширина в метрах).
#Значения данных атрибутов должны передаваться при создании экземпляра класса.
#Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
#всего дорожного полотна.
#Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
#метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
#Массу и толщину сделать публичными атрибутами.
#Проверить работу метода.
#Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class Road:
    length = 0
    width = 0

    def __init__(self, length, width, weight, depth):
        self.length = length
        self.width = width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self.length
        wid = self.width
        w = self.weight
        dep = self.depth
        res = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", res, "т")


result = Road(12, 1234, 15, 3)
result.mass()
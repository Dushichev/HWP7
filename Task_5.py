#Реализовать класс Stationery (канцелярская принадлежность).
#Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
#Метод выводит сообщение “Запуск отрисовки.”
#Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
#В каждом из классов реализовать переопределение метода draw.
#Для каждого из классов метод должен выводить уникальное сообщение.
#Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.




class Stationery:
     def __init__(self,title:str):
        self.title = title                
        print(f"используется концелярская пренадлежность:")
     def draw(self):                                  
        return print(f"запуск отрисовки:")
    
class Pen(Stationery):
    def __init__(self,title:str):
        super().__init__(title)
        print(f"{self.title}")

    def draw(self):
        print(f"отрисовка:{self.title},с гелевой пастой")      
     
class Pencil(Stationery):
     def __init__(self,title:str):
        super().__init__(title)
        print(f"{self.title}")

     def draw(self):
        print(f"отрисовка:{self.title},с мягким стержнем")   

class Handle(Stationery):
     def __init__(self,title:str):
        super().__init__(title)
        print(f"{self.title}")

     def draw(self):
       print(f"отрисовка:{self.title},с водоотталкивающей основой ") 
            
res =  Stationery("концелярская пренадлежность") 
res.draw()
print("-------------------------")
res = Pen("ручка")
res.draw()
print("-------------------------")
res = Pencil("карандаш")
res.draw()
print("-------------------------")
res = Handle("маркер")
res.draw()
print("-------------------------")
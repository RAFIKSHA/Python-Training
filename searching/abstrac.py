from abc import ABC, abstractmethod   
class Car(ABC):  
    @abstractmethod  
    def mileage(self):   
        pass  
  
class Tesla(Car):  
    a=10
    b="hello" 
    # def mileage(self):   
    #     print("The mileage is 30kmph")   
# class Suzuki(Car):   
#     def mileage(self):   
#         print("The mileage is 25kmph ")   
# class Duster(Car):   
#      def mileage(self):   
#           print("The mileage is 24kmph ")   
  
# class Renault(Car):   
#     def mileage(self):   
#             print("The mileage is 27kmph ")   
          
# # Driver code   
t= Tesla ()   
t.mileage()   
  

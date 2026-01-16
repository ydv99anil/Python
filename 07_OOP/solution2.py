# Problem 1: Create a Car class with attributes like brand and model. Then create an instance of this class:
# Basic Class and Object

class Car:
    totalCar = 0 #Problem 6 done ✅
    def __init__(self, brand, model):
        self.__brand = brand # before encapsulation self.brand Problem 4 
        self.__model = model
        Car.totalCar += 1 #Problem 6 done ✅
        

    #Problem 2 done ✅
    def carDetails(self): 
        return f"This car is {self.__brand} - {self.__model}"
    # before encapsulation self.brand
    
    #Problem 4 done ✅
    def getBrand(self): 
        return self.__brand
    
    #Problem 5 done ✅
    def fuelType(self):
        return "Petrol or Diesel"
    
    #Problem 7 done ✅
    @staticmethod
    def generalDesciption():
        return "Cars are means of public transport"
    
    @property
    def model(self):
        return self.__model
    

    
myCar1 = Car("Mahindra", "Scorpio")


print(myCar1.getBrand())
print(myCar1.model)


class ElectricCar(Car):
    totalEVs = 0
    name = "Electric Car"
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model) #Problem 3 done ✅
        self.batterySize = batterySize
        ElectricCar.totalEVs += 1

    def newCarDetails(self):
        return self.carDetails() + f" and its battery size is: {self.batterySize}"
    
    #Problem 5 done ✅
    def fuelType(self): # this is a Instance method in Python-OOP
        # print(f"{self.name}")   ** Not Correct **
        return f"Electric Charge: {self.getBrand()}, {self.name}"
    
    #Problem 7 done ✅
    @staticmethod # access values from class by class name only
    def generalDesciption(): # Static method
        return f"Cars are means of public transport: {ElectricCar.name}"
    
    @classmethod # access values from class by cls argument
    def carClassMethod(cls): # Class Method
        return f"{cls.name}"
    

EV1 = ElectricCar("Tiago", "Roxx", "100 kWh")

print(EV1.getBrand())
print(EV1.model)
print(EV1.batterySize)

print(EV1.newCarDetails())
print(EV1.carDetails())


# Problem 9: Demonstrate the use of isinstance() to check if myCar1 is an instance of Car and ElectricCar:
# Class Inheritance and isinstance() Function

print(isinstance(myCar1, Car))
print(isinstance(myCar1, ElectricCar))
print(isinstance(EV1, Car))
print(isinstance(EV1, ElectricCar))



# Problem 10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance:
# Multiple Inheritance

class Battery:
    def batteryInfo(self):
        return "This is battery info class"


class Engine:
    def engineInfo(self):
        return "This is Engine Info class"


class ElectricCar2(Battery, Engine, Car):
    pass

newEV = ElectricCar2("Tesla", "Model S")

print(newEV.engineInfo())
print(newEV.batteryInfo())
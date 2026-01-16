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
myCar2 = Car("Tata", "Sierra")
myCar3 = Car("Maaruti", "Suzuki")

# print(myCar1.brand) # ** before Encapsulation **
print(myCar1.getBrand())
print(myCar1.model)

# Problem 2: Add a method to the Car class that displays the full name of the car (brand and model):
# Class Method and Self

print(myCar1.carDetails())
print(myCar2.carDetails())
print(myCar3.carDetails())



# Problem 3: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size:
# Inheritance

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
EV2 = ElectricCar("Tata", "EV2", "400 kWh")

# print(EV1.brand) # before encapsulation self.brand
print(EV1.getBrand())
print(EV1.model)
print(EV1.batterySize)

print(EV1.newCarDetails())
print(EV1.carDetails())



# Problem 4: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it:
# Encapsulation

print("Encapsulation Here: ✅")
#Problem 3 done ✅
#    def getBrand(self): 
#        return self.__brand


# Problem 5: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors:
# Polymorphism

print("Polymorphism Here: ✅")

# yhaa fuelType alag kaam krega
print(myCar1.model, ":", myCar1.fuelType())
print(myCar2.model, ":", myCar2.fuelType())
print(myCar3.model, ":", myCar3.fuelType())

# yhaa fuelType alag kaam krega
print(EV1.model, ":", EV1.fuelType())



# Problem 6: Add a class variable to Car that keeps track of the number of cars created:
# Class Variables

print(Car.totalCar)
print(ElectricCar.totalCar)
print(ElectricCar.totalEVs)



# Problem 7: Add a static method to the Car class that returns a general description of a car:
# Static Method

print(Car.generalDesciption())
print("Static Method: ",ElectricCar.generalDesciption())
print("Instance Method: ", EV1.fuelType()) # Can access through the oblect only not by class
print("Class Method: ", ElectricCar.carClassMethod())


# Problem  8: Use a property decorator in the Car class to make the model attribute read-only.
# Property Decorators

print(myCar1.model) # = Scorpio

# Before use of decorator it works fine ->
print(myCar1.model, ": Yhaa decorator ka use krke humne model read only bnaa diya abb ese change nhii krr payenge")
# myCar1.model = "Bolero ZLx"
# print(myCar1.model()) # = Bolero ZLx
print(myCar1.model) # = Scorpio Abb change nhii hoga 

# After the use of Decorator: here line 138 and all car.model create an error that object has no attribute "model" so now we have to define the decorator i.e:
#   @property
#   def model(self): 
#       return self.__model
# Yhaa function ka naam same rkhenge taki hum usko ek property i.e model ki trh access krr ske
print("Problem 8 completed")


# Problem 9: Demonstrate the use of isinstance() to check if myCar1 is an instance of Car and ElectricCar:
# Class Inheritance and isinstance() Function

print(isinstance(myCar1, Car))
print(isinstance(myCar1, ElectricCar))
print(isinstance(EV1, Car))
print(isinstance(EV1, ElectricCar))

# Problem 10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance:
# Multiple Inheritance
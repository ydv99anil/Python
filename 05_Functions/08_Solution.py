# Create a function that accepts any number of keyword arguments and prints them in the format key: value:



# **kwargs FUNCTIONING

def kwargsFunc(**kwargs):
   
    for key, value in kwargs.items():
        print(f"{key} : {value}")

name = input("name?:")
age = input("age?:")
gradYear = input("Graduation Year?:")

kwargsFunc(name=name, age=age, gradYear=gradYear)

kwargsFunc(name="Anil Yadav", age="23", gradYear="2026")




# NORMAL FUNCTIONING

name = input("name?:")
age = input("age?:")
gradYear = input("Graduation Year?:")

def userDetails(name, age, gradYear):
    name = print("Name: ", name)
    age = print("Age: ", age)
    gradYear = print("Graduation Year: ", gradYear)
    # return name, age, gradYear  ## this return is not required and not correct

userDetails(name=name, age=age, gradYear=gradYear)

userDetails(name="Anil Yadav", age="23", gradYear="2026")
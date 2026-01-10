travelDistance = int(input("How long you are going(In KMs): "))

if travelDistance < 3:
    mode = "Walk"
elif travelDistance <= 15:
    mode = "Bike"
else: mode = "Car"

print("You should travel by:", mode)
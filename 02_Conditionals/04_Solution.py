fruit = input("Fruit Name: ")


if fruit != "Banana":
    print("Your fruit must be Banana!")
    exit()

fruitColor = input("What's the color of fruit: ").lower()

if fruit == "Banana":
    if fruitColor == "green":
        print("It is Unripe")
    elif fruitColor == "yellow":
        print("It is Ripe")
    elif fruitColor == "brown": 
        print("It is Overripe")
    else: print("Please give the correct color name!")
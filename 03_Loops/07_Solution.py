# Keep asking the user for input until they enter a number between 1 and 10:

while True:
    inputNumber = int(input("Pick a number b/w 1 and 10: "))
    if 1 <= inputNumber <= 10:
        print("Your pick is correct 👌")
        break
    else: print("Please pick a correct number!")
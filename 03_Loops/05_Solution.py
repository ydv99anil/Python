# Given a string, find the first non-repeated character:

string = input("String: ").strip().lower()

for char in string:
    print(char)
    if string.count(char) == 1:
        print("Char is:", char)
        break
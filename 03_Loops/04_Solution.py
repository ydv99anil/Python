# Reverse a string using a loop:

inputString = input("String: ").strip()
reversedString = ""

for char in inputString:
    reversedString = char + reversedString
print(reversedString)
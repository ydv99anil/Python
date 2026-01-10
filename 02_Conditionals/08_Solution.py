password = input("Enter password: ")
passLength = len(password)

if passLength == 0:
    print("Please first enter the password!")
    exit()

if passLength < 6:
    strength = "Week"
elif passLength <= 10:
    strength = "Moderate"
else: strength = "Strong"

print("Your password are:", strength)
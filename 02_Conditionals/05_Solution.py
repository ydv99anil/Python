whether = input("What's the whether here: ").strip().lower()

if whether == "sunny":
    activity = "Let's go for a walk"
elif whether == "rainy":
    activity = "Ohh!, You should read a book."
elif whether == "snowy":
    activity = "Build a Snowman 😍"
else: activity = "Stay Safe!"

print(activity)
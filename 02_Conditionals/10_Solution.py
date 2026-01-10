petSpecies = input("Pet's Species(Dog/Cat): ").lower().strip()

if petSpecies not in ("dog", "cat"):
    print("Please write Cat/Dog speacies only!")
    exit()

petAge = int(input("Pet's Age: "))

if petSpecies == "dog":
    if petAge < 2:
        food = "Light Puppy Food"
    elif petAge <= 5:
        food = "Puppy Food"
    else: food = "Senior Dog Food"
elif petSpecies == "cat":
    if petAge < 2:
        food = "Light Cat Food"
    elif petAge <= 5:
        food = "Cat Food"
    else: food = "Senior Cat Food"

print("Suggested Food: ", food)
orderSize = input("Order Size - Small, Medium, Large:").lower().strip()
extraShot = input("You want Extra Shot? :").lower().strip() == "yes"

if extraShot:
    coffee = orderSize + " Coffee with extra shot"
else: coffee = orderSize + " Coffee without extra shot"

print("Order: ", coffee)
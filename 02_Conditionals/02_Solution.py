age = int(input("Tell your age: "))
day = input("Today is: ").lower()

# if age < 18:
#     price = 60
# else: price = 100

price = 60 if age < 18 else 100

if day == "wednesday":
    discount = price * 0.2
    # price = price - discount
    price -= discount

print("Pay for ticket: Rs.", int(price))
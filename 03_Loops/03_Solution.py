# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("Number:"))

for i in range(1,11):
    if i != 5:
        print(num, "X", i, "=", num*i)
        # print(num * i)

for i in range(1,11):
    if i == 5:
        continue # 5th iteration ko gayab krr dega 
    print(num, "X", i, "=", num*i)
    # print(num * i)
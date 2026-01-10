# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) > 1:
        print(item)

# Another Method:
# SET = only stores unique item

uniqueItem = set()

for item in items:
    if item in uniqueItem:
        print("Duplicate Item: ", item)
        break
    uniqueItem.add(item)
print("Unique Set:",uniqueItem)
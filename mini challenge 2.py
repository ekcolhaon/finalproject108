groceries = ["bread", "apples", "bananas", "chicken", "rice"]

print("First item:", groceries[0])
print("Last item:", groceries[-1])

print("First 3 items:", groceries[:3])

groceries.append("eggs")

groceries.insert(0, "milk")
groceries.remove("rice")

if "bread" in groceries:
    print("Bread is in the grocery list!")
else:
    print("Bread is not in the grocery list.")

groceries.sort()
print("Sorted grocery list:", groceries)

print("Total items:", len(groceries))

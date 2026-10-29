# 1. Create a tuple with at least 5 items
travel_bag = ("shirt", "toothbrush", "shoes", "pants", "socks")

# 2. Print the second and fourth items
print("Second item:", travel_bag[1])
print("Fourth item:", travel_bag[3])

# 3. Check if shoes are in the bag
if "shoes" in travel_bag:
    print("You're ready to walk!")
else:
    print("You forgot your shoes!")

# 4. Create a tuple with 3 essentials
essentials = ("passport", "phone", "wallet")

# 5. Combine both tuples
final_bag = travel_bag + essentials

# 6. Print the total number of items
print("Total items:", len(final_bag))

# 7. Print the last item
print("Last item:", final_bag[-1])
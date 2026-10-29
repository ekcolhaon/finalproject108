first = 10
second = 3
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
print(f"{first} * {second} = {first * second}")
print(f"{first} / {second} = {first / second}")
print(f"{first} // {second} = {first // second}")  # Floor division
print(f"{first} % {second} = {first % second}")    # Remainder
print(f"{first} ** {second} = {first ** second}")  # Exponent

budget = 100
print("Starting budget:", budget)
budget += 20
print("After += 20:", budget)
budget -= 10
print("After -= 10:", budget)
budget *= 2
print("After *= 2:", budget)
budget /= 2
print("After /= 2:", budget)

print("Equal:", first == second)
print("Not equal:", first != second)
print("Greater than:", first > second)
print("Less than:", first < second)
print("Greater than or equal:", first >= second)
print("Less than or equal:", first <= second)

age = 25
has_ticket = True
print("May enter:", age >= 18 and has_ticket)
print("Discount eligible:", age < 18 or age >= 65)
print("Missing ticket:", not has_ticket)
print("Membership:", "Python" in ["Python", "React"])
print("Not a member:", "Java" not in ["Python", "React"])

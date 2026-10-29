print("Hello world from Python!")
# Printing text
print("Hello World")

# Variables
name = "Leo"
age = 24

# Data types
# String = text
# Integer = whole number
# Float = decimal number
# Boolean = True or False

print("Welcome to Python")
name = "Leo"
age = 24
print(name, age)

# Concatenation (putting things together)
# Cant concatenate strings and integers together
#print("Hello my name is " + name + " and my age is " + age) str() converts to string
print("Hello my name is " + name + " and my age is " + str(age))

name = "Leo"
age = 24
city = "Los Angeles"
money = 500
is_happy = True

print("My name is " + name + " and I am " + str(age) + " years old.")
print("I live in " + city + " and I have $" + str(money) + " saved up.")
print("One day, I decided to explore " + city + " and start a new adventure.")
print("I had $" + str(money) + " to spend on my trip.")
print("Am I happy about my adventure? " + str(is_happy))
members = 5
print("The last time I went to " + place + ", I had a great time " + activity + " with " + str(members) + " of my friends.")

# F-STRING: always start with f""
print(f"The last time I went to {place}, I had a great time {activity} with {members} of my friends.")

# Multiline f format: f""" """ or f''' '''
print(f"""The last time I went to {place},
        I had a great
    time {activity} with {members}
                of my friends.""")
# input() always returns a string
print(type(input("Enter your name: ")))

# Ex: converting input to int
new_age = int(input("Enter your age: "))
print(age + new_age)

# Pizza Calculator

# Ask the user for two inputs
slices = int(input("How many slices of pizza do you have? "))
people = int(input("How many people are sharing the pizza? "))

# Calculate slices per person
slices_per_person = slices / people

# Show the result using an f-string
print(f"Each person gets {slices_per_person} slices of pizza!")
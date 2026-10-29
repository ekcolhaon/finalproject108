x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


# MINI CHALLENGE: Club Entry

age = int(input("Enter your age: "))

has_id = input("Do you have a valid ID? (yes/no): ").lower()

can_enter = age >= 21 and has_id == "yes"

if age < 0:
    print("Invalid age entered.")

elif age >= 21 and has_id == "yes":
    print("Access Granted")

elif age >= 21 and has_id == "no":
    print("Access Denied - ID Required")

elif age >= 18 and age <= 20:
    print("Access Limited")

else:
    print("Access Denied - Too Young")

if can_enter:
    print("Welcome inside!")
else:
    print("Please see the front desk.")

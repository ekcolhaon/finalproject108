def check_password(password):
    if len(password) >= 8:
        return "Strong Password"
    elif len(password) >= 5:
        return "Medium Password"
    else:
        return "Weak Password"


password = input("Enter a password: ")

result = check_password(password)
print(result)

if "!" in password:
    print("Special character detected!")
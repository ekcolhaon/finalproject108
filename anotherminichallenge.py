def show_cart(cart):
    print("your cart")

    if not cart:
        print("Your cart is empty.")
    else:
        for item in cart:
            print(item)


cart = ["Apples", "Bread", "Milk"]
show_cart(cart)
from catalog import display_catalog, find_product


def display_cart(cart):
    print("\nYOUR CART")
    if not cart:
        print("Your cart is empty.")
        return 0
    total_cents = 0
    for item in cart:
        subtotal = item["price_cents"] * item["quantity"]
        total_cents += subtotal
        print(f"{item['id']}. {item['name']} | Quantity: {item['quantity']} "
              f"| Each: ${item['price_cents'] / 100:.2f} | Subtotal: ${subtotal / 100:.2f}")
    print(f"Total: ${total_cents / 100:.2f}")
    return total_cents


def read_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
        except ValueError:
            pass
        print("Please enter a positive whole number.")


def add_to_cart(cart, product_id, quantity):
    if quantity <= 0:
        return False
    product = find_product(product_id)
    if product is None:
        return False
    for item in cart:
        if item["id"] == product_id:
            item["quantity"] += quantity
            return True
    item = product.copy()  # Keep cart quantities separate from catalog data.
    item["quantity"] = quantity
    cart.append(item)
    return True


def remove_from_cart(cart, product_id):
    for index, item in enumerate(cart):
        if item["id"] == product_id:
            cart.pop(index)
            return True
    return False


def main():
    cart = []
    print("Welcome to Noah's Python Store!")
    while True:
        print("\n1. View catalog\n2. Add product\n3. View cart")
        print("4. Remove product\n5. Checkout\n6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_catalog()
        elif choice == "2":
            display_catalog()
            product_id = read_positive_integer("Product ID: ")
            if find_product(product_id) is None:
                print("Product not found.")
                continue
            quantity = read_positive_integer("Quantity: ")
            if add_to_cart(cart, product_id, quantity):
                print("Added to your cart!")
        elif choice == "3":
            display_cart(cart)
        elif choice == "4":
            display_cart(cart)
            if cart:
                product_id = read_positive_integer("Product ID to remove (all units): ")
                if remove_from_cart(cart, product_id):
                    print("Product removed.")
                else:
                    print("That product is not in your cart.")
        elif choice == "5":
            if not cart:
                display_cart(cart)
                continue
            display_cart(cart)
            confirm = input("Complete this practice checkout? (yes/no): ").strip().lower()
            if confirm == "yes":
                cart.clear()
                print("Practice order complete. Thank you! No payment was processed.")
            else:
                print("Checkout canceled. Your items are still in the cart.")
        elif choice == "6":
            print("Thanks for visiting!")
            break
        else:
            print("Please choose an option from 1 to 6.")

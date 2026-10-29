def main():
    counter = 1
    while counter <= 5:
        print("Counter:", counter)
        counter += 1  # Update the condition to avoid an infinite loop.

    print("Enter positive numbers to total them. Enter 'done' to finish.")
    total = 0.0
    while True:
        entry = input("Number or done: ").strip()
        if entry.lower() == "done":
            break
        try:
            number = float(entry)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if not 0 < number < float("inf"):
            print("Enter a finite number greater than zero.")
            continue
        total += number
        print(f"Running total: {total:g}")
    print(f"Final total: {total:g}")


if __name__ == "__main__":
    main()

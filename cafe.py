MENU = {
    "Cappuccino": 150,
    "Muffin": 120,
    "Latte": 180,
    "Espresso": 100,
}


def main():
    orders = []

    print("======= STARBUZZ CAFE =======")
    print("Menu:")
    for item, price in MENU.items():
        print(f"  {    item:<12} Rs. {price}")
    print("\nEnter an item name to add it to the bill. Press Enter when done.")

    while True:
        item_name = input("Item: ").strip()
        if not item_name:
            break

        item = next(
            (name for name in MENU if name.casefold() == item_name.casefold()),
            None,
        )
        if item is None:
            print("Sorry, that item is not on the menu.")
            continue

        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a whole-number quantity.")
            continue

        orders.append((item, quantity, MENU[item] * quantity))

    if not orders:
        print("No items ordered.")
        return

    print("\n======= STARBUZZ CAFE BILL =======")
    for item, quantity, line_total in orders:
        description = f"{item} x {quantity}"
        print(f"Item: {description:<18} = Rs. {line_total}")

    total = sum(line_total for _, _, line_total in orders)
    print("----------------------------------")
    print(f"Total Bill: Rs. {total} (Inclusive of taxes)")
    print("Thank you for visiting! 😊")


if __name__ == "__main__":
    main()
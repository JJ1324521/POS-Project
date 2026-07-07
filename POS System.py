# Point of Sale (POS) System
# This program runs on the command line (CMD)
# It stores items in a list, allows adding/removing, and displays totals.

def add_product(products):
    name = input("Enter product name: ").lower()

    if name == "kaas":
        price = 50
    elif name == "melk":
        price = 30
    elif name == "brood":
        price = 15
    else:
        print("Invalid choice, try again.")
        return

    products.append((name.capitalize(), price))
    print(f"{name.capitalize()} added successfully at R{price}")


def remove_product(products):
    name = input("Enter product name: ")
    for product in products:
        if product[0].lower() == name.lower():
            products.remove(product)
            print(f"Product {name.capitalize()} removed.")
            return
    print("Product not found.")
""

def display_products(products):
    if products:  # Check if the list is not empty
        total = 0
        for name, price in products:
            print(f"{name.capitalize()} : R{price:.2f}")
            total += price
        print(f"Total price: R{total}")
    else:
        print("Cart empty")


    # Main function with loop

def main():
    products = []
    while True:
        print("Choose an option:")
        print("1 - Add product")
        print("2 - Remove product")
        print("3 - Show products")
        print("4 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            remove_product(products)
        elif choice == "3":
            display_products(products)
        elif choice == "4":
            print("Program ended.")
            break
        else:
            print("Invalid choice, try again.\n")


    # Run the program

if __name__ == "__main__":
    main()
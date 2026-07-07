# Point of Sale (POS) System
# This program runs on the command line (CMD)
# It stores items in a list, allows adding/removing, and displays totals.

# Function to add a product from the product list into the cart
def add_product(products, cart):
    product_found = False
    name = input("Enter product name: ").lower() # Ask user for product name
    for product in products:
        if product[0].lower() == name.lower():
            cart.append((product[0].capitalize(), product[1])) # Add product to cart
            print(f"{product[0].capitalize()} added successfully at R{product[1]}")
            product_found = True
    if not(product_found): # If no product matched
        print("Invalid choice, try again.")
    return

# Function to remove a product from the cart
def remove_product(cart):
    product_found = False
    name = input("Enter product name: ") # Ask user which product to remove

    for product in cart:  # Loop through items in the cart
        if product[0].lower() == name.lower():
            cart.remove(product) # Remove the first matching product
            print(f"Product {name.capitalize()} removed.")
            product_found = True
            break

    if not(product_found): # If product not found in cart
        print("Product not found in cart.")
    return




# Function to display all items in the cart and calculate total
def display_cart(cart):
    if cart:  # Check if the list is not empty
        total = 0
        for item in cart:
            print(f"{item[0].capitalize()} : R{item[1]:.2f}")
            total += item[1]
        print(f"Total price: R{total}")
    else:
        print("Cart empty") # If no items in cart
    return

# Function to display all available products
def display_products(products):
    for product in products: # Loop through product list
        print(f"{product[0]}: R{product[1]:.2f}")
    return

# Main function with loop
def main():
    # Predefined list of products (name + price)
    products = [
        ["Brood", 15.99],
        ["Melk", 23.50],
        ["Kaas", 9.99]
    ]

    cart = []  # Empty shopping cart

    while True:  # Infinite loop until user chooses to exit
        print("Choose an option:")
        print("1 - Add product")
        print("2 - Remove product")
        print("3 - Show cart")
        print("4 - Display products")
        print("5 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_product(products, cart)  # Add product to cart
        elif choice == "2":
            remove_product(cart) # Remove product from cart
        elif choice == "3":
            display_cart(cart)  # Show cart contents
        elif choice == "4":
            display_products(products)  # Show available products
        elif choice == "5":
            print("Program ended.")  # Exit program
            break
        else:
            print("Invalid choice, try again.\n")  # Handle invalid input


    # Run the program

if __name__ == "__main__":
    main()

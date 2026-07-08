# Point of Sale (POS) System
# This program runs on the command line (CMD)

# Function to add a product from the product list into the cart
def add_product(products, cart):
    product_found = False
    # Ask user for product name
    name = input("Enter product name: ").lower()
    for product in products:
        if product[0].lower() == name.lower():
            # Add product to cart
            cart.append((product[0].capitalize(), product[1]))
            print(f"{product[0].capitalize()} added successfully at R{product[1]}")
            product_found = True
    # If no product matched
    if not(product_found): 
        print("Invalid choice, try again.")
    return

# Function to remove a product from the cart
def remove_product(cart):
    product_found = False
    # Ask user which product to remove
    name = input("Enter product name: ")

    # Loop through items in the cart
    for product in cart: 
        if product[0].lower() == name.lower():
            # Remove the first matching product
            cart.remove(product) 
            print(f"Product {name.capitalize()} removed.")
            product_found = True
            break

    if not(product_found): # If product not found in cart
        print("Product not found in cart.")
    return

# Function to display all items in the cart and calculate total
def display_cart(cart):
    # Check if the list is not empty
    if cart:  
        total = 0
        #Loop through each item in the cart
        for item in cart:
            print(f"{item[0].capitalize()} : R{item[1]:.2f}")
            total += item[1]
        print(f"Total price: R{total}")
    else:
        # If no items in cart
        print("Cart empty") 
    return

# Function to display all available products
def display_products(products):
    # Loop through product list
    for product in products: 
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
    # Empty shopping cart
    cart = [] 

    # Infinite loop until user chooses to exit
    while True: 
        print("Choose an option:")
        print("1 - Add product")
        print("2 - Remove product")
        print("3 - Show cart")
        print("4 - Display products")
        print("5 - Exit")
        choice = input("Your choice: ")

        # Run operations
        if choice == "1":
            add_product(products, cart) 
        elif choice == "2":
            remove_product(cart) 
        elif choice == "3":
            display_cart(cart) 
        elif choice == "4":
            display_products(products)  
        elif choice == "5":
            print("Program ended.")  
            break
        else:
            # Handle invalid input
            print("Invalid choice, try again.\n")  

# Run the program
if __name__ == "__main__":
    main()

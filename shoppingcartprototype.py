# Basic Shopping Cart Prototype
# Coding starts here...
# Starting items in the cart
shopping_cart = ["bed", "chair", "blanket", "pillow"]
prices = {"bed": 150, "chair": 85, "blanket": 45, "pillow": 25}

while True:
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    action = input("Please enter an action: ")

    if action == "1":
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        print(f"'{item}' has been added to the cart.")

    elif action == "2":
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for item in shopping_cart:
                print(item)

    elif action == "3":
        if len(shopping_cart) == 0:
            print("There are no items to remove.")
        else:
            item_to_remove = input("What item would you like to remove? ")
            if item_to_remove in shopping_cart:
                shopping_cart.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the cart.")
            else:
                print(f"'{item_to_remove}' is not in the cart.")

    elif action == "4":
        total = 0
        for item in shopping_cart:
            item_price = prices.get(item, 0)
            total += item_price
        print(f"The total price of the items in the cart is: ${total}")

    elif action == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

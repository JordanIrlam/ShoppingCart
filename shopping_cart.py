'''
Create variables that will store items and their prices

Create a menu that displays the cart and options they have i.e add, remove, view total cost and checkout clearly.

Manipulating the cart, implementing ways to remove and add items to cart.

Calculate costs, go through the prices of all items in cart to calculate the total cost.
'''


items = [
    {"name": "item1", "price": 10.99},
    {"name": "item2", "price": 4.99},   
    {"name": "item3", "price": 2.99},
    {"name": "item4", "price": 7.99},
    {"name": "item5", "price": 11.00} 
    ]


cart = {}

total_price = 0

# Main menu
while True:
    print("Would you like to:")
    print("1: Add an item to your cart")
    print("2: Remove an item from your cart")
    print("3: View total cost of items in cart")
    print("4: Checkout")
    choice = int(input("Enter the number for your prefered action:  "))

# Add item
    if choice == 1:
        while True:
            print("Which item would you like to add to your cart?")
            for i, item in enumerate(items, start=1):
                print(f"{i}: {item['name']}, {item['price']}")
            print("6: Go back")
            
            choice = input("Enter the number for the item you want: ")
            
            if choice == "6":
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(items):
                selected_item = items[int(choice) - 1]
                
                # Check if the item is already in the cart
                if selected_item['name'] in cart:
                    # If yes, increment the quantity
                    cart[selected_item['name']]['quantity'] += 1
                else:
                    # If no, add the item to the cart with quantity 1
                    cart[selected_item['name']] = {'item': selected_item, 'quantity': 1}
                
                print(f"{selected_item['name']} added to the cart.")
            else:
                print("Error, please retry.\n")
# Remove Item
    if choice == 2:
        while True:
            print("Which item would you like to remove from your cart?")
            for i, cart_item in enumerate(cart.values(), start=1):
                print(f"{i}: {cart_item['item']['name']}, Quantity: {cart_item['quantity']}")
            print("6: Go back")
            
            choice = input("Enter the number for the item you want to remove: ")
            
            if choice == "6":
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(cart):
                selected_cart_item = list(cart.values())[int(choice) - 1]
                
                # Check if the quantity is greater than 1, decrement the quantity
                if selected_cart_item['quantity'] > 1:
                    selected_cart_item['quantity'] -= 1
                    print(f"One {selected_cart_item['item']['name']} removed from the cart.")
                else:
                    # If quantity is 1, remove the item from the cart
                    del cart[selected_cart_item['item']['name']]
                    print(f"{selected_cart_item['item']['name']} removed from the cart.")
            else:
                print("Error, please retry.\n")

# View total cost of cart
    if choice == 3:
        print("\nYour Cart:")
        for item_info in cart.values():
            item = item_info['item']
            quantity = item_info['quantity']
            print(f"{item['name']}, Quantity: {quantity}, Price: {item['price'] * quantity}")

# Checkout
    if choice == 4:
        print("\nYour Cart:")
        for item_info in cart.values():
            quantity = item_info['quantity']
            item = item_info['item']
            item_price = item['price'] * quantity
            total_price += item_price
            print(f"{item['name']}, Quantity: {quantity}, Price: {item['price'] * quantity}")
        print(f"\nTotal Cost: £{round(total_price, 2)}")
       
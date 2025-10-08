# cafe_management.py

# Sample menu (dictionary format: item -> [price, stock])
menu = {
    "Coffee": [30.0, 10],
    "Tea": [25.0, 10],
    "Sandwich": [50.0, 5],
    "Cake": [40.0, 6]
}

admin_username = "admin"
admin_password = "1234"

def display_menu():
    print("\n--- MENU ---")
    for item, (price, stock) in menu.items():
        print(f"{item}: Rs.{price:.2f} (In stock: {stock})")

def take_order():
    order = {}
    total = 0
    while True:
        display_menu()
        choice = input("\nEnter item to order (or 'done' to finish): ").title()
        if choice.lower() == 'done':
            break
        if choice in menu:
            quantity = input(f"Enter quantity of {choice}: ")
            if not quantity.isdigit():
                print("Please enter a valid number.")
                continue
            quantity = int(quantity)
            if quantity > menu[choice][1]:
                print(f"Sorry, only {menu[choice][1]} {choice}(s) left.")
                continue
            order[choice] = order.get(choice, 0) + quantity
            menu[choice][1] -= quantity
            total += menu[choice][0] * quantity
        else:
            print("Item not found in menu.")
    return order, total

def print_bill(order, total):
    print("\n--- BILL ---")
    for item, qty in order.items():
        price = menu[item][0]
        print(f"{item} x {qty} = Rs.{price * qty:.2f}")
    print(f"Total: Rs.{total:.2f}")
    print("Thank you for your order!")

def admin_panel():
    print("\n--- ADMIN PANEL ---")
    while True:
        print("\n1. View Menu\n2. Update Price\n3. Restock Item\n4. Add New Item\n5. Back")
        choice = input("Choose an option: ")
        if choice == '1':
            display_menu()
        elif choice == '2':
            item = input("Enter item to update price: ").title()
            if item in menu:
                new_price = input("Enter new price (in Rs.): ")
                try:
                    menu[item][0] = float(new_price)
                    print(f"Updated price of {item}.")
                except:
                    print("Invalid price.")
            else:
                print("Item not found.")
        elif choice == '3':
            item = input("Enter item to restock: ").title()
            if item in menu:
                qty = input("Enter quantity to add: ")
                if qty.isdigit():
                    menu[item][1] += int(qty)
                    print(f"Restocked {item}.")
                else:
                    print("Invalid quantity.")
            else:
                print("Item not found.")
        elif choice == '4':
            item = input("Enter new item name: ").title()
            if item in menu:
                print("Item already exists.")
                continue
            price = input("Enter price (in Rs.): ")
            stock = input("Enter initial stock: ")
            try:
                menu[item] = [float(price), int(stock)]
                print(f"Added {item} to menu.")
            except:
                print("Invalid input.")
        elif choice == '5':
            break
        else:
            print("Invalid option.")

def login_admin():
    username = input("Admin username: ")
    password = input("Admin password: ")
    if username == admin_username and password == admin_password:
        admin_panel()
    else:
        print("Incorrect credentials.")

def main():
    while True:
        print("\n--- Café Management ---")
        print("1. Customer\n2. Admin\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            order, total = take_order()
            if order:
                print_bill(order, total)
            else:
                print("No order placed.")
        elif choice == '2':
            login_admin()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

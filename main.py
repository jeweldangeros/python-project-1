# Inventory Management System

items = []


# Function 1: Add items
def add_items():
    name = input("Enter product name: ")
    amount = int(input("Enter product price: "))
    category = input("Enter category: ")
    quantity = int(input("Enter initial stock quantity: "))

    item = {"Name": name, "Amount": amount, "Category": category, "Quantity": quantity}

    items.append(item)
    print("Item added successfully!")


# Function 2: View all items
def view_items():
    if not items:
        print("No items found in inventory.")
    else:
        print("\n===== INVENTORY =====")

        for item in items:
            print(f"Name: {item['Name']}")
            print(f"Price: {item['Amount']}")
            print(f"Category: {item['Category']}")
            print(f"Quantity: {item['Quantity']}")

            if item["Quantity"] > 0:
                print("Stock: Available")
            else:
                print("Stock: Out of Stock")

            print("------------------------")


# Function 3: Check product availability
def check_availability():
    name = input("Enter product name to search: ")

    for item in items:
        if name.lower() == item["Name"].lower():
            if item["Quantity"] > 0:
                print(f"{name} is available")
                print(f"Quantity: {item['Quantity']}")
            else:
                print(f"{name} is out of stock")
            return

    print("Product not found in inventory.")


# Function 4: Update stock


def update_stock():
    product_name = input("Enter product name: ")

    for item in items:
        if product_name.lower() == item["Name"].lower():
            print(f"Product found: {item['Name']}")
            print(f"Current stock: {item['Quantity']}")

            print("\n1. Add Stock")
            print("2. Remove Stock")

            answer = input("Select an option: ")

            if answer != "1" and answer != "2":
                print("Invalid option.")
                return

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter a whole number.")
                return

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

            if answer == "1":
                item["Quantity"] += quantity

            elif answer == "2":
                if quantity > item["Quantity"]:
                    print("Insufficient stock!")
                    return

                item["Quantity"] -= quantity

            print("Stock updated successfully!")
            print(f"New Stock: {item['Quantity']}")
            return

    print("Product not found in inventory.")


# Function 5: Interactive Menu
def select_menu():
    while True:
        print("\n===== INVENTORY MENU =====")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Check Availability")
        print("4. Update Stock")
        print("5. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            add_items()
        elif choice == "2":
            view_items()
        elif choice == "3":
            check_availability()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")


# Main Program
select_menu()

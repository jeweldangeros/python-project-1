# Inventory Management System

items = []


# Function 1: Add items
def add_items():
    name = input("Enter product name: ")
    amount = int(input("Enter product amount: "))
    category = input("Enter category: ")
    is_on_stock = input("Stock available? y/n: ").lower()

    item = {"Name": name, "Amount": amount, "Category": category, "Stock": is_on_stock}

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
            print(f"Amount: {item['Amount']}")
            print(f"Category: {item['Category']}")

            if item["Stock"] == "y":
                print("Stock: Available")
            else:
                print("Stock: Out of Stock")

            print("------------------------")


# Function 3: Check product availability

# Function 3: Check product availability


def check_availability():
    name = input("Please enter the name of the product: ")

    for item in items:
        if name.lower() == item["Name"].lower():
            if item["Stock"] == "y":
                print(f"{name} is available")
            else:
                print(f"{name} is not available")

            return

    print("Product not found in inventory.")


# Main program
add_items()
add_items()
view_items()
check_availability()

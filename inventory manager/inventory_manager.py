inventory = {
    "GPU": {
        "price": 600,
        "quantity": 5,
        "category": "PC"
    },
    "CPU": {
        "price": 300,
        "quantity": 10,
        "category": "PC"
    }
}
def add_product():
    product = input("Product name: ")
    inventory[product] = {}
    price = int(input("Product price: "))
    inventory[product]["price"] = price
    quantity = int(input("Product quantity: "))
    inventory[product]["quantity"] = quantity
    category = input("Product category: ")
    inventory[product]["category"] = category

def remove_product():
    product = input("Enter a product to remove: ")
    if product in inventory:
        inventory.pop(product)
        print("Product removed!")
    else:
        print("Product not found!")

def update_quantity():
    product = input("Enter a product to update quantity: ")
    quantity = int(input("Enter new quantity: "))
    inventory[product]["quantity"] = quantity

def show_inventory():
    for product, info in inventory.items():
        print(f"{product} -> Price: {info['price']}, Quantity: {info['quantity']}, Category: {info['category']}")

def search_product():
    search = input("Product name: ")
            
    if search in inventory:
        print(f"{search} -> Price: {inventory[search]['price']}, Quantity: {inventory[search]['quantity']}, Category: {inventory[search]['category']}")
    else:
         print("Product not fould!")

def show_categories():
    categories = set()
    for product, info in inventory.items():
        categories.add(info["category"])
    print(categories)

while True:
    print()
    print("1.Add Product")
    print("2.Remove Product")
    print("3.Update Quantity")
    print("4.Show Inventory")
    print("5.Search Product")
    print("6.Show Unique Categories")
    print("7.Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        add_product()
    elif choice == 2:
        remove_product()
    elif choice == 3:
        update_quantity()
    elif choice == 4:
        show_inventory()
    elif choice == 5:
        search_product()
    elif choice == 6:
        show_categories()
    elif choice == 7:
        break


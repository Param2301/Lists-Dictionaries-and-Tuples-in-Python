inventory = {}

inventory["apple"] = (10, 2.5)
inventory["banana"] = (20, 1.2)

def add_item(name, quantity, price):
   inventory[name] = (quantity, price)
   print(f"Added {name} to inventory.")


def remove_item(name):
   if name in inventory:
       del inventory[name]
       print(f"Removed {name} from inventory.")
   else:
       print(f"Sorry, {name} is not in the inventory.")

def update_quantity(name, new_quantity):
   if name in inventory:
       old_quantity, price = inventory[name]
       inventory[name] = (new_quantity, price)
       print(f"Updated {name} quantity from {old_quantity} to {new_quantity}.")
   else:
       print(f"Sorry, {name} is not in the inventory.")

def update_price(name, new_price):
   if name in inventory:
       quantity, old_price = inventory[name]
       inventory[name] = (quantity, new_price)
       print(f"Updated {name} price from ${old_price} to ${new_price}.")
   else:
       print(f"Sorry, {name} is not in the inventory.")

def display_inventory():
   print("\nCurrent inventory:")
   for item, details in inventory.items():
       quantity, price = details
       print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

def calculate_total_value():
   total_value = 0
   for item, details in inventory.items():
       quantity, price = details
       item_value = quantity * price
       total_value = total_value + item_value
   return total_value

print("Welcome to the Inventory Manager!")

display_inventory()

add_item("mango", 15, 3.0)

print("\nUpdated inventory:")
display_inventory()

update_quantity("apple", 15)

update_price("banana", 1.5)

remove_item("apple")

display_inventory()

total = calculate_total_value()
print(f"\nTotal value of inventory: ${total}")

print("\nNow you can try managing the inventory!")
print("Available commands: add, remove, update_quantity, update_price, display, total, exit")

while True:
   command = input("\nWhat would you like to do? ").lower()
   
   if command == "add":
       name = input("Enter item name: ")
       quantity = int(input("Enter quantity: "))
       price = float(input("Enter price: $"))
       add_item(name, quantity, price)
   
   elif command == "remove":
       name = input("Enter item name to remove: ")
       remove_item(name)
   
   elif command == "update_quantity":
       name = input("Enter item name: ")
       quantity = int(input("Enter new quantity: "))
       update_quantity(name, quantity)
   
   elif command == "update_price":
       name = input("Enter item name: ")
       price = float(input("Enter new price: $"))
       update_price(name, price)
   
   elif command == "display":
       display_inventory()
   
   elif command == "total":
       total = calculate_total_value()
       print(f"Total value of inventory: ${total}")
   
   elif command == "exit":
       print("Thank you for using the Inventory Manager!")
       break
   
   else:
       print("Sorry, I didn't understand that command.")
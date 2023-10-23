menu_item = {"Cheeseburger":2.99, "Sm Fry": 0.99, "Med Fry": 1.99, "Lg Fry":2.99, "Milk Shake": 4.99, "Double Cheeseburger": 4.99}

customer_1_item = menu_item.get("Cheeseburger")
print(f"Customer 1 ordered a Cheeseburger for {customer_1_item}")

print(f"Items of a Dictionary: {menu_item.items()}")
print(f"Keys of a Dictionary: {menu_item.keys()}")
print(f"Values of Dictionary: {menu_item.values()}")

menu_item["Milk Shake"] = 8.99
print(f"Items of a Dictionary: {menu_item.items()}")

for key in menu_item:
    print(key)

for key, value in menu_item.items():
    print(key, value)
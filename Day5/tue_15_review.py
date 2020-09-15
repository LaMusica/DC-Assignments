
stores = []


class GroceryITem:



def display_menu():







diplay_menu()
choice = input("Enter choice: ")

while True: 
    if choice == "1":
        name = input("Enter name for grocery store: ")
        address = input("Enter Add for grocery store:")
        store = GroceryStore(name, address)
        # add store to stores
        stores.append(store)
    elif choice == "2":
       for index in range(0, len(stores)):
           store = stores[index]
           print(f"{index + 1} - {store.name}")
       
       # grocery_store_index = input("Enter index of grocery store to add items: ")
        store_index = input("Enter grocery store number: ")
        store = stores[store_index -1]
        item_name = input("Enter grocery item name: ")
        item_price = float(input("Enter grocery item price: "))
        grocery_item = GroceryItem(item_name, item_price)

        
    
    
    
    
    elif choice == "q":
        break

print(stores)
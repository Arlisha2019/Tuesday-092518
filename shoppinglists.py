class GroceryStore:
    def __init__(self,store_name, store_address):
        self.store_name = store_name
        self.store_address = store_address
        self.items = []

class GroceryItem:
    def __init__(self,name):
        self.name = name


grocery_stores = []

while True:

    store_name = input("Please enter one of the desired grocery stores or q to quit: ")


    if(store_name == "q"):
        print("************************************************************")
        print("Thank You for using this Application! Hope to see you again!")
        print("************************************************************")
        break

    store_address = input("Enter {0} physical address: ".format(store_name))

    store = GroceryStore(store_name, store_address)

    grocery_stores.append(store)


    while True:

        name = input("Please enter your desired grocery item at {0} or N to quit: ".format(store_name))

        if(name == 'N'):
            print("Your shopping list is as follows:")
            for store in grocery_stores:
                print(store.store_name)
                print(store.store_address)
                for item in store.items:
                    print(item.name)
            print("Thank You for using our application!")
            break

        grocery_item = GroceryItem(name)

        store.items.append(grocery_item)

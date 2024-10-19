#Task 3: Add a function that prints 
# out the entire list in a formatted way.



def add_item(shopping_list, item):
    shopping_list.append(item)

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found in the list.")
def display_items(shopping_list):
    print("Your shopping list:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")




shopping_list = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Display items")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        add_item(shopping_list, item)
    elif choice == 2:
        item = input("Enter item to remove: ")
        remove_item(shopping_list, item)
    elif choice == 3:
        display_items(shopping_list)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
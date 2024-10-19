def add_item(shopping_list, item):
    shopping_list.append(item)

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found in the list.")




shopping_list = []


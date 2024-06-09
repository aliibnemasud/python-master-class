shopping_list = ["milk", "bread", "eggs", "spam", "bread", "rice"]

item_to_found = "bread"
found_index = None

# for index in range (len(shopping_list)):
#     if shopping_list[index] == item_to_found:
#         found_index = index
#         break

# Same function for the avobe
if item_to_found in shopping_list:
     found_index = shopping_list.index(item_to_found)


if found_index is not None:
    print("Item found at position {}".format(found_index))
else:
    print("{} not found".format(item_to_found))
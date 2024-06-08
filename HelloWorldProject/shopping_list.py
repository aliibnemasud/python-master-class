shopping_list = ["milk", "bread", "eggs", "spam", "bread", "rice",]

# for item in shopping_list:
#     if item != "milk":
#         print("Buy", item)

# for item in shopping_list:
#     if item == "milk":
#         continue
#     print("Buy", item)

for item in shopping_list:
    if item == "eggs":
        break
    print("Buy", item)

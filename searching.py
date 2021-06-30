shopping_list = ["milk", "eggs", "pasta", "bread", "rice", "spam"]

# using the break keyword will exit the loop
item_to_find = "rice"
found_at = None

# to iterate over an array using the index use: range(len(array))
# for i in range(len(shopping_list)):
#     if shopping_list[i] == item_to_find:
#         found_at = i
#         break

# because python is a rich language, the above can also be written as
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("{} is at index {} of the shopping list".format(item_to_find, found_at))
else:
    print("{} not found".format(item_to_find))
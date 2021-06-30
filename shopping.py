# A list in Python is an ordered squence of values, enclosed in square brackets
# similar to an array

shopping_list = ["milk", "eggs", "pasta", "bread", "rice", "spam"]

# for item in shopping_list:
#     # to check if item isn't rice
#     if item != "rice":
#         print("Buy " + item)

# using the continue keyword - continue skips the rest of the iteration of the loop
for item in shopping_list:
    if item == "rice":
        continue
    print("Buy " + item)


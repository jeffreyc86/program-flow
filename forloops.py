# parrot = "Norwegian blue"
#
# for char in parrot:
#     print(char)

# number = "9,223;372;036 854,775;807"
number = input("Enter a series of numbers entering any separator you'd like: ")
separators = ""

# isnumeric() is a string method to check if the string is a number
for char in number:
    if not char.isnumeric():
        separators += char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
arrOfNums = [int(val) for val in values]
sum = sum(arrOfNums)
print(sum)
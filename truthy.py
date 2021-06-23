if 0:
    print("True")
else:
    print("False")

# empty strings are falsey
name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")

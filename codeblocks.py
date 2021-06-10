name = input("Please enter your name: ")
# int function turns the input into an integer, it will error out if it is not convertible
age = int(input("How old are you {}? ".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("You're still too young to vote. Please come back in {0} years".format(18-age))

# if, elif, else

if age < 18:
    print("You're still too young to vote. Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")

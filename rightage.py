name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age <= 30:
    print("Welcome to the holiday, {}!".format(name))
else:
    if age < 18:
        print("Sorry, {}. You're too young. Come back in {} years.".format(name, 18-age))
    else:
        print("Sorry, {0}. You're {1} years too old.".format(name, age-30))
# use the not in operator to check if a value is NOT within a string/array/etc

# letter = input("Please enter a character: ")
#
# parrot = "Norwegian blue"
#
# if letter not in parrot:
#     print("{} is not within {}".format(letter, parrot))
# else:
#     print("I need {0} to complete the string {1}".format(letter, parrot))

activity = input("What would you like to do today? ")

# if "cinema" not in activity:
#     print("But I want to go to the cinema")

# if activity = "Cinema, this would still print "But I want to go to the cinema"
# because of case sensitivity
# to resolve this use the .casefold() function which turns everything to lowercase

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
else:
    print("Hooray, I'd love to see a movie!")
# use the in operator to check if a character/string is within a string

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("{0} is NOT in {1}".format(letter, parrot))

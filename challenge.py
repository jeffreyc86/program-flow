options = ["1.\tGo outside", "2.\tSmoke weed", "3.\tWatch a movie", "4.\tEat lunch", "5.\tAll of the above", "0. Exit"]

selection = "-"
while True:
    if selection == "0":
        print("You've quit the game")
        break
    elif selection in "12345":
        print("You chose {}".format(selection))
    else:
        print("Please select an option from 1-5. Press 0 to quit: ")
        for i in range(len(options)):
            print(options[i])

    selection = input()


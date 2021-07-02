low = 1
high = 1000

print("Please think of number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:
    # using // for integer division - always rounds down
    guess = low + ((high - low) // 2)
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     " Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        # python requires code in a code block
        # can use pass key word as a place holder
        # pass
        print("Please guess higher")
        low = guess+1
    elif high_low == "l":
        # Guess lower. The higher end of the range becomes 1 less than the guess
        print("Please guess lower")
        high = guess-1
    elif high_low == "c":
        singOrPlur = "guesses"
        if guesses == 1:
            singOrPlur = "guess"
        print("I got it in {} {}!".format(guesses, singOrPlur))
        break
    else:
        print("Please enter h, l, or c")

    guesses += 1

# single = is for assiging variables
# double == is for testing for equality

answer = 5

print("Please guess a number between 1 and 10")
guess = int(input())

# if guess < answer:
#     print("Please guess higher")
# elif guess > answer:
#     print("Please guess lower")
# else:
#     print("You guessed correctly")

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guess correctly")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guess correctly")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You guessed correctly")
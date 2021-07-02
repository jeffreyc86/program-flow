import random
# python has a library of built in modules
# to use them it is customary to import them at the top of your file

# the randint function is built into the random module
highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
# intelliJ has a built in TODO feature

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it correctly the first time!")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed correctly")
#     else:
#         print("Sorry, you have not guessed correctly")
while guess != answer:
    if guess < answer and guess != 0:
        print("Please guess higher")
    elif guess == 0:
        print("You've quit the game")
        break
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("You've guessed it correctly!")

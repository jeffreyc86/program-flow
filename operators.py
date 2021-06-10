# less than <
# less than or equal to <=
# greater than >
# greater than or equal to >=
# equal to ==
# not equal to !=

answer = 5
print("Please guess a number between 1 and 10")
guess = int(input())


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you've guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You've guessed it correctly the first time")

if guess == answer:
    print("You've guessed it correctly the first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you've guessed it")
    else:
        print("Sorry, you have not guessed correctly")

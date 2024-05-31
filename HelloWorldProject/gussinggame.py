answer = 5
guess = int(input("Please guess number between 1 to 10: "))

# if guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# if guess != answer:
#     if guess > answer:
#         print("Please guess lower")
#     elif guess < answer:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it.")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

if guess == answer:
    print("You got it first time")
else:
    if guess > answer:
        print("Please guess lower")
    elif guess < answer:
        print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it.")
    else:
        print("Sorry, you have not guessed correctly")

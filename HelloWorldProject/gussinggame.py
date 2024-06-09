import random
# answer = 5
highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0
print("Please guess number between 1 to 10: ")

# **** Improved Code ****

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

# **** Improved Code ****

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

# **** Improved Code ****
# if guess == answer:
#     print("You got it first time")
# else:
#     if guess > answer:
#         print("Please guess lower")
#     elif guess < answer:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it.")
#     else:
#         print("Sorry, you have not guessed correctly")

# **** Improved Code ****

while guess != answer:
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it.")
        break
    else:
        if guess > answer:
            print("Please guess lower")
        elif guess < answer:
            print("Please guess higher")

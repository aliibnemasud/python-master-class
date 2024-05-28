answer = 5
guess = int(input("Please guess number between 1 to 10: "))

if guess > answer:
    print("Please guess lower")
elif guess < answer:
    print("Please guess higher")
else:
    print("You got it.")
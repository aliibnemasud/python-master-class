# for i in range(1, 15):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#     print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif 100 < age:
    print("You are old enough. Take rest.")
else:
    print("{0} you are {1} years old".format(name, age))
    print("You are old enough to vote")





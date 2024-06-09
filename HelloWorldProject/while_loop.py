# for i in range (10):
#     print("i is now {}".format(i))

# When the condition is not false the loop is continue running.
# i=0
# while i < 10:
#     print("i is now {}".format(i))
#     i +=1

# adventure example of while loop
# available_exits = ["north", "south", "east", "west"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
# print("Aren't you glad you to out there.")


# available_exits = ["north", "south", "east", "west"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game Over")
#         break
# print("Aren't you glad you to out there.")

# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
# for i in range(0, 100, 7):
#     if i > 0:
#         if not i%11:
#             print(i)
#             break

# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break

"""Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5.
Zero is considered divisible by everything (zero should not appear in the output).
The aim is to use the continue statement, but it's also possible to do this without continue.
"""
# solve with
for i in range(20):
    if i%3 != 0 and i%5 != 0:
        print(i)







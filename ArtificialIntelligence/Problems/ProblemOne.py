# converts percentage to decimal.
# percentage_number = int(input("Enter Percentage Number: "))
# print("Decimal Number is: ", percentage_number/100)

# The formula to convert Celsius to Fahrenheit is given by: °F = °C × (9/5) + 32.
# celsius = int(input("Enter Celsius temperature: "))
# print("Celsius to Fahrenheit is: ", 1.8*celsius+32)

# inches to feet
# inches = int(input("Enter Inches to convert Feet: "))
# print("{} inches is {} feet and {} inches".format(inches, inches//12, inches%12))

# 4. A copy centre charges 50 won per copy for the first 100 copies and 30 won
# per copy for each additional copy.
# Write a program that requests the number as input and displays the total cost.

paper_to_print = int(input("Enter number of Paper need to print: "))
if paper_to_print <= 100:
    print("Total Cost {} won".format(paper_to_print * 50))
else:
    additional = paper_to_print - 100
    print("Total Cost {} won".format(50 * 100 + additional * 30))
def hello_world  ():
    print("Hello World")
    return  1
hello = hello_world()
print(hello)



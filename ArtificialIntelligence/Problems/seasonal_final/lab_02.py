# Problem 01
numbers = []
for i in range(5):
    num = int(input(f"Enter Number {i + 1} : "))
    numbers.append(num)

cumulative_number = 0
for num in numbers:
    cumulative_number = cumulative_number + num
    print(cumulative_number)

# Problem 02

# Read the number from the user and convert it to an integer
number = int(input("Enter a number: "))

# Extract and print digits from right to left
while number > 0:
    digit = number % 10  # Get the rightmost digit
    print(digit, end=", " if number // 10 > 0 else "\n")  # Print digit with comma or newline
    number //= 10  # Remove the rightmost digit


# Problem 03

# Read the size of the square from the user
N = int(input("Enter the size of the square: "))

# Use nested loops to print the square
for i in range(N):  # Outer loop for rows
    for j in range(N):  # Inner loop for columns
        print("+", end="")  # Print '+' without moving to a new line
    print()  # Move to the next line after each row


# Problem 04

# Read the string from the user
input_string = input("Enter a string: ")

# Check if the string contains only 0s and 1s
if all(char in '01' for char in input_string):  # Validate each character
    print("Binary Number")
else:
    print("Not a Binary Number")

# Problem 05

# Read the input word from the user
word = input("Enter a word: ")

# Check conditions and modify the word accordingly
if word.endswith("est"):
    # If the word ends with "est", print it as is
    print(word)
elif word.endswith("er"):
    # If the word ends with "er", add "est"
    print(word + "est")
elif len(word) == 2:
    # If the length of the word is 2, print it as is
    print(word)
elif len(word) == 3:
    # If the length of the word is 3, add "er"
    print(word + "er")
else:
    # For other cases, add "er"
    print(word + "er")


# Problem 06

# Read the input string from the user
word = input("Enter a word: ")

# Generate and print subsequent substrings
for i in range(1, len(word) + 1):  # Loop through 1 to length of word (inclusive)
    print(word[:i])  # Print the substring from the start to the ith position

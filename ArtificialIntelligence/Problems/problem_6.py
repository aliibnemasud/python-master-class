def sum_of_smallest_and_largest(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest + largest

# Example list of 6 numbers
numbers = [12, 45, 7, 32, 18, 22]

# Calculate the sum of the smallest and largest numbers
result = sum_of_smallest_and_largest(numbers)

# Print the result
print(f"The sum of the smallest and largest numbers in the list is {result}.")

# Input from user to find the smallest number
def sum_of_smallest_and_largest(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest + largest

# Ask the user to enter 6 numbers
numbers = []
for i in range(6):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the sum of the smallest and largest numbers
result = sum_of_smallest_and_largest(numbers)

# Print the result
print(f"The sum of the smallest and largest numbers in the list is {result}.")


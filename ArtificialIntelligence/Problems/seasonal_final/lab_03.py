# Problem 01

import numpy as np

# Task 1: Create a 3x3 array with values ranging from 1 to 9
array_3x3 = np.arange(1, 10).reshape(3, 3)
print("3x3 Array:")
print(array_3x3)

# Task 2: Reverse the array arr = np.array([1, 2, 3, 4, 5])
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print("\nReversed Array:")
print(reversed_arr)

# Task 3: Convert arr = np.array([5, 6, 7, 8, 9]) to a 2x3 array
arr = np.array([5, 6, 7, 8, 9])
reshaped_arr = arr.reshape(2, 3)
print("\nReshaped 2x3 Array:")
print(reshaped_arr)

# Problem 02

import numpy as np

# Define the recursive factorial function
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    return n * factorial(n - 1)  # Recursive call

# Take 5 input numbers from the user
input_numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(5)]

# Store the numbers in a NumPy array
numbers_array = np.array(input_numbers)

# Calculate factorials using the recursive function
factorials = np.array([factorial(num) for num in numbers_array])

# Print the factorial values sequentially
print("\nFactorials:")
for num, fact in zip(numbers_array, factorials):
    print(f"Factorial of {num} is {fact}")


# Problem 03

import numpy as np

# Step 1: Create a vector of size 10 with zeros
zeros_vector = np.zeros(10)

# Step 2: Create a vector of size 10 with ones
ones_vector = np.ones(10)

# Step 3: Change the dimension of the vectors to 10x1
zeros_reshaped = zeros_vector.reshape(10, 1)
ones_reshaped = ones_vector.reshape(10, 1)

# Step 4: Merge the two vectors vertically
vertical_merge = np.concatenate((zeros_reshaped, ones_reshaped), axis=0)

# Step 5: Merge the two vectors horizontally
horizontal_merge = np.concatenate((zeros_reshaped, ones_reshaped), axis=1)

# Print the results
print("Vector of zeros:")
print(zeros_reshaped)

print("\nVector of ones:")
print(ones_reshaped)

print("\nVertical merge:")
print(vertical_merge)

print("\nHorizontal merge:")
print(horizontal_merge)

# Problem 4

import numpy as np

# File content (for example, assume it's saved in a file named "data.csv")
file_name = "data.csv"

# Read the file using numpy.genfromtxt
data = np.genfromtxt(file_name, delimiter=",", dtype=float, missing_values="", filling_values=np.nan)

# Print the data
print("File Content as Array:")
print(data)

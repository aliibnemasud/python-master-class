def calculate_differences(numbers):
    average = sum(numbers) / len(numbers)
    smallest = min(numbers)
    largest = max(numbers)
    difference_smallest = average - smallest
    difference_largest = average - largest
    return difference_smallest, difference_largest

# Example list of 10 numbers
numbers = [15, 42, 8, 23, 67, 34, 18, 5, 89, 12]

# Calculate the differences
difference_smallest, difference_largest = calculate_differences(numbers)

# Print the results
print(f"The difference between the average and the smallest number is {difference_smallest:.2f}")
print(f"The difference between the average and the largest number is {difference_largest:.2f}")

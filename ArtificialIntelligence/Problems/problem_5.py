# 5. Print average of all numbers divisible by 3 and less than 100.
def average_of_numbers_divisible_by_3():
    numbers = [num for num in range(1, 100) if num % 3 == 0]
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

# Calculate the average
average = average_of_numbers_divisible_by_3()

# Print the average
print(f"The average of all numbers divisible by 3 and less than 100 is {average:.2f}")
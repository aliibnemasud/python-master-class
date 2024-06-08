# numbers = "1,445;511:235 556,256;256"
numbers = input("Please enter series of number: ")
separators = ""

for char in numbers:
    if not char.isnumeric():
        separators = separators + char

print(separators)

# values = "".join(char if char not in separators else " " for char in numbers).split()
# print([int(val) for val in values])


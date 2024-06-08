age = int(input("How old are you? "))

if age >= 16 and age <= 65:
    print("Go Swimming.")
else:
    print("Gelo.")

# using range
age = int(input("How old are you? using range "))

if age in range(16, 66):
    print("Go Swimming.")
else:
    print("Gelo.")
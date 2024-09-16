# 9. A sailor has a boat known as Téssares Boat, which has four corners. The boat
# is capable of carrying goods of any weight as long as there is equal distribution
# of loads on each corner of the boat - the centre area has been occupied by the
# engine. The sailor needs your help to know the maximum amount of weight he
# can carry in each shipment.
# Write a Python program that reads the total weight of the shipment and prints
# the maximum load (or weight) the boat can take from the given shipment. We
# can assume that the weight of each good is exactly 1 unit, therefore, the weight
# of 5 units means there are 5 (loose) items in the shipment.

def calculate_max_load_per_corner(total_weight):
    # The boat has four corners
    corners = 4
    # Calculate the maximum load per corner
    max_load_per_corner = total_weight // corners

    return max_load_per_corner

# Ask the user to enter the total weight of the shipment
total_weight = int(input("Enter the total weight of the shipment: "))

# Calculate the maximum load per corner
max_load_per_corner = calculate_max_load_per_corner(total_weight)

# Print the maximum load per corner
print(f"The maximum load each corner of the boat can take is {max_load_per_corner} units.")

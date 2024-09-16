def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Ask the user to enter the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = calculate_triangle_area(base, height)

# Print the area of the triangle
print(f"The area of the triangle with base {base} and height {height} is {area:.2f}")

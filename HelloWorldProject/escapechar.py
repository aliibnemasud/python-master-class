splitString = "This is a split string\n split over\n several"
print(splitString)
tabString = "1\t2\t3\t4"
print(tabString)
print('The pet shop owner said "No, no, \'e\'s uh, ....he\'s resting".')
# or
print("The pet shop owner said \"No, no 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no 'e's uh,...he's resting".""")

# it will break the line
print("""This is the new line 
several 
is here 
""")
# it will break the rule
print("""This is the new line \
several \
is here \
""")
# Path
# print("C:\Users\tiambuchalka\notes.text") - Problem to declare like this.
# Here are the solution
# Use Double backslash
print("C:\\Users\\tiambuchalka\\notes.text")
# Use Row string using just - r behind the string
print(r"C:\Users\tiambuchalka\notes.text")


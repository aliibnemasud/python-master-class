parrot = "Norwegian Blue"
print(parrot[0:7])  # Norwegi
print(parrot[:7])  # Norwegi

print(parrot[10:])  # Blue

print(parrot[:6])
print(parrot[6:])
print(parrot[6:] + parrot[:6])  # Norwegian Blue
print(parrot[:])  # Norwegian Blue

name = "Ali Ibne Masud"
print(name[0:10:2])   #AiIn
print(name[0:10:3])   # A nM

numbers = "1,445,511,235,556,256,256"
separators = numbers[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in numbers).split()
print([int(val) for val in values])

letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[::-1])  # zyxwvutsrqponmlkjihgfedcba
print(letters[25::-1])  # zyxwvutsrqponmlkjihgfedcba










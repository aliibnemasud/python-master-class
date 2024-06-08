quote = """Alright, but apart from the Sanitation, the Medicine,
Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, 
and Public Health, what have the Romans ever done for us?
"""
capsL = ""
# for capitalLatter in quote:
#     if capitalLatter.isupper():
#         capsL = capsL + capitalLatter

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        capsL = capsL + char

print(capsL)
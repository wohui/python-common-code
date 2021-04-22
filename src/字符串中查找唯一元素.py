my_string = "aavvccccddddeee"

# converting the string to a set
temp_set = set(my_string)
for item in temp_set:
    print(item)
# stitching set into a string using join
new_string = ''.join(temp_set)

print(new_string)
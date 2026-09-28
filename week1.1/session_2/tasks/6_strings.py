# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
# Converts the string to lowercase
print(f"Modified String 1: {user_string.lower()}")

# Converts the string to uppercase
print(f"Modified String 2: {user_string.upper()}")

# Removes spaces from the beginning and end of the string
print(f"Modified String 3: {user_string.strip()}")

# Replaces every 'a' with '@'
print(f"Modified String 4: {user_string.replace('a', '@')}")

# Makes the first character uppercase and the rest lowercase
print(f"Modified String 5: {user_string.capitalize()}")

# Reverses the string
print(f"Modified String 6: {user_string[::-1]}")

# Capitalizes the first letter of each word
print(f"Modified String 7: {user_string.title()}")

# Returns the number of characters in the string
print(f"Modified String 8: {len(user_string)}")

# Finds the position of the first 'a'
print(f"Modified String 9: {user_string.find('a')}")

# Counts how many times 'a' appears
print(f"Modified String 10: {user_string.count('a')}")

# Checks if the string starts with 'Hello'
print(f"Modified String 11: {user_string.startswith('Hello')}")

# Checks if the string ends with ':'
print(f"Modified String 12: {user_string.endswith('!')}")

# Checks if the string contains only letters and numbers
print(f"Modified String 13: {user_string.isalnum()}")

# Checks if the string contains only letters
print(f"Modified String 14: {user_string.isalpha()}")

# Checks if the string contains only numbers
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!

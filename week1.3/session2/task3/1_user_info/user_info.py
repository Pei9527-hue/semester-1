# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
# Ask the user for their information
name = input("What is your name? ")
age = input("How old are you? ")
colour = input("What is your favourite colour? ")
# Open a file called 'user_info.txt' for reading
with open("user_info.txt","w",encoding="utf-8") as file:
    file.write(f"Name:{name}\n")
    file.write(f"Age:{age}\n")
    file.write(f"Favourite colour: {colour}\n")

print("Information saved successfully!")    
# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'

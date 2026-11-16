import random

# Get user to input how many random numbers they want
number = int(input("How many random numbers do you want"))
# Generate this many random numbers
random_numbers = []
for i in range(number):
    random_number = random.randint(1,100)
    random_numbers.append(random_number)

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt","w")as outfile:
    for num in random_numbers:
        outfile.write(str(num) + "\n")

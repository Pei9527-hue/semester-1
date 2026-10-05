# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

# Read numbers form user
numbers = read_numbers()

# Check whether the list is empty
if len(numbers) == 0:
  sys.exit("Error: no numbers provided")

# Calculate minimum
minimum = min(numbers)

# Calculate maximun
maximum = max(numbers)

# Calculate mean
mean = sum(numbers) / len(numbers)

# Caculate median
numbers.sort()

middle = len(numbers) // 2

if len(numbers) % 2 == 1:
  # Odd number
  median = numbers[middle]
else:
  # Even number
  median = (numbers[middle - 1] + numbers[middle]) / 2

# Print results
print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print (f"{mean}")
print(f"Median = {median}")

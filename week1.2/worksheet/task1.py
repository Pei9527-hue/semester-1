# Worksheet 1.2: Task 1 Solution
import sys

# Ask the user to enter a grade
grade = input("Enter your grade: ")

# Check whether the input is an interger
if not grade.isdecimal():
  sys.exit("Error: Grade must be an integer between 0 and 100")

# Convert string to integer
grade = int(grade)

# Check whether the grade is in the valid range
if grade < 0 or grade > 100：
  sys.exit("Error: Grade must be an integer between 0 and 100")

# Grade 
if grade >= 70:
  result = "Distinction"
elif grade >= 40:
  result = "Pass"
else:
  result = "Fail"

# Final
print(f"{grade} is a {result}")

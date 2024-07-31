# -*- coding: utf-8 -*-
"""selfintroduction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qhsx-pECWz5_7mxLm_vgPXE1kVgqCHxN

# Program Introduction.
 This program takes basic information such as first name, last name, birth year, and birth month to calculate the current age of a user. It then prints a personalized greeting message displaying the user's name and age. This simple program demonstrates basic variable assignments, arithmetic operations, and conditional statements in Python
"""

first_name="matthew"
last_name="adams"
current_year=2024
current_month=7
dob=2005
birth_month=10
age=current_year-dob

if (current_month>birth_month ):
 age=age
else :
 age=(current_year-dob-1)
print(("Hi,my name is "),(first_name),(last_name),("and my age is"),(age),("years old!"))

"""# **Explanation:**

1. ***User Information: ***
first_name and last_name store the user's name.
current_year and current_month store the current year and month.
dob and birth_month store the user's year and month of birth.

2. *** Age Calculation:*** The program calculates the initial age by subtracting the birth year from the current year.
If the current month is greater than the birth month, the calculated age remains the same.
If the current month is less than or equal to the birth month, the age is decremented by one year to account for the upcoming birthday.

3. *** Output Greeting:*** The program prints a personalized message using formatted strings, showing the user's full name and age.

4. *** User Input:*** Below is a modified program where user input is taken in.
"""

# Get user input for personal details
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
dob_year = int(input("Enter your year of birth (e.g., 2005): "))
dob_month = int(input("Enter your month of birth (1-12): "))

# Get current date from user
current_year = int(input("Enter the current year (e.g., 2024): "))
current_month = int(input("Enter the current month (1-12): "))

# Calculate age
age = current_year - dob_year
if current_month < dob_month:
    age -= 1

# Output the result
print(f"Hi, my name is {first_name} {last_name} and my age is {age} years old!")
"""
Author: Paul Sommers
Date written: 11/5/2024
Assignment: Module 03 Programming Assignment 1
Short Desc: This program prompts the user to enter a series of single-number numbers
            and calculates the sum of all the numbers in the string.
"""

# Ask the user to input a series of numbers
user_input = input("Enter a series of numbers with no separators: ")

# Initialize the total
total = 0

# Loop through each character in the string
for number in user_input:
    total += int(number)  # Convert each number to an integer and add to the total

# Output the total sum of the numbers
print("The sum of the numbers is:", total)
"""
Author: Paul Sommers
Date written: 11/5/2024
Assignment: Module 03 Programming Assignment 2
Short Desc: This program generates random numbers between 1 to 500, writes them to a file, and displays them to the console. 
            The user specifies how many random numbers to generate.
"""

import random

# Ask the user how many numbers to generate
random_num_quantity = int(input("Enter how many random numbers to generate: "))

# Open a file to write the numbers
with open("randomly_generated_numbers.txt", "w") as file:
    
    # Loop to generate, write, and print numbers
    for _ in range(random_num_quantity):
        random_number = random.randint(1, 500)
        file.write(str(random_number) + "\n")
        print(random_number)
# Create two empty lists called my_numbers and winning_numbers.

# Loop over a range of 5 steps (i.e., range(0,5)) and populate both lists with a random number between 1 and 69.

# Outside the loop, add one more number to each list that is between 1 and 26.

# Lastly, print the my_numbers and winning_numbers lists to the terminal.

import random

my_numbers = []
winning_numbers = []

for i in range(5):
    my_numbers.append(random.randint(1, 69))
    winning_numbers.append(random.randint(1, 69))

my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))

print("My Numbers:", my_numbers)
print("Winning Numbers:", winning_numbers)
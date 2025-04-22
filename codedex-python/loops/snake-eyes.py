# Suppose we have a pair of dice. 🎲 🎲

# "Snake eyes" means rolling two 1s. Why is it called that? The two small dots look like a pair of snake eyes. Ssss. 🐍👀

# It’s the lowest possible roll (1 + 1 = 2) and seen as bad luck. 😅

# Let's keep rerolling two dice until we get snake eyes.

# First, use the random module to “roll” the two dice.

# Each die (die1 and die2) has an integer value from 1 to 6.

# Store the sum of the two random values in a new total variable.

# Until the total is 2, use a while loop to keep "re-roll" the dices and print out a simple 'Nope'.

import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

total = dado1 + dado2

while total != 2:
    print('Ainda não')
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    total = dado1 + dado2

if total == 2:
    print('Olho de cobra!')
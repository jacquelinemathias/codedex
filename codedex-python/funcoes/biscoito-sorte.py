# Create a fortune_cookie.py program that gives the user random fortunes.

# Define a function named fortune(). Inside the function, print out a random fortune from the list of options below:

#     Don't pursue happiness – create it.
#     All things are difficult before they are easy.
#     The early bird gets the worm, but the second mouse gets the cheese.
#     Someone in your life needs a letter from you.
#     Don't just think. Act!
#     Your heart will skip a beat.
#     The fortune you search for is in another cookie.
#     Help! I'm being held prisoner in a Chinese bakery!

# Make sure to use the random module's random.randint() and an if/elif/else.

# Then, call the fortune() function three times and see what you get!

import random

def fortune():
    num  = random.randint(1, 8)
    if num == 1:
        print("Don't pursue happiness - create it.")
    elif num == 2:
        print('All things are difficult before they are easy.')
    elif num == 3:
        print('The early bird gets the worm, but the second mouse gets the cheese.')
    elif num == 4:
        print('Someone in your life needs a letter from you.')
    elif num == 5:
        print("Don't just think. Act!")
    elif num == 6:
        print('Your heart will skip a beat.')
    elif num == 7:
        print('The fortune you search for is in another cookie.')
    else:
        print("Help! I'm being held prisoner in a Chinese bakery!")

fortune()
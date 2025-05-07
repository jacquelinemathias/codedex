# Import the following at the top of the file:

#     From the math module, the pi (π) variable.
#     From the random module, the .choice() method, renamed as ch for short.

# Next, use the ch() method to get a random string from planets and assign it to a variable called random_planet.

# And use the imported pi (π) variable to calculate the surface area of a sphere.

# To do this, we'll need to know the radius r for a given random_planet (rounded to the nearest kilometer).

# Write an if/elif/else statement and assign a value to r with the following in mind:

#     If random_planet is 'Mercury', then r is 2440.
#     Else, if random_planet is 'Venus', then r is 6052.
#     Else, if random_planet is 'Earth', then r is 6371.
#     Else, if random_planet is 'Mars', then r is 3390.
#     Else, if random_planet is 'Saturn', then r is 58232.
#     Else, print "Oops! An error occurred." to the console.

# Lastly, calculate the area and print the name of the random_planet along with its area to the console.

# Bonus: The calculated results may seem a bit long. Is there a built-in Python function that can round it?

from math import pi as π
from random import choice as ch

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn']

random_planet = ch(planets)

if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print("Oops! An error occurred.")

area = 4*π*r*2
arredondar = round(area,2)
print(random_planet, "'s area is", arredondar, 'km2.')
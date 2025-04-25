# Create a new file called rocket.py.

# Define a function named distance_to_miles() that converts a distance from kilometers to miles. It should:

#     Take in one parameter named distance (the distance in kilometers).
#     Print the distance in miles.

# After, call the function and use 10000 as the argument.

def distance_to_miles(distance):
  miles = distance / 1609
  print(miles)

distance_to_miles(1000)
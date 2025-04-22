# Let's make it so that it's the same guessing game, but there is a new limit to the number of tries (it was infinite before).

# First, introduce a variable called tries at the top and give it a value of 0.

# Then, add a second condition with the tries variable to the while loop using a relational operator.

tentativa = 0
numero = 0

while numero != 6 and tentativa < 5:
  numero = int(input("Tente adivinhar o número:  "))
  tentativa += 1

if tentativa == 5:
  print('Acabaram suas chances de adivinhar :(')
else:
  print("Acertou!")
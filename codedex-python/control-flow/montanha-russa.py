# Create a new file called the_cyclone.py.

# Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

# Use a combination of relational and logical operators to create the rules:

#     If they are tall enough and have enough credits, print "Enjoy the ride!"
#     Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
#     Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
#     Else, print a message saying they have not met either requirement.

altura = int(input('Qual sua altura (em cm)?'))
creditos = int(input('Quantos créditos você tem?'))

if altura >= 137 and creditos >= 10:
  print('Aproveite o passeio!')
elif altura < 137 and creditos >= 10:
  print('Você é nanico demais.')
elif altura >= 137 and creditos < 10:
  print('Você não tem dinheiro!')
else:
  print('Nanico e pobre.')
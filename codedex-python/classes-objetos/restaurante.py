# Create a Restaurant class in a restaurants.py file with the following attributes:

#     .name of the type str
#     .category of the type str
#     .rating of the type float
#     .delivery of the type bool

# Make these empty/default values for now.

# Nothing should happen when you run the code, because we have yet to use this class. In the next exercise, we will start using it!

# In a new file called bobs_burgers.py, create an instance of the Restaurant class called bobs_burgers with the following attributes:

#     'Bob\'s Burgers'
#     'American Diner'
#     4.7
#     False

# Once you do that, create two more instances of the Restaurant class with your favorite dinner spots nearby.

# Then, use print(vars()) to output each of the three restaurants!

class Restaurante:
  nome = ''
  categoria = ''
  nota = 0.0
  entrega = False
  
bobs_burgers = Restaurante()
guacamole = Restaurante()
frutos_goias = Restaurante()

bobs_burgers.nome = "Bob's Burgers"
bobs_burgers.categoria = 'American Diner'
bobs_burgers.nota = 4.7
bobs_burgers.entrega = False

guacamole.nome = 'Guacamole'
guacamole.categoria = 'Culinária Mexicana'
guacamole.nota = 5.0
guacamole.entrega = True

frutos_goias.nome = 'Frutos de Goiás'
frutos_goias.categoria = 'Açaí e lanches'
frutos_goias.nota = 4.5
frutos_goias.entrega = False

print(vars(bobs_burgers))
print(vars(guacamole))
print(vars(frutos_goias))
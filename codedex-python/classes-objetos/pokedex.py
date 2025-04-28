# Create a new file called pokedex.py.

# Next, let's define a Pokemon class with the following attributes:

#     entry (integer)
#     name (string)
#     types (list of strings)
#     description (string)
#     is_caught (boolean)

# Note: Make sure to use the __init__() method.

# Next, create an instance method called .speak() that prints a string of the sound a Pokémon makes. A Pokémon usually just says their name, so make the .speak() simply print out their name twice!

# Then, create another instance method called .display_details() that prints the attributes of a Pokemon object like the following:

# Entry Number: 25
# Name: Pikachu
# Type: Electric
# Description: It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
# Pikachu has already been caught!

# Lastly, create three Pokemon class objects and use the .speak() or .display_details() instance methods for each one.

class Pokemon:
    def __init__(self, numero, nome, tipo, fraqueza, descricao, capturado):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.fraqueza = fraqueza
        self.descricao = descricao
        self.capturado = capturado
    
    def fala_pokemon(self):
        print(self.nome, '!', self.nome, '!')
    
    def detalhes(self):
        print('Número na Pokédex: ' + str(self.numero))
        print('Nome: ', self.nome)
        print('Tipo: ', self.tipo)
        print('Fraquezas: ', self.fraqueza)
        print('Descrição: ', self.descricao)
        if self.capturado == True:
            print(self.nome, 'já foi capturado!')
        else:
            print(self.nome, 'ainda não foi capturado!')

porygon = Pokemon(137, 'Porygon', ['Normal'], ['Lutador'], 'Porygon é um Pokémon artificial. Por não respirar, pode ser usado em qualquer tipo de ambiente.', True)

ceruledge = Pokemon(937, 'Ceruledge', ['Fantasma', 'Fogo'], ['Água', 'Terra', 'Pedra', 'Fantasma', 'Escuridão'], 'As lâminas em seus braços queimam com o ressentimento de um espadachim que pereceu antes de atingir seus objetivos.', True)

urshifu_agua = Pokemon(892, 'Urshifu', ['Lutador', 'Água'], ['Planta', 'Elétrico', 'Voador', 'Psíquico', 'Fada'], 'Acredita-se que esse Pokémon modelou seu estilo de luta baseado no curso de um rio - às vezes rápido, às vezes calmo.', False)

porygon.fala_pokemon()
porygon.detalhes()

ceruledge.fala_pokemon()
ceruledge.detalhes()

urshifu_agua.fala_pokemon()
urshifu_agua.detalhes()
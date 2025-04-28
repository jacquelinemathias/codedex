# Create a favorite_cities.py program.

# Let's make a City class that uses the __init__() method to define the following attributes:

#     name (string)
#     country (string)
#     population (integer rounded to the nearest thousand people)
#     landmarks (list of strings)

# Next, create an object for your hometown and assign the attributes above.

# Lastly, create another object of the city that you've always wanted to visit!

# Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.

class Cidade: 
  def __init__(self, nome, pais, populacao, pontos_turisticos, apelido, ano_fundacao, prefeito_2025):
    self.nome = nome
    self.pais = pais
    self.populacao = populacao
    self.pontos_turisticos = pontos_turisticos
    self.apelido = apelido
    self.ano_fundacao = ano_fundacao
    self.prefeito_2025 = prefeito_2025

florianopolis = Cidade('Florianópolis', 'Brasil', 537.211, ['Ponte Hercílio Luz', 'Museu Histórico', 'Praias', 'Mercado Público', 'Fortalezas'], 'Floripa', 1673, 'Topázio Neto')
reykjavik = Cidade('Reykjavik', 'Islândia', 139.875, ['Aurora Boreal', 'Museu Falológico', 'Fontes termais', 'Caminhada em geleiras', 'Igreja de Hallgrímur'], 'Vik', 1786, 'Einar Þorsteinsson')

print(vars(florianopolis))
print(vars(reykjavik))
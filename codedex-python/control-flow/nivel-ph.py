# Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

# First, create a ph variable and ask the user for a value between 0 and 14.

# Write an if, elif, else statement that:

#     If ph is greater than 7, output "Basic".
#     If ph is less than 7, output "Acidic".
#     Else, output "Neutral".

ph = int(input('Informe o nível de pH: '))

if ph > 7 and ph <= 14:
  print('A solução é básica!')
elif ph < 7 and ph >= 0:
  print('A solução é ácida!')
elif ph == 7:
  print('A solução é neutra!')
else:
  print('Por favor, informe um número válido.')
  
# Fiz um pouco diferente de novo, porque não existe pH maior que 14 nem menor que 0.
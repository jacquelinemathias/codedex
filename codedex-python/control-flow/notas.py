# Create a grades.py program that checks whether a grade is above or below 55.

# Start by creating a variable called grade and give it a value between 0-100.

# Write a if/else statement for the following:

#    If grade is greater than or equal to 55, then print "You passed."
#    Else, print "You failed."

# After you run the code, change grade's value and rerun it. Do this a few times to make sure it's working as intended.

nota = int(input('Quanto você tirou na prova?'))

if nota >= 55 and nota <= 100:
  print('Você foi aprovado!')
elif nota >= 0 and nota <= 54:
  print('Você foi reprovado :(')
else:
  print('Por favor, informe um número válido.')
  
# Fiz um pouco diferente do que foi pedido no enunciado!
# Ask the user the month number using the input() function.

# Check for the four seasons using an if/elif/else statement and logical operators:

#     month is 1, 2, 3, print 'Winter 🌨️'
#     month is 4, 5, 6, print 'Spring 🌱'
#     month is 7, 8, 9, print 'Summer 🌻'
#     month is 10, 11, 12, print 'Autumn 🍂'
#     Everything else is 'Invalid'

mes = int(input('Em qual mês do ano você está? '))

if mes == 1 or mes == 2 or mes == 3:
    print('Verão 🌻')
elif mes == 4 or mes == 5 or mes == 6:
    print('Outono 🍂')
elif mes == 7 or mes == 8 or mes == 9:
    print('Inverno 🌨️'),
elif mes == 10 or mes == 11 or mes == 12:
    print('Primavera 🌱')
else:
    print('Inválido.')
    
# Adaptado às estações do Brasil 🌴
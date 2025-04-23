# In a five-star restaurant review system (⭐️⭐️⭐️⭐️⭐️), the stars typically represent the different levels of satisfaction.

# But what does each of the stars mean?

# Start by creating a rating variable and set it equal to a decimal number.

# Make a rating system using an if/elif/else statement:

#     rating greater than 4.5, print 'Extraordinary'
#     rating greater than 4, print 'Excellent'
#     rating greater than 3, print 'Good'
#     rating greater than 2, print 'Fair'
#     Everything else, print 'Poor'

avaliacao = float(input('Avalie o restaurante, com uma nota de 0 a 5 estrelas: '))

if avaliacao > 5 or avaliacao < 0:
    print('Informe um valor válido.')
elif avaliacao > 4.5:
    print('Excelente')
elif avaliacao > 4:
    print('Ótimo')
elif avaliacao > 3:
    print('Bom')
elif avaliacao > 2:
    print('Regular')
else:
    print('Podre...')
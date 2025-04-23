# Create a weight conversion program that:

#     Asks the user what their Earth weight is (as a float).
#     Asks the user for a planet number (as an int).

# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

# To calculate the user's weight:
# destination weight=Earth weight × relative gravity

# Number	Planet	      Relative Gravity
# 1	        Mercury	          0.38
# 2	        Venus	          0.91
# 3	        Mars	          0.38
# 4	        Jupiter	          2.53
# 5	        Saturn	          1.07
# 6	        Uranus	          0.89
# 7	        Neptune	          1.14

# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.

peso = float(input('Quanto você pesa? '))
planeta = int(input('Em qual planeta você gostaria de se pesar? (Escolha um número de 1 a 7) '))

if planeta == 1:
    resultado = peso * 0.38
    print('Em Mercúrio, você pesa ', resultado, ' quilos.')
elif planeta == 2:
    resultado = peso * 0.91
    print('Em Vênus, você pesa ', resultado, ' quilos.')
elif planeta == 3:
    resultado = peso * 0.38
    print('Em Marte, você pesa ', resultado, ' quilos.')
elif planeta == 4:
    resultado = peso * 2.53
    print('Em Júpiter, você pesa ', resultado, ' quilos.')
elif planeta == 5:
    resultado = peso * 1.07
    print('Em Saturno, você pesa ', resultado, ' quilos.')
elif planeta == 6:
    resultado = peso * 0.89
    print('Em Urano, você pesa ', resultado, ' quilos.')
elif planeta == 7:
    resultado = peso * 1.14
    print('Em Netuno, você pesa ', resultado, ' quilos.')
else:
    print('Número inválido.')
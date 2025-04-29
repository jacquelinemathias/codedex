# Write an average() function that takes in two parameters:

#     num1
#     num2

# It should calculate and return the average of the two numbers.

# The average of num1 and num2 is:

# (num1+num2)/2

def media():
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    resultado = (num1 + num2) / 2
    print('A média dos dois números é', resultado)

media()
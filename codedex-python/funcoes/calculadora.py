# Create a calculator.py program and define these five functions:

#     add(a, b) that adds two numbers a and b.
#     subtract(a, b) that subtracts two numbers a and b
#     multiply(a, b) that multiplies two numbers a and b.
#     divide(a, b) that divides two numbers a and b.
#     exp(a, b) that takes a to the exponent (or power) of b.

# Make sure to return the result in each function definition.

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))

def adicao(a, b):
    resultado = a + b
    return resultado

def subtracao(a, b):
    resultado = a - b
    return resultado

def multiplicacao(a, b):
    resultado = a * b
    return resultado

def divisao(a, b):
    resultado = a / b
    return resultado

def exponenciacao(a, b):
    resultado = a ** b
    return resultado

print(adicao(a, b))
print(subtracao(a, b))
print(multiplicacao(a, b))
print(divisao(a, b))
print(exponenciacao(a, b))

# Exercício modificado para atender inputs de usuário, e não precisar alterar o valor de a e b no print o tempo todo.
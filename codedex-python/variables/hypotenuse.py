# Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.
# c = √(a ** 2 + b ** 2), ou
# 

a = int(input('Informe o valor do lado A do triângulo:'))

b = int(input('Informe o valor do lado B do triângulo: '))

c = (a ** 2 + b ** 2) ** 0.5

print(c)
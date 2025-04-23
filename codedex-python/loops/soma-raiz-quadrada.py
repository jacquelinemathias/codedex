# First, ask the user for an integer with int(input()) and store it in a number variable. Then, define a total variable with an initial value of 0.

# Note: You can pass a string prompt to int(input()).

# Next, use a for loop and range() function to calculate the total of the squares of all integers from 1 to that number.

# Last, print the output as an integer value.

num = int(input('Informe um número: '))
total = 0

for numero in range (1, num + 1):
    quadrado = numero ** 2
    total = total + quadrado

print(total)
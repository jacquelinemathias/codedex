# Write a dog_years() function that takes two parameters:

#     name (string)
#     age (integer)

# It should calculate and return a string featuring the dog's name as well as its age in human years.

# For example, if the dogs Landon, Red, and Cooper were 3, 6, and 2 years old respectively:

# dog_years('Landon', 3)
# dog_years('Red Bean', 6)
# dog_years('Cooper', 2)

# The return messages should look like:

# Landon is 21 years old in human years.
# Red Bean is 42 years old in human years.
# Cooper is 14 years old in human years.

def idade_cachorro():
    nome = input('Informe o nome do cachorro: ')
    idade = int(input('Informe a idade do cachorro: '))
    
    idade_humana = idade * 7
    
    return print(nome, 'teria', idade_humana, 'anos se fosse uma pessoa.')

idade_cachorro()
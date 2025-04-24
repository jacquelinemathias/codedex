# Let's use a Python list to find a specific three-letter combination, starting with the following:

# Next, define two variables:

#     item_to_find string that is set as a three-letter combination of your choice, with no spaces (e.g. 'TGA' or 'CAT').
#     item_found boolean, initialized to False.

# Loop through each item in the dna_sequence list. Inside, use an if statement to test if a given item is equal to the item_to_find. If so, set item_found to True.

# Outside the loop, use an if/else statement to check if item_found is True:

#     If so, print something like "Item Found!"
#     Else, print something like "Item not found."

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = input('Informe uma sequência de 3 letras maiúsculas, sem espaços: ')
item_found = False

for i in dna_sequence:
    if i == item_to_find:
        item_found = True

if item_found == True:
    print('Item found!')
else:
    print('Item not found.')

# Alterei o exercício porque ficar mudando a variável manualmente não fazia sentido.
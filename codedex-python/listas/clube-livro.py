# Create a reading_list.py program that stores the following items in a books list:

#     'Harry Potter'
#     '1984'
#     'The Fault in Our Stars'
#     'The Mom Test'
#     'Life in Code'

# Suppose we want to add 'Pachinko' to the list. Can you use a list method to do so?

# Let's say we finished reading 'The Fault in Our Stars' and '1984'. Can you use the .remove() method to remove one and the .pop() method to remove the other?

# Print the updated list out to make sure everything's good to go!

livros = ['Harry Potter', '1984', 'A culpa é das estrelas', 'O teste da mãe', 'Life in Code']

livros.remove('A culpa é das estrelas')
livros.pop(1)

print(livros)
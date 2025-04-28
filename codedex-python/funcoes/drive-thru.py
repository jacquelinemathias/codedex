# Create a drive_thru.py program with your favorite fast food chain's menu.

# Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!

# For example, if you called the function with:

#     Argument value 1, it could return '🍔 Cheeseburger'.
#     Argument value 2, it could return '🍟 Fries'.
#     Argument value 3, it could return '🥤 Soda'.
#     Argument value 4, it could return '🍦 Ice Cream'.
#     Argument value 5, it could return '🍪 Cookie'.

# Make sure to call this function a few times to make sure that it works!

# Lastly, let's do the following:

#     Create a welcome menu and put that in a welcome() function.
#     Create a main program that takes in user input with input().

def welcome():
    print('=========================')
    print('Bem vindo ao restaurante!')
    print('=========================')
    print('Cardápio:')
    print('1) Cheeseburger')
    print('2) Fries')
    print('3) Soda')
    print('4) Ice Cream')
    print('5) Cookie')

welcome()
item = int(input('Bem vindo! O que gostaria de pedir? '))

def get_item():
    if item == 1:
        return('🍔 Cheeseburger')
    elif item == 2:
        return('🍟 Fries')
    elif item == 3:
        return('🥤 Soda')
    elif item == 4:
        return('🍦 Ice Cream')
    elif item == 5:
        return('🍪 Cookie')
    else:
        return('Número inválido!')

pedido = get_item()
print(pedido)
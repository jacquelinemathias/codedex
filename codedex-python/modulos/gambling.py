# Create a symbols list and include the following items: '🍒',' 🍇', '🍉', '7️⃣'.

# Next, create a results variable that uses the .choices() method from the random module and get three random symbols. Make sure to import the required module at the top of the file!

# Then, print each value from results, separated by | pipe characters:

# 🍉 | 🍒 | 🍇

# Lastly, use an if/else statement:

#     If all of the list items in results are equal to '7️⃣', print "Jackpot! 💰".
#     Else, print "Thanks for playing!".

import random

itens = ['🍉', '🍒', '🍇', '7️⃣']

def play():
    resultado = random.choices(itens, k = 3)

    print(resultado[0], '|', resultado[1], '|', resultado[2])

    if resultado[0] == '7️⃣' and resultado[1] == '7️⃣' and resultado[2] == '7️⃣':
        print('Você venceu! 💰')
    else:
        print('Obrigado por jogar :)')

# Bonus:

#     Rewrite this program with a play() function.
#     Add a while loop for the player to keep playing, round after round.
#     Ask the player for a 'Y' or 'N' input to keep playing with input().
   
while True:
    play()
    continuar = input('Deseja continuar? S/N:')
    if continuar != 's' and continuar != 'S':
        print('Jogo encerrado.')
        break
import random

player = 0
comp = 0

print('=====================')
print('Rock, Paper, Scissors')
print('=====================')
print('1) ✊🏻')
print('2) 🖐🏻')
print('3) ✌🏻')

player = int(input('Pick a number: '))
comp = random.randint(1, 3)

if player == 1:
    player = ('✊🏻')
elif player == 2:
    player = ('🖐🏻')
else:
    player = ('✌🏻')

if comp == 1:
    comp = ('✊🏻')
elif comp == 2:
    comp = ('🖐🏻')
else:
    comp = ('✌🏻')

print('You chose: ' + player)
print('CPU chose: ' + comp)

if player == ('✊🏻') and comp == ('✊🏻'):
    print("It's a tie!")
elif player == ('🖐🏻') and comp == ('🖐🏻'):
    print("It's a tie!")
elif player == ('✌🏻') and comp == ('✌🏻'):
    print("It's a tie!")
elif player == ('✊🏻') and comp == ('🖐🏻'):
    print('CPU won!')
elif player == ('🖐🏻') and comp == ('✊🏻'):
    print('You won!')
elif player == ('✌🏻') and comp == ('✊🏻'):
    print('CPU won!')
elif player == ('✊🏻') and comp == ('✌🏻'):
    print('You won!')
elif player == ('✌🏻') and comp == ('🖐🏻'):
    print('You won!')
else:
    print('CPU won!')